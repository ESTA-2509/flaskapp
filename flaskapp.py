from flask import render_template,Flask, json,request, jsonify, current_app as app
app = Flask(__name__)
import numpy as np
import matplotlib.pyplot as plt
import os
import mysql.connector
import json
import collections
from run import *
print("step2")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="demo"
)
mycursor = mydb.cursor()
sql="select Average_Rating_apps from `result` GROUP BY Date DESC LIMIT 1"
mycursor.execute(sql)
Average_Rating_apps_json = mycursor.fetchone()
Average_Rating_apps = json.dumps(Average_Rating_apps_json)
Average_Rating_apps = Average_Rating_apps.replace("[", "")
Average_Rating_apps = Average_Rating_apps.replace("]", "")
Average_Rating_apps = float(Average_Rating_apps)
#xu ly khi ban vao host 127.0.0.1:5000
app = Flask(__name__, static_url_path='/static/')
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route('/')
def index ():
    to_send=str(Average_Rating_apps)
    to_send1=str(int(Average_Rating_apps*20))+"%"
    return render_template('index.html',Average_Rating=to_send, percent_rating=to_send1) #se hien ra giao dien la file index.html

@app.route('/freevspaid', methods=['GET', 'POST'])
def freevspaid ():
    # show the form, it wasn't submitted
    return render_template('freevspaid.html')

@app.route('/rating', methods=['GET', 'POST'])
def rating ():
    # show the form, it wasn't submitted
    return render_template('rating.html')

@app.route('/categories', methods=['GET', 'POST'])
def categories ():
    # show the form, it wasn't submitted
    return render_template('cate_page.html')   
@app.route('/search_page', methods=['GET', 'POST'])
def search_page ():
    # show the form, it wasn't submitted
    return render_template('search_page.html')
@app.route('/app_detail', methods=['GET', 'POST'])
def app_detail ():
    # show the form, it wasn't submitted
    return render_template('app_detail.html') 
@app.route('/index_get_data')
def stuff():
  # Assume data comes from somewhere else
    filename = os.path.join(app.static_folder, 'chart/cate_details.json')
    with open(filename) as blog_file:
        data = json.load(blog_file)
    return jsonify(data)

@app.route('/index_get_data_android')
def stuff2():
  # Assume data comes from somewhere else
    filename = os.path.join(app.static_folder, 'chart/android_os_details.json')
    with open(filename) as blog_file:
        data = json.load(blog_file)
    return jsonify(data)
@app.route("/test",methods=["GET","POST"])
def test():
    return render_template('test.html')

@app.route("/android_os",methods=["GET","POST"])
def android_os():
    return render_template('android_os.html')
@app.route("/searchdata",methods=["GET","POST"])
def searchdata():
    search_word = request.form['search_word']
    print(search_word)
    query_1 = "SELECT `icon`, `title`,`developer`,`score`*20 as `score%`, `installs`, `url`, `headerImage`, `appId` FROM `apps` WHERE `title` LIKE '%{}%' ORDER BY `minInstalls` DESC".format(search_word)
    mycursor.execute(query_1)
    programming = mycursor.fetchall()
    return jsonify({'data': render_template('response.html', searchdata=programming)})

@app.route("/searchdata_1",methods=["GET","POST"])
def searchdata_1():
    appId = request.form['appId']
    print(appId)
    query = "SELECT *, `score`*20 as `score%` FROM `apps` WHERE `appId` LIKE '%{}%'".format(appId)
    mycursor.execute(query)
    programming_1 = mycursor.fetchall()
    return jsonify({'data': render_template('response_1.html', programming=programming_1)})

if __name__ == "__main__":
    app.run(debug=True, port=8000)