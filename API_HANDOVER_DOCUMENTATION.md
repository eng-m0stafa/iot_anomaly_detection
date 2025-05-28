# Anomaly Detection API Handover Documentation

## 1. API Overview

The Anomaly Detection API is built using FastAPI and provides endpoints for detecting anomalies in IoT sensor data using an autoencoder model.

### 1.1 Current Endpoints

1. **GET /** - Welcome endpoint
   - Returns: `{"message": "Welcome to the Anomaly Detection API"}`

2. **POST /predict** - Anomaly detection endpoint
   - Input: JSON with sensor data array
   - Output: Anomaly detection results

## 2. Required Files

The following files must be included in the deployment:
- `app.py` - Main API application
- `anomaly_detection_pipeline.pth` - Trained model weights
- `scaler.pkl` - Data scaler for preprocessing
- `requirements.txt` - Dependencies list

## 3. API Authentication

Currently, the API doesn't have authentication. Here are the recommended steps to add security:

1. **Add API Key Authentication**:
```python
from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader

API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header != "your-secret-api-key":
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key_header
```

2. **Add to endpoints**:
```python
@app.post("/predict")
async def predict(data: SensorData, api_key: str = Security(get_api_key)):
    # existing code
```

## 4. Environment Setup

### 4.1 Required Dependencies
```
fastapi==0.115.12
uvicorn==0.34.2
torch==2.7.0
numpy==2.2.6
joblib==1.5.1
scikit-learn
```

### 4.2 Environment Variables
Create a `.env` file with:
```
API_KEY=your-secret-api-key
MODEL_PATH=anomaly_detection_pipeline.pth
SCALER_PATH=scaler.pkl
```

## 5. Data Format

### 5.1 Input Format
```json
{
    "data": [float, float, ...]  // Array of sensor readings
}
```

### 5.2 Output Format
```json
{
    "reconstruction_error": float,
    "is_anomaly": boolean,
    "threshold": float
}
```

## 6. Model Details

### 6.1 Architecture
- Autoencoder with 3-layer encoder and decoder
- Input dimension: Variable (based on sensor data)
- Hidden layers: 64 → 32 → 16 → 32 → 64 → input_dim

### 6.2 Preprocessing
- Data scaling using StandardScaler
- Input reshaping to match model requirements

## 7. Deployment Considerations

### 7.1 Production Settings
```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001,
        workers=4,  # Adjust based on server capacity
        ssl_keyfile="path/to/key.pem",  # For HTTPS
        ssl_certfile="path/to/cert.pem"  # For HTTPS
    )
```

### 7.2 Monitoring
- Add logging
- Implement health check endpoint
- Set up error tracking

## 8. Testing

### 8.1 Test Cases
```python
def test_predict_endpoint():
    test_data = {"data": [1.0, 2.0, 3.0, 4.0, 5.0]}
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    assert "reconstruction_error" in response.json()
```

## 9. Pending Tasks

1. **Security**:
   - [ ] Implement API key authentication
   - [ ] Add rate limiting
   - [ ] Set up HTTPS

2. **Monitoring**:
   - [ ] Add logging system
   - [ ] Implement health checks
   - [ ] Set up error tracking

3. **Documentation**:
   - [ ] Add OpenAPI/Swagger documentation
   - [ ] Create API usage examples
   - [ ] Document error codes

4. **Performance**:
   - [ ] Add caching
   - [ ] Optimize model inference
   - [ ] Implement batch processing

## 10. Handover Checklist

- [ ] Share API documentation
- [ ] Provide API key
- [ ] Share model files
- [ ] Set up deployment environment
- [ ] Conduct knowledge transfer session
- [ ] Create monitoring dashboard
- [ ] Document known issues
- [ ] Set up backup procedures

## 11. Contact Information

For any questions or issues, contact:
- Name: [Your Name]
- Email: [Your Email]
- Role: Anomaly Detection Team Lead

## 12. Additional Resources

- [Link to model training documentation]
- [Link to data preprocessing documentation]
- [Link to API testing documentation]

---

*Note: This documentation should be updated as the API evolves.* 