from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/data')
def send_data():
    return jsonify({"message": "Hello from Python backend!"})

@app.route('/info')
def send_info():
    return jsonify({"info": "This is extra data from Flask!"})

@app.route('/users')
def get_users():
    users = [
        {"id": 1, "name": "Dorukhan"},
        {"id": 2, "name": "Esmer"},
        
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
