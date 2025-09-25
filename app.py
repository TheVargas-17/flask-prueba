from flask import Flask
app = Flask(__name__)

@app.route('/')
def holas_mundo():
    return '<h1> hola mundo ,desde flask</h1>'
if __name__ == '__main__':
    app.run(debug=True)