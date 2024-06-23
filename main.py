import firebase_admin
from firebase_admin import credentials

# setup flask and cors
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

cred = credentials.Certificate("your_service_key.json")


@app.route('/', methods=['GET'])
def home():
    return jsonify({'message':'Welcome to Firebase Server'})

@app.route('/get-token', methods=['GET'])
def get_token():
    init=firebase_admin.initialize_app(cred)
    access_token=init._credential.get_access_token()[0]
    expiry=init._credential.get_access_token()[1]
    return jsonify({'access_token':access_token, 'expiry':expiry})

if __name__ == '__main__':
    app.run(debug=True)

