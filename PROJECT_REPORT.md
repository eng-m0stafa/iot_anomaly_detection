# Cyber-Physical System Project Report

## 1. Project Overview

This project implements a comprehensive cyber-physical system that combines IoT sensor data collection, anomaly detection, and a web-based API for real-time monitoring and analysis. The system is designed to process and analyze data from physical sensors while providing cyber security monitoring capabilities.

## 2. System Architecture

### 2.1 Components

1. **Physical Layer**
   - IoT sensors collecting various environmental data
   - Data points include:
     - Temperature
     - Humidity
     - Pressure
     - PIR (Passive Infrared) motion detection
     - Noise levels (Low, Medium, High, Average)
     - Particulate Matter (PM) measurements
     - Various other environmental metrics

2. **Cyber Layer**
   - Data processing and analysis pipeline
   - Anomaly detection system
   - Web API for real-time monitoring

3. **Integration Layer**
   - Data synchronization between physical and cyber components
   - Real-time data processing and analysis

### 2.2 Data Flow

1. Sensor data collection
2. Data preprocessing and normalization
3. Anomaly detection processing
4. API-based data access and monitoring

## 3. Technical Implementation

### 3.1 Data Processing Pipeline

The data processing pipeline is implemented across several Jupyter notebooks:

- `Physical_DataProcessing_Final.ipynb`: Handles physical sensor data processing
- `Cyber_DataProcessing_Final.ipynb`: Processes cyber-related data
- `CyPhy_DataProcessing_Final.ipynb`: Integrates both physical and cyber data streams

### 3.2 Anomaly Detection System

The anomaly detection system uses an autoencoder neural network architecture:

```python
class Autoencoder(torch.nn.Module):
    def __init__(self, input_dim):
        super(Autoencoder, self).__init__()
        self.encoder = torch.nn.Sequential(
            torch.nn.Linear(input_dim, 64),
            torch.nn.ReLU(),
            torch.nn.Linear(64, 32),
            torch.nn.ReLU(),
            torch.nn.Linear(32, 16)
        )
        self.decoder = torch.nn.Sequential(
            torch.nn.Linear(16, 32),
            torch.nn.ReLU(),
            torch.nn.Linear(32, 64),
            torch.nn.ReLU(),
            torch.nn.Linear(64, input_dim)
        )
```

### 3.3 Web API

The system provides a FastAPI-based web interface (`app.py`) with the following endpoints:

- `GET /`: Welcome message
- `POST /predict`: Anomaly detection endpoint

## 4. Data Analysis and Results

### 4.1 Data Processing Steps

1. **Data Collection**
   - Raw sensor data collection
   - Timestamp synchronization
   - Data normalization

2. **Preprocessing**
   - Handling missing values
   - Data scaling
   - Feature engineering

3. **Analysis**
   - Statistical analysis
   - Pattern recognition
   - Anomaly detection

### 4.2 Key Metrics

The system monitors various environmental and system metrics:

- Temperature variations
- Humidity levels
- Pressure readings
- Motion detection
- Noise levels
- Particulate matter concentrations
- System performance metrics

## 5. Project Files

### 5.1 Core Components

- `app.py`: Web API implementation
- `anomaly_detection.ipynb`: Anomaly detection model development
- `IoTGarageCyberPhysical.py`: Core library implementation
- `anomaly_detection_pipeline.pth`: Trained model weights
- `scaler.pkl`: Data scaling parameters

### 5.2 Data Processing Notebooks

- `Physical_DataProcessing_Final.ipynb`
- `Cyber_DataProcessing_Final.ipynb`
- `CyPhy_DataProcessing_Final.ipynb`
- `Physical_CyPhy_Master_Final.ipynb`
- `Cyber_Physical_CyPhy_Master_Final.ipynb`

## 6. Setup and Deployment

### 6.1 Requirements

The project requires the following key dependencies:
- Python 3.x
- PyTorch
- FastAPI
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Uvicorn

### 6.2 Running the System

1. Start the web API:
```bash
python app.py
```

2. Access the API at `http://localhost:8000`

## 7. Future Improvements

1. Enhanced anomaly detection algorithms
2. Real-time visualization dashboard
3. Automated alert system
4. Extended sensor support
5. Improved data processing pipeline
6. Advanced security features

## 8. Conclusion

This cyber-physical system successfully integrates IoT sensor data collection with advanced data processing and anomaly detection capabilities. The system provides a robust foundation for monitoring and analyzing environmental and system metrics while maintaining security and reliability.

---

*Note: This report is based on the current state of the project and may be updated as the system evolves.* 