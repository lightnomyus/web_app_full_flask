from flask import render_template, flash, redirect, url_for, request
from flask1 import app, db, bcrypt
from flask1.simple_forms import RegistrationForm, LoginForm
from flask1.models import Doctor, Patient, Rec001
from flask_login import login_user, current_user, logout_user, login_required

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


@app.route('/login', methods=['GET', 'POST'], endpoint='login_page')
def login_page():
    if current_user.is_authenticated:
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
    return redirect(url_for('home_page'))


@app.route('/account', endpoint='account_page')
@login_required
def account_page():
    return render_template('account.html', title='Account')
