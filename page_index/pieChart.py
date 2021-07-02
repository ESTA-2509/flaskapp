# library
import pandas as pd
import matplotlib.pyplot as plt
import os
import mysql.connector
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="demo"
)
mycursor = mydb.cursor()
sql="select count(appId) from `apps`"
mycursor.execute(sql)
All_apps = mycursor.fetchone()
All_apps_json = json.dumps(All_apps)
All_apps_json = All_apps_json.replace("[", "")
All_apps_json = All_apps_json.replace("]", "")

sql1="select count(appId) from `apps` WHERE `Free` = '1'"
mycursor.execute(sql1)
Free_Apps = mycursor.fetchone()
Free_apps_json = json.dumps(Free_Apps)
Free_apps_json = Free_apps_json.replace("[", "")
Free_apps_json = Free_apps_json.replace("]", "")
Paid_apps_json = str(int(All_apps_json) - int(Free_apps_json))
Free_apps_percent = int(Free_apps_json) / int(All_apps_json)
Paid_apps_percent = 1 - Free_apps_percent
labels = 'Trả Phí: ' + Paid_apps_json, 'Miễn Phí: '+ Free_apps_json

sizes = [Paid_apps_percent, Free_apps_percent]
colors = ( "orange", "cyan") 
fig1, ax_1 = plt.subplots()
explode = (0, 0) 
ax_1.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%', shadow=True, startangle=90)
patches, texts, auto = ax_1.pie(sizes, colors=colors, shadow=True, startangle=90,explode=explode, autopct='%1.1f%%' )
# file name   
file_name_1 = 'pie_Chart.png'
# change the current working
# directory
my_path_1 = os.path.abspath(file_name_1)
if os.path.exists(file_name_1):
  os.remove(file_name_1)
plt.savefig(my_path_1, transparent=True)
plt.close('all')
