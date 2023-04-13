from flask import Blueprint,request
from sqlalchemy.sql import text
from db import db
import datetime

visitorlog_blueprint = Blueprint('visitorlog_blueprint', __name__)
@visitorlog_blueprint.route('/add-visitors',methods=['POST']) #api
def addVisitors():
    gender=request.form['gender']
    age_group=request.form['age']
    comments=request.form['comments']
    currentDate=datetime.datetime.today().strftime('%Y-%m-%d')

    sql=text('INSERT INTO visitors_log(gender,age,comments,date) VALUES ('+gender+','+age_group+',"'+comments+'","'+currentDate+'")')
    db.engine.execute(sql)
    return 'data logged successfully'
