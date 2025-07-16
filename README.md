# GCP Proof of Life - Cloud Run Service

A simple REST API service designed for quick deployment to Google Cloud Run to test connectivity and authentication from external systems like ServiceNow.

## Overview

This proof-of-life application provides a minimal REST API with API key authentication to verify that external systems can successfully reach and authenticate with a Cloud Run service.

## Features

- Simple REST API with multiple endpoints
- API key authentication via headers
- JSON responses with timestamps
- Health check endpoint
- Ping/pong test endpoint
- Containerized for Cloud Run deployment
- Fast deployment with included scripts

## API Endpoints

### `GET /`
Returns service information and available endpoints.

### `GET /health`
Health check endpoint that returns service status.
- **Authentication**: Required
- **Response**: Service health status with timestamp

### `GET|POST /ping`
Ping endpoint that returns "pong" response.
- **Authentication**: Required  
- **Response**: Pong message with timestamp and method
- **POST**: Echoes back any JSON payload sent

## Authentication

The service uses API key authentication. Include your API key in one of these headers:
- `X-API-Key: your-api-key`
- `Authorization: Bearer your-api-key`

## Quick Start

### Prerequisites
- Google Cloud SDK installed and configured
- Docker (optional, for local testing)
- Python 3.11+ (for local development)

### Deployment

1. **Create deployment script from template:**
   ```bash
   cp deploy.sh.template deploy.sh
   ```

2. **Configure deployment script:**
   ```bash
   # Edit deploy.sh and replace placeholder values:
   PROJECT_ID="your-gcp-project-id"
   API_KEY="your-secure-api-key"
   ```

3. **Make script executable and deploy:**
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

4. **Test the service:**
   ```bash
   curl -H "X-API-Key: your-api-key" https://your-service-url/health
   ```

### Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables:**
   ```bash
   export API_KEY="your-test-key"
   export PORT=8080
   ```

3. **Run locally:**
   ```bash
   python app.py
   ```

## ServiceNow Integration

To test from ServiceNow, use these settings:

- **URL**: `https://your-service-url/ping`
- **Method**: `POST`
- **Headers**: `X-API-Key: your-api-key`
- **Content-Type**: `application/json`
- **Body**: `{"test": "data from ServiceNow"}`

## Testing Examples

### Health Check
```bash
curl -H "X-API-Key: your-api-key" \
  https://your-service-url/health
```

### Ping Test
```bash
curl -H "X-API-Key: your-api-key" \
  https://your-service-url/ping
```

### POST with Data
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key" \
  -d '{"test": "data from ServiceNow"}' \
  https://your-service-url/ping
```

## Project Structure

```
gcp-proof-of-life/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container configuration
├── deploy.sh.template # Deployment script template
├── deploy.sh.template # Deployment script template
├── deploy.sh          # Deployment script (local only, not in git)
├── test_requests.md   # Testing documentation
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Security Notes

- The `deploy.sh` script is excluded from version control as it contains sensitive API keys
- Change the default API key before deployment
- Consider using Google Cloud Secret Manager for production deployments
- The service allows unauthenticated access to Cloud Run but requires API key for endpoints

## Troubleshooting

### Common Issues

1. **Authentication errors**: Verify API key is correctly set in headers
2. **Deployment failures**: Check GCP project ID and permissions
3. **Service not responding**: Verify Cloud Run service is running and accessible

### Getting Service URL
```bash
gcloud run services describe gcp-proof-of-life --region=us-central1 --format='value(status.url)'
```

## Contributing

This is a proof-of-concept project. Modify as needed for your specific testing requirements.
