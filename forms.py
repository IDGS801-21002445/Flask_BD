#from wtforms import Form
from wtforms import Form
from wtforms import Form
#from wtforms import StringField, TelField, IntegerField
from wtforms import StringField,TelField,IntegerField
#from wtforms import EmailField
from wtforms import StringField,TelField,IntegerField
#from wtforms.validators import DataRequired, Email
from wtforms.validators import DataRequired,Email
from wtforms import Form
from wtforms import SelectField, RadioField
from wtforms import validators


#Sin validaciones
# class UserForm(Form):
#     nombre = StringField('nombre')
#     email = StringField("email")
#     apaterno = TelField("apaterno")
#     amaterno = StringField('amamterno')
#     edad = IntegerField('edad') 

#Con Validaciones  
class UserForm(Form):
    id=IntegerField('id',[validators.number_range(min=1,max=20,message='Id inválido')])
    nombre = StringField('nombre',[validators.DataRequired(message='El campo es requerido'),
                                    validators.length(min=4,max=10,message='Ingresa un nombre válido')])
    
    email = StringField("email",[validators.Email(message='Ingresa un email válido')])

    apaterno = TelField("apaterno",[validators.DataRequired(message='El campo es requerido'),
                                    validators.length(min=4,max=10,message='Ingresa un apellido válido')])
    
    amaterno = StringField('amamterno',[validators.DataRequired(message='El campo es requerido'),
                                    validators.length(min=4,max=10,message='Ingresa un apellido válido')])
    
    edad = IntegerField('edad',[validators.DataRequired(message='El campo es requerido'),
                                    validators.length(min=4,max=10,message='Ingresa un edad válido')]) 
    
class distanciasForm(Form):
    x1 = IntegerField("x1")
    x2 = IntegerField("x2")
    y1 = IntegerField("y1")
    y2 = IntegerField('y2')
    d = IntegerField('d')