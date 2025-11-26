import time
from flask import Flask, request, jsonify
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


@app.route('/submitInsec', methods=['POST'])
def submitInsec():
    if request.is_json:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')

        print("Name:", name)
        print("Email:", email)

        return jsonify({
            "message": f"Data recieved successfully! Hello {name}, {email}"
        }), 200
    else:
        return jsonify({"message": "Data error, wtf?!"}), 400

if __name__ == '__main__':
    app.run(port=5000)
