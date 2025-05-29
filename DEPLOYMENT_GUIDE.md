# IoT Anomaly Detection API Deployment Guide

## Prerequisites
- Docker and Docker Compose installed
- API key (provided by the team)
- (Optional) Data files for full operation (see README.md)

## 1. Environment Setup
1. Clone the repository:
   ```sh
git clone <repository-url>
cd iot_anomaly_detection
   ```
2. Create a `.env` file in the project root with:
   ```env
API_KEY=<your-api-key-here>
PYTHONUNBUFFERED=1
   ```
   Replace `<your-api-key-here>` with the provided key.

## 2. Build and Start the Services
Run:
```sh
docker compose up --build -d
```
This will start:
- The API (FastAPI, port 8005)
- Prometheus (port 9090)
- Grafana (port 3000)

## 3. Test the API

### Health Check
```sh
curl http://localhost:8005/health
```
Should return:
```json
{"status":"healthy","version":"1.0.0","models_loaded":["autoencoder","lstm","dlrm","rnn"]}
```

### Prediction Endpoint
Send a POST request with exactly 10 features:
```sh
curl -X POST "http://localhost:8005/predict" \
  -H "X-API-Key: <your-api-key-here>" \
  -H "Content-Type: application/json" \
  -d '{"data":[1,2,3,4,5,6,7,8,9,10],"model_type":"autoencoder"}'
```
Response example:
```json
{
  "anomaly_score": 0.0123,
  "is_anomaly": false,
  "confidence": 0.95,
  "model_used": "autoencoder",
  "timestamp": "2024-06-07T12:34:56"
}
```

## 4. Monitoring
- Prometheus: [http://localhost:9090](http://localhost:9090)
- Grafana: [http://localhost:3000](http://localhost:3000) (default login: admin/admin)

## 5. Stopping the Services
```sh
docker compose down
```

## 6. Troubleshooting
- If the API is not responding, check logs:
  ```sh
  docker compose logs api
  ```
- If you get a "must have 10 features" error, ensure your `data` array has exactly 10 numbers.
- If you change code or ports, rebuild and restart:
  ```sh
  docker compose down
  docker compose up --build -d
  ```

## 7. Additional Information
- See `README.md` for data setup and more details.
- See `API_HANDOVER_DOCUMENTATION.md` for full API details.

---
**Ready for backend integration!** 