from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return f'Hello from my Flask Endpoint Server'

@app.route('/hello', methods=['GET'])
def hello_get():
    name = request.args.get('name', 'World')
    lastname = request.args.get('lastname', 'no last name provided')
    nameCapital = name.upper()
    lastnameCapital = lastname.upper()
    return f'Hello {nameCapital}{lastnameCapital}!'
# /hello?name=lol&lastname=john (example)


@app.route('/calculation', methods=['GET'])
def calculation_path():
    number = request.args.get('number', 10)
    number_real = int(number)
    number_analyzed = number_real * number_real
    return f'number analyzed is: {number_analyzed}'
# /calculation?number=3 (example)

@app.route('/hello', methods=['POST'])
def hello_post():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    
    name = data.get('name', 'World')
    return jsonify({'message': f'Hello {name}!'})

if __name__ == '__main__':
    app.run(debug=True)


## test CURL for post:
# curl -X POST http://localhost:5000/hello -H "Content-Type: application/json" -d '{"name": "Cooper"}'

## test CURL for get:
# curl -X GET http://localhost:5000/hello?name=Cooper