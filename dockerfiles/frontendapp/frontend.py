from flask import Flask 
from flask import jsonify
from flask import request
from flask_mysqldb import MySQL
import os
import json

app = Flask(__name__)

MYSQL_HOST=os.environ.get('MYSQL_HOST')
PASSWORD=os.environ.get('PASSWORD')
MYSQL_USER=os.environ.get('MYSQL_USER')
MYSQL_DATABASE=os.environ.get('MYSQL_DATABASE')




app.config['MYSQL_HOST'] =MYSQL_HOST
app.config['MYSQL_USER'] =MYSQL_USER
app.config['MYSQL_PASSWORD'] =PASSWORD
app.config['MYSQL_DB'] = MYSQL_DATABASE


 
mysql = MySQL(app)


@app.route('/')
def hello_world():

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT title FROM data')
    results=cursor.fetchone()
    
    y = json.dumps(results)
    res = str(y)[1:-1]
    output=res.strip( '."')
    return (output)


