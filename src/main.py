import datetime
from flask import Flask, jsonify, request
import json
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def main():
    data = {
        "message": "Welcome to FLASK API 2.0"
    }
    return jsonify(data), 200# GET

@app.route('/api/message', methods=['POST', 'PUT'])
def show_message():

    body = request.data
    data = json.loads(body)
    print(body)
    print(data['message'], 1)

    body_json = request.get_json()
    print(body_json['message'], 2)

    message = request.json.get("message")
    print(message, 3)

    person = "{\"name\":\"Luis\"}";
    person = json.loads(person)
    print(person['name'])

    person = {"name": "Luis" }
    person = json.dumps(person)
    print(person)
 
    return jsonify(data)


@app.route('/api/test-methods', methods=['GET', 'POST', 'PUT', 'DELETE'])
def test_methods():
    if request.method == 'GET':
        return jsonify({ "method": request.method }), 200
    if request.method == 'POST':
        return jsonify({ "method": request.method }), 200
    if request.method == 'PUT':
        return jsonify({ "method": request.method }), 200
    if request.method == 'DELETE':
        return jsonify({ "method": request.method }), 200


@app.route('/api/saludo/<name>/<surname>', methods=['GET'])
def saludo(name, surname):
    firstname = "John"
    lastname = "Doe"
    text = f'{firstname} {lastname}'
    print(text)
    return jsonify({ "message": f'Hola {name} {surname}'}), 200

if __name__ == "__main__":
    app.run()


# text = `${name} ${lastnamr}`
