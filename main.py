from flask import Flask
app = Flask(__name__)#nombre de la app es main.py

#Rutas
@app.route('/')
def hello():
    return 'HOla mundo FLASK'