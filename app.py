import torch
import torch.nn as nn
import numpy as np
from fastapi import FastAPI, HTTPException, Depends, Security, Response
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
import os
from datetime import datetime
from prometheus_client import Counter, Gauge, Histogram, generate_latest
import time
from dotenv import load_dotenv
from models import EnhancedAutoencoder, EnhancedLSTM, EnhancedDLRM, EnhancedRNN

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="IoT Anomaly Detection API",
    description="API for detecting anomalies in IoT sensor data using multiple models",
    version="1.0.0"
)

# API Key security
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

# Prometheus metrics
prediction_counter = Counter('predictions_total', 'Total number of predictions')
anomaly_counter = Counter('anomalies_detected', 'Total number of anomalies detected')
prediction_latency = Histogram('prediction_latency_seconds', 'Prediction latency in seconds')
model_memory_usage = Gauge('model_memory_usage_bytes', 'Memory usage of models in bytes', ['model_name'])

# Define input data model with fixed namespace warning
class SensorData(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    data: List[float]
    timestamp: Optional[str] = None
    model_type: Optional[str] = "autoencoder"  # Default model type

# Load all models
models = {}
try:
    # Load Autoencoder
    autoencoder_dict = torch.load('models/enhanced_autoencoder.pth')
    input_dim = autoencoder_dict['encoder.0.weight'].shape[1]
    models['autoencoder'] = EnhancedAutoencoder(input_dim)
    models['autoencoder'].load_state_dict(autoencoder_dict)
    models['autoencoder'].eval()

    # Load LSTM
    lstm_dict = torch.load('models/enhanced_lstm.pth')
    models['lstm'] = EnhancedLSTM(input_dim)
    models['lstm'].load_state_dict(lstm_dict)
    models['lstm'].eval()

    # Load DLRM
    dlrm_dict = torch.load('models/enhanced_dlrm.pth')
    models['dlrm'] = EnhancedDLRM(input_dim)
    models['dlrm'].load_state_dict(dlrm_dict)
    models['dlrm'].eval()

    # Load RNN
    rnn_dict = torch.load('models/enhanced_rnn.pth')
    models['rnn'] = EnhancedRNN(input_dim)
    models['rnn'].load_state_dict(rnn_dict)
    models['rnn'].eval()

    # Update memory usage metric
    for model_name, model in models.items():
        model_memory_usage.labels(model_name=model_name).set(
            sum(p.numel() * p.element_size() for p in model.parameters())
        )

except Exception as e:
    print(f"Error loading models: {str(e)}")
    raise

# API key validation
async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header != os.getenv("API_KEY"):
        raise HTTPException(
            status_code=403,
            detail="Invalid API Key"
        )
    return api_key_header

# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "models_loaded": list(models.keys())
    }

# Prediction endpoint
@app.post("/predict")
async def predict(
    data: SensorData,
    api_key: str = Depends(get_api_key)
):
    start_time = time.time()
    
    try:
        # Validate input data
        if len(data.data) != input_dim:
            raise HTTPException(
                status_code=400,
                detail=f"Input data must have {input_dim} features"
            )

        # Convert input to tensor
        input_tensor = torch.FloatTensor(data.data).unsqueeze(0)
        
        # Get model
        model_type = data.model_type.lower()
        if model_type not in models:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid model type. Available models: {list(models.keys())}"
            )
        
        model = models[model_type]
        
        # Make prediction
        with torch.no_grad():
            output = model(input_tensor)
            reconstruction_error = torch.mean((output - input_tensor) ** 2).item()
        
        # Determine if anomaly
        threshold = 0.1  # This should be calibrated based on your data
        is_anomaly = reconstruction_error > threshold
        
        # Update metrics
        prediction_counter.inc()
        if is_anomaly:
            anomaly_counter.inc()
        prediction_latency.observe(time.time() - start_time)
        
        return {
            "anomaly_score": reconstruction_error,
            "is_anomaly": bool(is_anomaly),
            "confidence": 1.0 - min(reconstruction_error / threshold, 1.0),
            "model_used": model_type,
            "timestamp": data.timestamp or datetime.now().isoformat()
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction error: {str(e)}"
        )

# Metrics endpoint for Prometheus
@app.get("/metrics")
async def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
