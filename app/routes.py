from app import app
from flask import render_template, request
from app.models import model, formopener



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/dataEntry', methods= ['GET','POST'])
def dataEntry():
    userdata = request.form
    xName = userdata["X-axis"]
    yName = userdata["Y-axis"]
    print(userdata)
    return render_template('dataEntry.html', xName = xName, yName = yName)