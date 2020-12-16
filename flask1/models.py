from flask1 import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader  # try without "()"
def load_user(user_id):
    return Doctor.query.get(int(user_id))


class Doctor(db.Model, UserMixin):
    __tablename__ = 'doctor'
    doctor_id = db.Column('doctor_id', db.Integer, primary_key=True)
    doctor_name = db.Column('doctor_name', db.String(100))
    email = db.Column('email', db.String(100))
    phone = db.Column('phone', db.String(15))
    doctor_usr = db.Column('doctor_usr', db.String(20))
    doctor_pass = db.Column('doctor_pass', db.String(100))

    def __repr__(self):
        return f"Doctor('{self.doctor_id}', '{self.doctor_name}', '{self.doctor_usr}', '{self.doctor_pass}')"

    def get_id(self):
        return self.doctor_id


class Patient(db.Model):
    __tablename__ = 'patient'
    patient_id = db.Column('patient_id', db.Integer, primary_key=True)
    patient_name = db.Column('patient_name', db.String(100))
    doctor_id = db.Column('doctor_id', db.Integer)
    email = db.Column('email', db.String(100))
    phone = db.Column('phone', db.String(15))
    patient_usr = db.Column('patient_usr', db.String(20))
    patient_pass = db.Column('patient_pass', db.String(100))
    is_recording = db.Column('is_recording', db.Boolean)

    def __repr__(self):
        return f"Patient('{self.patient_name}', '{self.patient_usr}', '{self.doctor_id}')"


class SummaryRec(db.Model):
    __tablename__ = 'summaryrec'
    id = db.Column('id', db.Integer, primary_key=True)
    patient_id = db.Column('patient_id', db.Integer)
    n_rec = db.Column('n_rec', db.Integer)
    latest_time = db.Column('latest_time', db.DateTime)
    is_active = db.Column('is_active', db.Boolean)


class Rec001(db.Model):
    __tablename__ = 'rec001'
    record_id = db.Column('record_id', db.Integer, primary_key=True)
    patient_id = db.Column('patient_id', db.Integer)
    upload_time = db.Column('upload_time', db.DateTime)
    record_file = db.Column('record_file', db.String(100))
    HR = db.Column('hr', db.Integer)
    n_rec = db.Column('n_rec', db.Integer)

    def __repr__(self):
        return f"Raw file('{self.record_id}', '{self.patient_id}', '{self.upload_time}')"
