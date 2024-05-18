from flask_login import UserMixin
from app.extensions import db
from enum import Enum
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = "Users"
    Attrs = ['username', 'name', 'surname', 'email', 'role']

    # password is hash for "84Alptug"
    default_password = "65bfde124fdff1b62ab3220f46d8ec9e02e4005b6731e174e67fee558ea09b78"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # attributes
    username = db.Column(db.Text, nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text)
    surname = db.Column(db.Text)
    email = db.Column(db.Text, nullable=True, unique=True)
    role = db.Column(db.Text, nullable=False, default='[99]')

    # settings
    lang = db.Column(db.Text, default="en_US")

    # dates
    createdat = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updatedat = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    deletedat = db.Column(db.DateTime)

    def __init__(self, userinfo, password_hash=default_password):
        for attr in self.Attrs:
            if attr in userinfo:
                setattr(self, attr, userinfo[attr])
        self.password_hash = password_hash

    def __repr__(self):
        return f"<User: username={self.username}, role={self.role}>"

    class Role(Enum):
        # NONE = 0
        ADMIN = 1
        DEVELOPER = 2
        TESTER = 3
        MAINTAINER = 4
        SUPERVISOR = 5
        MUSTERITEMSIL = 6
        KALIP = 7
        KUMASALMA = 8
        AKSESUARALMA = 9
        FASONTAKIP = 10
        IHRACAT = 11
        SEVKIYAT = 12
        PLANLAMA = 13
        MALIYET = 14
        MUHASEBE = 15
        INSANKAYNAK = 16
        NUMUNETAKIP = 17
        SURDURULEBILIRLIK = 18
        YONETIM = 19
        # SYSTEM = 98
        DUMMY = 99
