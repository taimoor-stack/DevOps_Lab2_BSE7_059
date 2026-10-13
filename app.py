from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Lab Assignment 1 - BSE7_059</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)