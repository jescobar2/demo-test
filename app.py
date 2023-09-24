from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    host = os.uname()[1]
    return f"Hello, fucking world!\nVersion: 1.0.0\nHostname: {host}\n"

if __name__ == '__main__':
    port = os.environ.get('PORT', '8081')
    app.run(host='0.0.0.0', port=int(port))