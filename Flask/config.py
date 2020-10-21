from flask import Flask, render_template, request, json, jsonify, session, redirect, url_for
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
mysql = MySQL()
app.secret_key = 'clef'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'JobBoardFlask'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
