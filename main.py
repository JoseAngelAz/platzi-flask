from flask import Flask
app = Flask(__name__)

#Rutas
@app.route('/')
def hello():
    return 'HOla mundo FLASK'