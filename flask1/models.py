from flask1 import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader  # try without "()"
def load_user(user_id):
    return Doctor.query.get(int(user_id))


class Doctor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    # image_file = db.Column(db.String(20), nullable=False, default='default_doc.jpg')
    password = db.Column(db.String(60), nullable=False)
    patient_lists = db.relationship('Patient', backref='doctor_name', lazy=True)

    def __repr__(self):
        return f"Doctor('{self.username}', '{self.email}')"


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    # image_file = db.Column(db.String(20), nullable=False, default='default_patient.jpg')
    password = db.Column(db.String(60), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    record_lists = db.relationship('Rec001', backref='patient_name', lazy=True)

    def __repr__(self):
        return f"Patient('{self.username}', '{self.email}', '{self.doctor_id}')"


class Rec001(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    date_uploaded = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # or try utcnow()
    record_file = db.Column(db.String(20), nullable=False, default='Dummy_400sps_10min.csv')

    def __repr__(self):
        return f"Raw file('{self.id}', '{self.patient_id}', '{self.date_uploaded}')"
