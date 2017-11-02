import sys, os
sys.path.append(os.getcwd())

from flask import Flask, render_template, redirect, session, request
from models.fact_model import FactModel
from models.base_model import DBSingelton

app = Flask(__name__)

@app.before_first_request
def initialize_tables():
	connect_db()
	if not FactModel.table_exists():
		FactModel.create_table()
	disconnect_db()

@app.before_request
def connect_db():
	DBSingelton.getInstance().connect()

@app.teardown_request
def disconnect_db(err=None):
	DBSingelton.getInstance().close()

app.secret_key = os.environ.get("FLASK_SECRET_KEY")
