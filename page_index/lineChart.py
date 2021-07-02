import numpy as np
import matplotlib.pyplot as plt
import os   
import mysql.connector
import json

from numpy.lib.arraypad import pad
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="demo"
)
mycursor = mydb.cursor()
sql="select count(appId) from `apps`"
mycursor.execute(sql)
All_apps_json = mycursor.fetchone()
All_apps= json.dumps(All_apps_json)
All_apps = All_apps.replace("[", "")
All_apps = All_apps.replace("]", "")

sql="select count(appId) from `apps` WHERE `released`IS NULL"
mycursor.execute(sql)
NULL_apps_json = mycursor.fetchone()
NULL_apps = json.dumps(NULL_apps_json)
NULL_apps = NULL_apps.replace("[", "")
NULL_apps = NULL_apps.replace("]", "")

string_year="year(DATE_FORMAT(STR_TO_DATE(`released`,'%M %d, %Y'), '%Y-%m-%d'))"
Year=[]
Apps=[]
for x in range(8):
  #Lấy dữ liệu tổng số ứng dụng và năm cách đây 11 năm
  k=x
  sql_6_1="SELECT COUNT(*) FROM `apps` WHERE " + string_year +" <= YEAR(CURDATE() - INTERVAL "+ str(k) +" YEAR)"
  mycursor.execute(sql_6_1)
  All_apps_6_json = mycursor.fetchone()
  All_apps_6 = json.dumps(All_apps_6_json)
  All_apps_6 = All_apps_6.replace("[", "")
  All_apps_6 = All_apps_6.replace("]", "")
  All_apps_6=int(All_apps_6)+int(NULL_apps)
  Apps.append(int(All_apps_6))

  sql_6_2="SELECT "+ string_year +" FROM `apps` WHERE " + string_year +" = YEAR(CURDATE() - INTERVAL "+ str(k) +" YEAR) LIMIT 0,1"
  mycursor.execute(sql_6_2)
  years_6_json = mycursor.fetchone()
  years_6 = json.dumps(years_6_json)
  years_6 = years_6.replace("[", "")
  years_6 = years_6.replace("]", "")
  years_6=int(years_6)
  Year.append(int(years_6))

fig, ax = plt.subplots(figsize =(18, 9))
plt.plot(Year, Apps, color='red', marker='o')
plt.title('Số lượng ứng dụng hiện tại: ' + All_apps, fontsize=16)
plt.xlabel('Năm', fontsize=14)
plt.ylabel('Số lượng ứng dụng', fontsize=14)
plt.grid(True,color='#ffcc29')
for x,y in zip(Year,Apps):
    label = "{:.0f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
# file name   
file_name = 'Line_Chart.png'
# change the current working
# directory
my_path = os.path.abspath(file_name)
if os.path.exists(file_name):
  os.remove(file_name)
plt.savefig(my_path, transparent=True)
plt.close('all')