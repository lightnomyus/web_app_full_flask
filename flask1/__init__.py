from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates', )

app.config['SECRET_KEY'] = '65f295c5f593a281ba036c81a4ee5212'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from flask1 import routes