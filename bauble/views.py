from flask import render_template, redirect, request, url_for
from app import app,db
from models import *

@app.route("/")
def intro():
    output="Bauble Default Page"
    return render_template('default.html', output=output)

@app.route("/generator/<int:id>")
def bauble(id):
    output ="This is where I'd display generator number {} for you".format(id) 
    return render_template('default.html', output=output)

