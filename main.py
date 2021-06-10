from flask import Flask,request,make_response,redirect, render_template, session
from flask_bootstrap import Bootstrap
app = Flask(__name__)#nombre de la app es main.py

#instancia de bootstrap
bootstrap = Bootstrap(app)
#lista
todos = ['Comprar cafe','Enviar Solicitud de compra','Entregar el Producto']
#llave secreta
app.config['SECRET_KEY']='SUPER SECRETO'

#Rutas
@app.route('/')
def index():
    ip_user = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = ip_user
    return response
@app.route('/hello')
def hello():
    user_ip = request.session.get('user_ip')
    #cuando hay muchos parametros para pasar a la vista mejor pasarla como un contexto en un diccionario
    context = {
         'user_ip':user_ip,
         'todos':todos 
    }
    return render_template('hello.html',**context)

#manejador de errores

@app.errorhandler(404)
def notfound(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)   
def ServerError(error):
    return render_template('500.html', error=error)
