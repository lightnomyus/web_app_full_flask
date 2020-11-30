from flask import render_template, flash, redirect, url_for, request
from flask1 import app, db, bcrypt
from flask1.simple_forms import RegistrationForm, LoginForm
from flask1.models import Doctor, Patient, Rec001, load_user
from flask_login import login_user, current_user, logout_user, login_required
from flask1.plot_ecg import load_from_file


# @app.route('/', endpoint='home_page')
@app.route('/home', endpoint='home_page')
def home_page():
    if current_user.is_authenticated and current_user is not None:
        print(current_user)
        patient_list = Patient.query.filter_by(doctor_id=current_user.id).all()
    else:
        print("Not authenticated")
    return render_template('index.html', acc=current_user, var_patient=patient_list)
    # trial with dummy variables from posts


@app.route('/about', endpoint='about_page')
def about_page():
    return render_template('anu.html', title='About')


@app.route('/register', methods=['GET', 'POST'], endpoint='register_page')
def register_page():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = RegistrationForm()
    if form.validate_on_submit():
        pass_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        temp_doctor = Doctor(username=form.username.data, email=form.email.data, password=pass_hash)
        db.session.add(temp_doctor)
        db.session.commit()
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('login_page'))
    return render_template('register_form.html', title='Register', form=form)


@app.route('/', methods=['GET', 'POST'], endpoint='login_page')
@app.route('/login', methods=['GET', 'POST'], endpoint='login_page')
def login_page():
    if current_user is not None and current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Doctor.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_pass.data)
            next_page = request.args.get('next')  # set next page
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home_page'))
        else:
            flash('Login Unsuccessful. Check username and password!', 'danger')
    return render_template('login_form.html', title='Login', form=form)


@app.route('/logout', endpoint='logout_page')
def logout_page():
    logout_user()
    flash(f'Logged Out successfully', 'success')
    return redirect(url_for('login_page'))


@app.route('/account', endpoint='account_page')
@login_required
def account_page():
    return render_template('account.html', title='Account')
    # image_file = url_for('static', filename = 'images/' + current_user.image_file)

# @app.route('/patient/<int:patient_id>', endpoint='patient_list_page')
# @login_required
# def patient_list_page(patient_id):


@app.route('/patient/<int:patient_id>', endpoint='patient_page')
@login_required
def patient_page(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    recording = Rec001.query.filter_by(patient_id=patient.id).all()
    return render_template('patient.html', title=patient.username, patient=patient, rec_list=recording)


@app.route('/ecg/<int:ecg_id>', endpoint='ecg_page')
@login_required
def ecg_page(ecg_id):
    ecg = Rec001.query.get_or_404(ecg_id)
    upload = ecg.date_uploaded
    file_in = 'flask1/' + ecg.record_file
    # time to plot ecg
    ch1, ch2, ch3, ppg = load_from_file(file_in)
    return render_template('view_ecg.html', title=ecg.id, val1=ch1, val2=ch2, val3=ch3, val4=ppg, updated=upload)
