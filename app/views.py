from app import app
from flask import render_template, redirect, url_for, request
import requests

@app.route("/")
def index():
    return render_template('index.html')

# @app.route("/zodiacapp")
# def zodiacapp():
#     try:
#         return redirect(url_for('192.168.50.92:5001/'))
#     except Exception:
#         return Exception
