from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    encrypted_password = generate_password_hash(data['password'], method='bcrypt')

    # Store the encrypted password in the database

    return jsonify({'message': 'User successfully registered!'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Retrieve the encrypted password from the database

    if check_password_hash(stored_encrypted_password, data['password']):
        return jsonify({'message': 'User successfully logged in!'})
    else:
        return jsonify({'message': 'Incorrect password!'})

if __name__ == '__main__':
    app.run(debug=True)