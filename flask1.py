from flask import Flask, render_template, flash, redirect, url_for
from simple_forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates', )

app.config['SECRET_KEY'] = '65f295c5f593a281ba036c81a4ee5212'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


class Doctor(db.Model):
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


posts = [
    {
        'name': 'Mohammed Avdol',
        'age': 33,
        'description': 'Yes, I AM!'
    },
    {
        'name': 'Joseph Joestar',
        'age': 64,
        'description': 'OH MY GOD'
    },
    {
        'name': 'Giorno Giovana',
        'age': 15,
        'description': 'Kono Giorno Giovana ha, Yume ga aru'
    }
]


@app.route('/', endpoint='home_page')
@app.route('/home', endpoint='home_page')
def home_page():
    return render_template('index.html', var_post=posts)


@app.route('/second', endpoint='second_page')
def second_page():
    return render_template('second.html')


@app.route('/about', endpoint='about_page')
def about_page():
    return render_template('anu.html', title='Anu')


@app.route('/register', methods=['GET', 'POST'], endpoint='register_page')
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        pass_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        temp_doctor = Doctor(username=form.username.data, email=form.email.data, password=pass_hash)
        db.session.add(temp_doctor)
        db.session.commit()
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('login_page'))
    return render_template('register_form.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'], endpoint='login_page')
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'lightnomyus' and form.password.data == 'password':
            flash('Logged In Successfully', 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Login Unsuccessful. Check username and password!', 'danger')
    return render_template('login_form.html', title='Login', form=form)


if __name__ == '__main__':
    app.run()
