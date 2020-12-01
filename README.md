# Web App TA

## 1. Tutorial to Set up and Developing with this Project

Prerequisites:
* Install [Python3](https://www.python.org/downloads/), and pip (don't use Conda, Conda sucks. Only use Conda if you're dealing with data visualization + machine learning in Windows)
* Text editor (Atom/Vscode/Sublime/Notepad++) or
* [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) (using Pycharm for Flask / Django project will make your life simpler and less stressful rather than using conventional text editor. Trust me)  :ok_hand:
* Install git

PS: for this project, I use Python 3.7.3. However, in the official Python3 website, the newest version is 3.9 which has big difference with 3.7. I recommend using Python 3.6 or 3.7 to prevent incompatibility issue with this specific project (yes, you can set different version of Python for different virtual environment. Just use 3.6 or 3.7 for the virtual environment for this project).

### 1.1 Clone This Repository

Go to cmd / terminal  / Git bash, then type

```
git clone https://github.com/lightnomyus/tugas_akhir_web_app.git
```

### 1.2 Create Python Virtual Environment

After success cloning the git, then go to the folder or type `cd tugas_akhir_web_app`. Then, open cmd / terminal inside `tugas_akhir_web_app` folder, and type

```
python -m venv <venv-name>
```

Replace `venv-name` with your own name. Now, let's assume that we name the folder `venv1`. Then, activate the virtual environment by this command:

```
venv1\scripts\activate
```

However, if you want to deactivate, type `venv1\scripts\deactivate`.

### 1.2.b With Pycharm

If you use Pycharm, you can skip step 1.2. Instead creating a virtual environment manually, just create a new project in Pycharm (better if you use the enterprise version, since you can choose new Flask project when creating a new project in Pycharm). Pycharm will automatically create a new virtual environment in a folder called `venv`. Then, open the Pycharm Terminal to activate and launch Python virtual environment automatically.

### 1.3 Install Required Packages

For this projects, there are several packages required. For that, use this pip command:

```
pip install -r requirements.txt
```

Or if you would like to install one by one to install the most updated version of each package, use these commands:

```
pip install Flask
pip install email_validator
pip install flask-wtf
pip install flask-sqlalchemy
pip install flask-bcrypt
pip install flask-login
pip install flask-bootstrap
pip install flask-admin
```
PS: `pip install flask` is required if you create your own virtual environment with step 1.2.a. However, if you use Pycharm and choose new Flask project, Pycharm will automatically install FLask package. Thus, no need to install again. After you install all these libraries above, you are ready to start developing and contributing for this project. 

### 1.4 How to Run Server

Run these commands:

```
1. set FLASK_APP=run.py
2. set FLASK_ENV=development
3. flask run
```

PS: `set FLASK_ENV=development` is used when we are in development stage (not deploying the final app). 

Alternatively, since I have wrapped this project into a package, you can just use `python run.py` instead of those 3 commands above. 

After `flask run` has finished, type in browser:

```
http://localhost:4888
```

This will redirect you into the sign in page of this project. To sign in, use any of the Doctor's account in Doctor table in Database (section 2.1 below)

The default configuration for the server is in `run.py` file:
```
app.run(host="localhost", port=4888, debug=True)
```

You can change the port number, or set `debug=False` if you want to deploy the app. However, since we are still in developing stage, I set `debug=True`.

### 1.5 How to Debug Error on Browser

If there is something wrong, usually error will appear in you browser. To debug, go to the specific line that causes error. In the leftmost side, there will be a small button. It is debug button. If you click that debug button, you will be asked a password. The password is available when you start server (if you set `Debug=True`, there will be a Debug PIN/Password available that is shown in your terminal when you run the server. Copy-paste that password). After that, you can type Python console command to check/verify if something is wrong.

## 2. Database Simulation Explanation

I have implemented database simulation with SQLAlchemy. The model for the database can be seen in `models.py` file.
There are 3 tables: Doctor, Patient, and Rec001. Doctor tables stores all info about Doctors. Each patient will have a foreign key referenced to doctor id. Then, each patient has a table to store all of his/her ECG recordings.

### 2.1 Doctor table

ID | Username | Email      | Password
------------ | ------------- | ------------- | ------------- 
1 | boike | boike@gmail.com | boike2 (hashed)
2 | giky | giky@gmail.com | ladygaga (hashed)
3 | gilgamesh | gilga@gmail.com | wakaka (hashed)

PS: all password are stored in hash format. Use `Bcrypt` library to decode the hashed password

### 2.2 Patient Table

ID | Username | Email      | Password | Doctor ID
------------ | ------------- | ------------- | ------------- | ------------- 
1 | danny | danny@gmail.com | danny1 (hashed) | 1
2 | mega | mega@gmail.com | megacantik (hashed) | 1
3 | violet | violet@gmail.com | major_gilbert (hashed) | 1
4 | amy | amy@gmail.com | violet (hashed) | 1
5 | hinata | uzumaki@gmail.com | raikage (hashed) | 1
6 | kaguya | kaguya_sama@gmail.com | miyuki (hashed) | 2
7 | tanjiro | kibutsuji_muzan@gmail.com | nezuko (hashed) | 2
8 | eren | eren_yaeger@gmail.com | historiamywife (hashed) | 1

PS: all patient passwords are hashed too. Doctor ID is the foreign key, reference to ID in Doctor table.

### 2.3 Rec001 Table

Basically, this table stores references to record files in storage.

ID | Patient ID | File
------------ | ------------- | -------------
1 | 1 | 'rawdata/m1.csv'
2 | 1 | 'rawdata/m2.csv'
3 | 1 | 'rawdata/m3.csv'
4 | 1 | 'rawdata/m4.csv'
5 | 1 | 'rawdata/m5.csv'
6 | 1 | 'rawdata/m6.csv'
7 | 1 | 'rawdata/m7.csv'
8 | 1 | 'rawdata/m8.csv'
9 | 1 | 'rawdata/m9.csv'
10 | 1 | 'rawdata/m10.csv'
11 | 1 | 'rawdata/m1.csv'
12 | 1 | 'rawdata/m2.csv'
13 | 1 | 'rawdata/m3.csv'
14 | 1 | 'rawdata/m4.csv'
15 | 1 | 'rawdata/m5.csv'
16 | 1 | 'rawdata/m6.csv'
17 | 1 | 'rawdata/m7.csv'
18 | 1 | 'rawdata/m8.csv'
19 | 1 | 'rawdata/m9.csv'
20 | 1 | 'rawdata/m10.csv'
21 | 1 | 'rawdata/m1.csv'
22 | 1 | 'rawdata/m2.csv'
23 | 1 | 'rawdata/m3.csv'
24 | 1 | 'rawdata/m4.csv'
25 | 1 | 'rawdata/m5.csv'
26 | 1 | 'rawdata/m6.csv'
27 | 1 | 'rawdata/m7.csv'
28 | 1 | 'rawdata/m8.csv'
29 | 1 | 'rawdata/m9.csv'
30 | 1 | 'rawdata/m10.csv'
31 | 1 | 'rawdata/m1.csv'
32 | 1 | 'rawdata/m2.csv'
33 | 1 | 'rawdata/m3.csv'
34 | 1 | 'rawdata/m4.csv'
35 | 1 | 'rawdata/m5.csv'
36 | 1 | 'rawdata/m6.csv'
37 | 1 | 'rawdata/m7.csv'
38 | 1 | 'rawdata/m8.csv'
39 | 1 | 'rawdata/m9.csv'
40 | 1 | 'rawdata/m10.csv'
41 | 1 | 'rawdata/m1.csv'
42 | 1 | 'rawdata/m2.csv'
43 | 1 | 'rawdata/m3.csv'
44 | 1 | 'rawdata/m4.csv'
45 | 1 | 'rawdata/m5.csv'
46 | 1 | 'rawdata/m6.csv'
47 | 1 | 'rawdata/m7.csv'
48 | 1 | 'rawdata/m8.csv'
49 | 1 | 'rawdata/m9.csv'
50 | 1 | 'rawdata/m10.csv'
51 | 1 | 'rawdata/m1.csv'
52 | 1 | 'rawdata/m2.csv'
53 | 1 | 'rawdata/m3.csv'
54 | 1 | 'rawdata/m4.csv'
55 | 1 | 'rawdata/m5.csv'
56 | 1 | 'rawdata/m6.csv'
57 | 1 | 'rawdata/m7.csv'
58 | 1 | 'rawdata/m8.csv'
59 | 1 | 'rawdata/m9.csv'
60 | 1 | 'rawdata/m10.csv'

PS: Patient ID is the foreign key, reference to ID in Patient table.

If there is any question, ask with the PIC for this web app development (a.k.a @lightnomyus). Enjoy you coding.
