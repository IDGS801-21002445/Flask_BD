import math
from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms

app = Flask(__name__)
##Forma de redirigir a págias de error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.before_request
def before_request():
    g.nombre = 'Mario'
    print('before 1')

@app.after_request
def after_request(response):
    print('After 1')
 
    return response
@app.route("/")
def index() :
    return render_template("index.html")

@app.route("/resultado", methods=["GET","POST"])
def resultado() :

    if request.method == "POST" :
        numero1 = request.form.get("n1")
        numero2 = request.form.get("n2")
        res_suma = numero1 + numero2
        res_resta = numero1 - numero2
        res_multiplicacion = numero1 * numero2
        res_division = numero1 / numero2

        if request.form.get("suma") :
            return "La suma de {} + {} da como resultado {}".format(numero1, numero2, res_suma)
        elif request.form.get("resta") :
            return "La suma de {} + {} da como resultado {}".format(numero1, numero2, res_resta)
        elif request.form.get("multiplicacion") :
            return "La suma de {} + {} da como resultado {}".format(numero1, numero2, res_multiplicacion)
        elif request.form.get("division") :
            return "La suma de {} + {} da como resultado {}".format(numero1, numero2, res_division)
    return "No aplica"

@app.route("/operaciones", methods=['GET','POST'])
def operaciones():

    return render_template("index.html")

@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
    print('alumno {}'.format(g.nombre))
    nom=""
    apa = ""
    ama = ""
    email = ""
    edad =""
    alumno_clase=forms.UserForm(request.form)
    if request.method == "POST" and alumno_clase.validate():
        nom = alumno_clase.nombre.data
        apa = alumno_clase.apaterno.data
        ama = alumno_clase.amaterno.data
        email = alumno_clase.email.data
        edad = alumno_clase.edad.data

        print('Nombre: {}'.format(nom))
        print('apaterno: {}'.format(apa))
        print('amaterno: {}'.format(ama))
        print('edad: {}'.format(edad))
        print('email: {}'.format(email))
        ##Mensajes de respuesta de la aplicación
        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)

    return render_template("alumnos.html", form=alumno_clase,nom=nom,apa=apa,ama=ama,email=email)

@app.route("/maestros", methods=['GET','POST'])
def distancia():
  
    "Hola desde FLASK"
    return "Hola desde FLASK"

if __name__ == "__main__":
    
    app.run(debug=True)

