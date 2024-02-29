
from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms

from models import db
from models import Alumnos


app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

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
# @app.route("/")
# def index() :
#     return render_template("index.html")

@app.route("/alumnosr", methods=['GET','POST'])
def alumnosr():
    print('Nombre:')

    return render_template("alumnos.html")

@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
    print('alumno {}'.format(g.nombre))
    nom=""
    apa = ""
    ama = ""
    email = ""
    edad =0
    create_form=forms.UserForm(request.form)
    if request.method=='POST':
        alum=Alumnos(nombre=create_form.nombre.data,
                     apaterno=create_form.nombre.data,
                     email=create_form.nombre.data)
        db.session.add(alum)
        db.session.commit()
    return render_template('alumnos.html',form=create_form)
    #alumno_clase=forms.UserForm(request.form)
    ##if request.method == "POST" and alumno_clase.validate():
    #     nom = alumno_clase.nombre.data
    #     apa = alumno_clase.apaterno.data
    #     ama = alumno_clase.amaterno.data
    #     email = alumno_clase.email.data
    #     edad = alumno_clase.edad.data

    #     print('Nombre: {}'.format(nom))
    #     print('apaterno: {}'.format(apa))
    #     print('amaterno: {}'.format(ama))
    #     print('edad: {}'.format(edad))
    #     print('email: {}'.format(email))
    #     ##Mensajes de respuesta de la aplicación
    #     mensaje='Bienvenido {}'.format(nom)
    #     flash(mensaje)
    # ## return render_template("alumnos.html")
    # return render_template("alumnos.html", form=alumno_clase,nom=nom,apa=apa,ama=ama,email=email)

@app.route("/indexr", methods=['GET','POST'])
def indexr():

    return render_template("index.html")


@app.route('/index', methods=['GET','POST'])
def index():
    create_form=forms.UserForm(request.form)
    if request.method=='POST':
        alum=Alumnos(nombre=create_form.nombre.data,
                     apaterno=create_form.nombre.data,
                     email=create_form.nombre.data)
        db.session.add(alum)
        db.session.commit()
    return render_template('index.html',form=create_form)
# @app.route("/maestros", methods=['GET','POST'])
# def distancia():
  
#     "Hola desde FLASK"
#     return "Hola desde FLASK"
@app.route("/ABC_Completo", methods=["GET","POST"])
def ABCompleto():
    alum_form=forms.UserForm(request.form)
    alumno=Alumnos.query.all()
    
    return render_template("ABC_Completo.html",alumno=alumno)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.run(debug=True)

