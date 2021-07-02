from flask import Flask, Markup, render_template
app = Flask(__name__)
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
import json
import os
import collections
import psycopg2
from array import *
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="demo"
)
mycursor = mydb.cursor()
sql="SELECT `genre`, COUNT(`appId`) as Num_of_apps FROM `apps` GROUP BY `genre` ORDER BY COUNT(`appId`) DESC"
mycursor.execute(sql)
categories = mycursor.fetchall()

# Convert query to objects of key-value pairs

objects_list= {}
objects_list['data']=[]
for row in categories:
    d = collections.OrderedDict()
    d["genre"] = row[0]
    d["Num_of_apps"] = row[1]
    objects_list['data'].append(d)
    j = json.dumps(objects_list)
file_name_10 = 'cate_details.json'
# change the current working
# directory
my_path_10 = os.path.abspath(file_name_10)
with open(my_path_10, 'w') as f:
  f.write(j)
f.close()
