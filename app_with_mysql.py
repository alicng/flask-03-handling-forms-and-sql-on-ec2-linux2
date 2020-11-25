from flask import Flask
from flaskext.mysql import MySQL
app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST']='call-mysql-db-server.cbanmzptkrzf.us-east-1.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER']='admin'
app.config['MYSQL_DATABASE_PASSWORD']='Clarusway_1'
app.config['MYSQL_DATABASE_DB']='clarusway'
app.config['MYSQL_DATABASE_PORT']=3306
mysql = MySQL()
mysql.init_app(app)
connection = mysql.connect()
connection.autocommit(True)
cursor=connection.cursor()