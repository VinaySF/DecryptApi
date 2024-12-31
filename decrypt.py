from flask import Flask, request, jsonify
from cryptography.fernet import Fernet # type: ignore

app = Flask(__name__)

@app.route('/decrypt', methods=['POST'])
def decrypt_payload():
    try:
        # Parse the JSON input
        data = request.get_json()
        
        # Validate input
        if not data or 'encrypted_payload' not in data or 'secret_key' not in data:
            return jsonify({'error': 'Missing encrypted_payload or secret_key'}), 400
        
        encrypted_payload = data['encrypted_payload']
        secret_key = data['secret_key']

        # Decode and decrypt the payload
        fernet = Fernet(secret_key.encode())
        decrypted_data = fernet.decrypt(encrypted_payload.encode()).decode()

        return jsonify({'decrypted_payload': decrypted_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
