from flask import render_template, flash, redirect, url_for, request, session
from flask1 import app, db, bcrypt
from flask1.simple_forms import LoginForm
from flask1.models import Doctor, Patient, Rec001, SummaryRec
from flask_login import login_user, current_user, logout_user, login_required
from flask1.plot_ecg import load_from_file
from sqlalchemy import and_, desc
from azure.storage.blob import BlobServiceClient


# @app.route('/', endpoint='home_page')
@app.route('/home', endpoint='home_page')
def home_page():
    if current_user.is_authenticated and current_user is not None:
        # print(current_user)
        session["selected_doctor_name"] = current_user.doctor_name
        patient_list = Patient.query.filter_by(doctor_id=current_user.doctor_id).all()
    else:
        print("Not authenticated")

    if "selected_patient_name" in session:
        session.pop("selected_patient_name", None)
    if "selected_patient_id" in session:
        session.pop("selected_patient_id", None)
    return render_template('index.html', acc=current_user, var_patient=patient_list)


@app.route('/about', endpoint='about_page')
def about_page():
    return render_template('anu.html', title='About')


@app.route('/', methods=['GET', 'POST'], endpoint='login_page')
@app.route('/login', methods=['GET', 'POST'], endpoint='login_page')
def login_page():
    if current_user is not None and current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Doctor.query.filter_by(doctor_usr=form.username.data).first()
        if user and bcrypt.check_password_hash(user.doctor_pass, form.password.data):
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


@app.route('/patient/<int:selected_id>', endpoint='patient_page')
@login_required
def patient_page(selected_id):
    patient = Patient.query.get_or_404(selected_id)
    recording = SummaryRec.query.filter_by(patient_id=selected_id).order_by(SummaryRec.id.desc())
    session["selected_patient_name"] = patient.patient_name
    session["selected_patient_id"] = patient.patient_id
    return render_template('patient.html', title='patient', patient=patient, summary_rec_list=recording)


@app.route('/detail/<int:active_patient_id>/<int:active_rec>', endpoint='detail_page')
@login_required
def detail_page(active_patient_id, active_rec):
    rec_session = Rec001.query.filter(and_(Rec001.patient_id == active_patient_id, Rec001.n_rec == active_rec)).all()

    # parsing data fro HR summary
    plot_legend = 'HR'
    plot1 = []
    times = []
    for i in rec_session:
        # data1 = int(i.HR)
        # t1 = i.upload_time
        plot1.append(int(i.HR))
        times.append(i.upload_time)

    if "selected_patient_name" in session:
        local_name = session["selected_patient_name"]
    if "selected_patient_id" in session:
        local_id = session["selected_patient_id"]
    if "selected_doctor_name" in session:
        local_doc = session["selected_doctor_name"]
    session["selected_n_rec"] = active_rec
    return render_template('detail.html', title='detail', rec_list=rec_session, p_name=local_name, p_id=local_id,
                           d_name=local_doc, values=plot1, labels=times, legend=plot_legend)


@app.route('/ecg/<int:ecg_id>', endpoint='ecg_page')
@login_required
def ecg_page(ecg_id):
    # session
    if "selected_patient_name" in session:
        local_name = session["selected_patient_name"]
    if "selected_patient_id" in session:
        local_id = session["selected_patient_id"]
    if "selected_doctor_name" in session:
        local_doc = session["selected_doctor_name"]
    if "selected_n_rec" in session:
        local_n_rec = session["selected_n_rec"]
    rec_session = Rec001.query.filter(and_(Rec001.patient_id == local_id, Rec001.n_rec == local_n_rec)).order_by(Rec001.record_id.desc())

    ecg = Rec001.query.get_or_404(ecg_id)
    id_now = ecg.record_id
    id_n_m = ecg.record_id
    id_n_h = ecg.record_id
    id_n_d = ecg.record_id

    id_p_m = ecg.record_id
    id_p_h = ecg.record_id
    id_p_d = ecg.record_id
    upload = ecg.upload_time
    id_hr = ecg.HR

    # previous minute
    for i in rec_session:
        temp_sel = i.upload_time - upload
        secs = temp_sel.total_seconds()
        if -60 >= secs > -120:
            id_p_m = i.record_id
            break

    # previous hour
    for i in rec_session:
        temp_sel = i.upload_time - upload
        secs = temp_sel.total_seconds()
        if -3600 >= secs > -3660:
            id_p_h = i.record_id
            break

    # previous day
    for i in rec_session:
        temp_sel = i.upload_time - upload
        secs = temp_sel.total_seconds()
        if -86400 >= secs > -86460:
            id_p_d = i.record_id
            break

    # next minute
    for i in rec_session:
        temp_sel = i.upload_time - upload
        secs = temp_sel.total_seconds()
        if secs >= 60:
            id_n_m = i.record_id

    # next hour
    for i in rec_session:
        temp_sel = i.upload_time - upload
        secs = temp_sel.total_seconds()
        if secs >= 3600:
            id_n_h = i.record_id

    # next day
    for i in rec_session:
        temp_sel = i.upload_time - upload
        secs = temp_sel.total_seconds()
        if secs >= 86400:
            id_n_d = i.record_id

    azure_credential = "yrAk6GS3kpefZYdNEDyQtuFep5cBp5OvM2INpvedAe2o6d5ifBhcbGNmT1yGExg9oqCZnu40hQse1RxE4MzAXQ=="
    blob_name = ecg.record_file
    blob_service_client = BlobServiceClient(account_url="https://lightnomyusblob1.blob.core.windows.net",
                                            credential=azure_credential)
    blob_client = blob_service_client.get_blob_client(container='lightcontainer1', blob=blob_name)

    # method1
    with open('flask1/temp1.csv', 'wb') as f:
        b = blob_client.download_blob()
        b.readinto(f)
    # time to plot ecg
    ch1, ch2, ch3, ppg = load_from_file('flask1/temp1.csv')
    return render_template('view_ecg.html', title='view-ecg', val1=ch1, val2=ch2, val3=ch3, val4=ppg, hr=id_hr,
                           p_name=local_name, p_id=local_id, d_name=local_doc, updated=upload, next_min=id_n_m,
                           prev_min=id_p_m, next_hour=id_n_h, prev_hour=id_p_h, next_day=id_n_d, prev_day=id_p_d)
