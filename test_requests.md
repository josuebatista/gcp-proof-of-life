# Testing the Cloud Run Service

## Quick Deploy
1. Update `PROJECT_ID` and `API_KEY` in `deploy.sh`
2. Run: `./deploy.sh`

## Test Endpoints

### Health Check
```bash
curl -H "X-API-Key: your-secure-api-key-here" https://your-service-url/health
```

### Ping Test
```bash
curl -H "X-API-Key: your-secure-api-key-here" https://your-service-url/ping
```

### POST Test
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-secure-api-key-here" \
  -d '{"test": "data from ServiceNow"}' \
  https://your-service-url/ping
```

## ServiceNow Integration
Use these settings in ServiceNow:
- **URL**: `https://your-service-url/ping`
- **Method**: POST
- **Headers**: `X-API-Key: your-secure-api-key-here`
- **Content-Type**: `application/json`