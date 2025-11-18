import time
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/hello')
def hello():
    print("Hello world!")
    return jsonify({"message": "hello world!"})

if __name__ == '__main__':
    app.run(port=5000)
