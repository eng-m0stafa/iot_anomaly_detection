# IoT Anomaly Detection Project

This repository contains an anomaly detection system for IoT sensor data using multiple deep learning models.

## Project Structure

- `app.py`: Main application file
- `models.py`: Model definitions
- `train_models.py`: Training scripts
- `requirements.txt`: Project dependencies
- `prometheus.yml`: Prometheus configuration
- `dashboard.json`: Grafana dashboard configuration

## Data Files

The data files for this project are stored in the following directories:
- `CyPhy/`: Contains the CyPhy dataset
- `Master/`: Contains the Master dataset

These directories are not included in the repository due to their size. The data files can be downloaded from our Google Drive:
[Download Data Files](https://drive.google.com/drive/folders/1xlgUnIGV5O_M7owjcbi-MtfSXAWaXC4t)

The data files include:
- `BREMaster.csv` (1.14 GB)
- `CUMaster.csv` (3.82 GB)
- `Phy_BRE_Master.csv` (4.99 GB)

Please download these files and place them in the appropriate directories:
- Place `BREMaster.csv` and `CUMaster.csv` in the `Master/` directory
- Place `Phy_BRE_Master.csv` in the `CyPhy/` directory

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/eng-m0stafa/iot_anomaly_detection.git
   cd iot_anomaly_detection
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On Linux/Mac
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the data files from Google Drive and place them in the appropriate directories:
   - Place `BREMaster.csv` and `CUMaster.csv` in the `Master/` directory
   - Place `Phy_BRE_Master.csv` in the `CyPhy/` directory

5. Run the application:
   ```bash
   python app.py
   ```

## Model Training

To train the models:
```bash
python train_models.py
```

## API Documentation

The API documentation is available at `http://localhost:8003/docs` when the application is running.

## Monitoring

- Prometheus metrics are available at `/metrics`
- Grafana dashboard is provided in `dashboard.json`

## Documentation

Additional documentation is available in:
- `DEPLOYMENT.md`: Deployment instructions
- `HANDOVER_CHECKLIST.md`: Project handover checklist
- `DATA_DOCUMENTATION.md`: Data documentation
- `API_HANDOVER_DOCUMENTATION.md`: API documentation

## License

MIT License - See LICENSE file for details
