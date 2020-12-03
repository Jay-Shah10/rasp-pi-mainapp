from app import app
from flask import render_template, redirect, url_for, request
import requests

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/zodiacapp")
def zodiacapp():
    try:
        # error code 302 will mean success for this connection.
        return redirect('http://192.168.50.92:5001', code=302)
    except Exception as e:
        return e

@app.route('/carlist')
def carlist():
    try:
       return redirect('http://192.168.50.92:5002/carlist', code=302)
    except Exception as e:
        return e


@app.route('/sensor')
def sensor():
   try:
       return redirect('http://192.168.50.92:5000', code=302)
   except Exception as e:
       return e