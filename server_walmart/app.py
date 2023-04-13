# import all necessary  commands for flask
from flask import Flask
from flask_cors import CORS
from db import db
from visitorslog import visitorlog_blueprint
from dashboard import dashboard_blueprint
# connecting with CORP
app = Flask(__name__)
CORS(app)

# Database Configuration
username = 'root'
password = ''
userpass ='mysql+pymysql://' + username + ':'+password +'@'
server ='127.0.0.1' #reserved ip address of mysql
dbname = '/walmart'

# configuration of app file
app.config['SQLALCHEMY_DATABASE_URI']=userpass+server+dbname  
# log all details of database 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True

# intialize the app file
db.init_app(app)

# register the blueprint
app.register_blueprint(visitorlog_blueprint) 
app.register_blueprint(dashboard_blueprint) 

# route to app
@app.route('/')
def hello_world():
    return 'hello world'

if __name__=='__main__':
    app.debug = True
    app.run()