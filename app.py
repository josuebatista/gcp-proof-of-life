from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

VALID_API_KEY = os.environ.get('API_KEY', 'default-test-key-123')

def validate_api_key():
    api_key = request.headers.get('X-API-Key') or request.headers.get('Authorization')
    if api_key and api_key.startswith('Bearer '):
        api_key = api_key[7:]
    return api_key == VALID_API_KEY

@app.route('/health', methods=['GET'])
def health_check():
    if not validate_api_key():
        return jsonify({'error': 'Invalid or missing API key'}), 401
    
    return jsonify({
        'status': 'healthy',
        'message': 'Cloud Run service is operational',
        'timestamp': datetime.utcnow().isoformat(),
        'service': 'gcp-proof-of-life'
    })

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if not validate_api_key():
        return jsonify({'error': 'Invalid or missing API key'}), 401
    
    response_data = {
        'message': 'pong',
        'timestamp': datetime.utcnow().isoformat(),
        'method': request.method,
        'service': 'gcp-proof-of-life'
    }
    
    if request.method == 'POST' and request.is_json:
        response_data['received_data'] = request.get_json()
    
    return jsonify(response_data)

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        'message': 'GCP Proof of Life Service',
        'endpoints': {
            '/health': 'Health check endpoint',
            '/ping': 'Ping endpoint (GET/POST)'
        },
        'authentication': 'Send API key in X-API-Key header or Authorization: Bearer <key>'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)