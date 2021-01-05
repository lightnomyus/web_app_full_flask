from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# from flask_bootstrap import Bootstrap

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates', )

# bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '65f295c5f593a281ba036c81a4ee5212'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql://lightnomyus:L1ghtn0myu5@holterserver1.database.windows.net:1433/holter_database1?driver=SQL+Server'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://lightnomyus@lightnomyus1998:L1ghtn0myu5@lightnomyus1998.postgres.database.azure.com:5432/postgres'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'
# login_manager.init_app(app)  # new
# new

from flask1 import routes
