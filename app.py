from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home_get():
    name = request.args.get('name', 'World')
    lastname = request.args.get('lastname', 'no last name provided')
    nameCapital = name.upper()
    lastnameCapital = lastname.upper()

    response = {
        "message": f'Hello {nameCapital}{lastnameCapital}!'
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
