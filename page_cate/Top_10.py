from flask import Flask, Markup, render_template

app = Flask(__name__)

import numpy as np
import matplotlib.pyplot as plt
import os
import mysql.connector
import json
from array import *
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="demo"
)
mycursor = mydb.cursor()
index=0
index_name=0
sql="SELECT COUNT(*) as count_cate FROM (SELECT COUNT(`appId`), `genre` FROM `apps` GROUP BY `genre` ORDER BY COUNT(`appId`)) count_cate"
mycursor.execute(sql)
count_cate = mycursor.fetchone()
count_cate = json.dumps(count_cate)
count_cate = count_cate.replace("[", "")
count_cate = count_cate.replace("]", "")
count_cate=int(count_cate)
index=int(index)
index_name=int(index_name)
Top=array('i',[])
Top_10=[]
Top_cate=[]
for k in range(0, count_cate, 1):
        sql="SELECT COUNT(`appId`) FROM `apps` GROUP BY `genre` ORDER BY COUNT(`appId`) DESC LIMIT " + str(index) + ", 1"
        mycursor.execute(sql)
        Apps_cate = mycursor.fetchone()
        Apps_cate = json.dumps(Apps_cate)
        Apps_cate = Apps_cate.replace("[", "")
        Apps_cate = Apps_cate.replace("]", "")
        Top.append(int(Apps_cate))
        sql_1="SELECT `genre` FROM `apps` GROUP BY `genre` ORDER BY COUNT(`appId`) DESC LIMIT " + str(index) + ", 1"
        mycursor.execute(sql_1)
        Name_Apps_cate = mycursor.fetchone()
        Name_Apps_cate = json.dumps(Name_Apps_cate)
        Name_Apps_cate = Name_Apps_cate.replace("[", "")
        Name_Apps_cate = Name_Apps_cate.replace("]", "")
        Name_Apps_cate =str(Name_Apps_cate)
        Top_cate.extend([Name_Apps_cate.strip('"')])
        index = index + 1

Top_10 = [Top[0], Top[1], Top[2], Top[3], Top[4], Top[5], Top[6], Top[7], Top[8], Top[9], Top[10]]
Top_10_cate = [Top_cate[0], Top_cate[1], Top_cate[2], Top_cate[3], Top_cate[4], Top_cate[5], Top_cate[6], Top_cate[7], Top_cate[8], Top_cate[9], Top_cate[10]]


x = np.arange(len(Top_10_cate))  # the label locations
width = 0.5  # the width of the bars
fig, ax = plt.subplots(figsize=(15,6))
rects1 = ax.bar(x, Top_10, width, label='Loại ứng dụng')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Số lượng ứng dụng')
ax.set_xticks(x)
ax.set_xticklabels(Top_10_cate)
ax.legend()
ax.bar_label(rects1, padding=3)
fig.tight_layout()
file_name_7 = 'Top_10.png'
my_path_7 = os.path.abspath(file_name_7)
if os.path.exists(my_path_7):
  os.remove(my_path_7)
plt.savefig(my_path_7, transparent=True)
plt.close('all')