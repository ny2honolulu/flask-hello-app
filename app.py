from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Python 3.12 and Flask!"

if __name__ == '__main__':
    app.run(debug=True)
