from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates', )
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '65f295c5f593a281ba036c81a4ee5212'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql://lightnomyus:L1ghtn0myu5@holterserver1.database.windows.net/holter_database1?driver=ODBC Driver 17 for SQL Server'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'
login_manager.init_app(app)  # new
# new

from flask1 import routes