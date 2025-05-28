# Deployment Guide

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

## Installation Steps

1. Clone the repository:
```bash
git clone <repository-url>
cd iot-anomaly-detection
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
- Create a `.env` file in the project root
- Add your API key: `API_KEY=your_api_key_here`

5. Train the models:
```bash
python train_models.py
```

6. Run the application:
```bash
python app.py
```

## Environment Variables
- `API_KEY`: Your API key for authentication
- `PORT`: (Optional) Port number for the API (default: 8003)

## Monitoring Setup
1. Install Prometheus:
```bash
# Download Prometheus from https://prometheus.io/download/
# Extract and run:
./prometheus --config.file=prometheus.yml
```

2. Install Grafana:
```bash
# Download Grafana from https://grafana.com/grafana/download
# Install and start the service
```

3. Configure Grafana:
- Add Prometheus as a data source
- Import the provided dashboard (dashboard.json)
