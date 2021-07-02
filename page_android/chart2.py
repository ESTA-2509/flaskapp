from flask import Flask, Markup, render_template
app = Flask(__name__)
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
import json, os
import collections
from array import *
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="demo"
)
mycursor = mydb.cursor()
sql="SELECT `androidVersion`, COUNT(`appId`) as Num_of_apps FROM `apps` GROUP BY `androidVersion` ORDER BY COUNT(`appId`) DESC"
mycursor.execute(sql)
categories = mycursor.fetchall()

# Convert query to objects of key-value pairs

objects_list= {}
objects_list['data']=[]
for row in categories:
    d = collections.OrderedDict()
    d["androidVersion"] = row[0]
    d["Num_of_apps"] = row[1]
    objects_list['data'].append(d)
    j = json.dumps(objects_list)
file_name_11 = 'android_os_details.json'
# change the current working
# directory
my_path_11 = os.path.abspath(file_name_11)
with open(my_path_11, 'w') as f:
  f.write(j)
f.close()
