from flask import Flask
from .config import DevConfig,ProdConfig
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_migrate import Migrate

app = Flask(__name__)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


db = SQLAlchemy(app)
photos = UploadSet('photos',IMAGES)
mail = Mail(app)
Migrate(app,db)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']


# Creating the app configurations
app.config.from_object(ProdConfig)
# configure UploadSet
configure_uploads(app,photos)


from app import views
