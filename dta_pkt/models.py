from flask_login import UserMixin

from dta_pkt import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    #passwords are 20 char max but then we hash it so it gets pretty long hence the 80 max limit
    password = db.Column(db.String(80), nullable=False)
    #llamo a al conjunto de momentos para un usuario su horario
    horario = db.relationship('Moment', backref='usuario', lazy=True)

    def __repr__(self):
        return f"Usuario: {self.username}"

class Moment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #dias de la semana representados como 0 - 6
    dia = db.Column(db.Integer, nullable = False)
    hora = db.Column(db.Integer)
    act = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    def __repr__(self):
        return f"{self.dia} a las {self.hora} deberia estar {self.act}"
