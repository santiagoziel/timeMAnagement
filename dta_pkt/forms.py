from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

from dta_pkt.models import User

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min = 4, max = 20, message= "Nombre de usuario debe tener entre 4 y 20 caracteres")], render_kw={"placeholder":"Nombre de Usuario"})
    password = PasswordField(validators=[InputRequired(), Length(min = 4, message= "Contraseña debe tener entre 4 y 20 caracteres")], render_kw={"placeholder":"Contraseña"})
    submit = SubmitField("Registrar usuario")

    def validate_username(self,username):
        existing_user_name = User.query.filter_by(username = username.data).first()

        if existing_user_name:
            raise ValidationError("Ya existe un usuario con ese nombre, por favor elija otro")

class LogInForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min = 4, max = 20)], render_kw={"placeholder":"Nombre de Usuario"})
    password = PasswordField(validators=[InputRequired(), Length(min = 4, max = 20)], render_kw={"placeholder":"Contraseña"})
    submit = SubmitField("Ingresar")
