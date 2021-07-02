import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
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

sql="UPDATE `apps` SET `androidVersion` = REPLACE(`androidVersion`, '4.4W', '4.4')"
mycursor.execute(sql)

string_year="year(DATE_FORMAT(STR_TO_DATE(`released`,'%M %d, %Y'), '%Y-%m-%d'))"
Year=[]
Apps=[]
Apps_4_0=[]
Apps_4_1=[]
Apps_5=[]
Apps_6=[]
Apps_7=[]
Apps_8=[]
for x in range(8):
  #Lấy dữ liệu tổng số ứng dụng và năm cách đây 11 năm
  k=x
  sql_1="SELECT COUNT(*) FROM `apps` WHERE " + string_year +" <= YEAR(CURDATE() - INTERVAL "+ str(k) +" YEAR) LIMIT 0,1"
  mycursor.execute(sql_1)
  All_apps_json = mycursor.fetchone()
  All_apps = json.dumps(All_apps_json)
  All_apps = All_apps.replace("[", "")
  All_apps = All_apps.replace("]", "")
  All_apps= int(All_apps)
  Apps.append(int(All_apps))

  sql_2="SELECT "+ string_year +" FROM `apps` WHERE " + string_year +" = YEAR(CURDATE() - INTERVAL "+ str(k) +" YEAR) LIMIT 0,1"
  mycursor.execute(sql_2)
  years_json = mycursor.fetchone()
  years = json.dumps(years_json)
  years = years.replace("[", "")
  years = years.replace("]", "")
  years=int(years)
  Year.append(int(years))

  sql_3="SELECT COUNT(*) FROM `apps` WHERE (`androidVersion` LIKE '1%' OR `androidVersion` LIKE '2%' OR `androidVersion` LIKE '3%') AND " + string_year +" <= YEAR(CURDATE() - INTERVAL "+ str(k) +" YEAR) LIMIT 0,1"
  mycursor.execute(sql_3)
  All_apps_4_0_json = mycursor.fetchone()
  All_apps_4_0 = json.dumps(All_apps_4_0_json)
  All_apps_4_0 = All_apps_4_0.replace("[", "")
  All_apps_4_0 = All_apps_4_0.replace("]", "")
  All_apps_4_0=((int(All_apps_4_0))/All_apps)*100
  Apps_4_0.append(float(All_apps_4_0))

  sql_4="SELECT COUNT(*) FROM `apps` WHERE (`androidVersion` LIKE '4%') AND " + string_year +" <= YEAR(CURDATE() - INTERVAL "+ str(k) +" YEAR) LIMIT 0,1"
  mycursor.execute(sql_4)
  All_apps_4_1_json = mycursor.fetchone()
  All_apps_4_1 = json.dumps(All_apps_4_1_json)
  All_apps_4_1 = All_apps_4_1.replace("[", "")
  All_apps_4_1 = All_apps_4_1.replace("]", "")
  All_apps_4_1=((int(All_apps_4_1))/All_apps)*100
  Apps_4_1.append(float(All_apps_4_1))

  sql_5="SELECT COUNT(*) FROM `apps` WHERE (`androidVersion` LIKE '5%') AND " + string_year +" <= YEAR(CURDATE() - INTERVAL "+ str(k) +" YEAR) LIMIT 0,1"
  mycursor.execute(sql_5)
  All_apps_5_json = mycursor.fetchone()
  All_apps_5 = json.dumps(All_apps_5_json)
  All_apps_5 = All_apps_5.replace("[", "")
  All_apps_5 = All_apps_5.replace("]", "")
  All_apps_5=((int(All_apps_5))/All_apps)*100
  Apps_5.append(float(All_apps_5))

  sql_6="SELECT COUNT(*) FROM `apps` WHERE (`androidVersion` LIKE '6%') AND " + string_year +" <= YEAR(CURDATE() - INTERVAL "+ str(k) +" YEAR) LIMIT 0,1"
  mycursor.execute(sql_6)
  All_apps_6_json = mycursor.fetchone()
  All_apps_6 = json.dumps(All_apps_6_json)
  All_apps_6 = All_apps_6.replace("[", "")
  All_apps_6 = All_apps_6.replace("]", "")
  All_apps_6=((int(All_apps_6))/All_apps)*100
  Apps_6.append(float(All_apps_6))

  sql_7="SELECT COUNT(*) FROM `apps` WHERE (`androidVersion` LIKE '7%') AND " + string_year +" <= YEAR(CURDATE() - INTERVAL "+ str(k) +" YEAR) LIMIT 0,1"
  mycursor.execute(sql_7)
  All_apps_7_json = mycursor.fetchone()
  All_apps_7 = json.dumps(All_apps_7_json)
  All_apps_7 = All_apps_7.replace("[", "")
  All_apps_7 = All_apps_7.replace("]", "")
  All_apps_7=((int(All_apps_7))/All_apps)*100
  Apps_7.append(float(All_apps_7))

  sql_8="SELECT COUNT(*) FROM `apps` WHERE (`androidVersion` LIKE '8%') AND " + string_year +" <= YEAR(CURDATE() - INTERVAL "+ str(k) +" YEAR) LIMIT 0,1"
  mycursor.execute(sql_8)
  All_apps_8_json = mycursor.fetchone()
  All_apps_8 = json.dumps(All_apps_8_json)
  All_apps_8 = All_apps_8.replace("[", "")
  All_apps_8 = All_apps_8.replace("]", "")
  All_apps_8=((int(All_apps_8))/All_apps)*100
  Apps_8.append(float(All_apps_8))

fig, ax = plt.subplots(figsize =(18, 9))

# plot lines
plt.plot(Year, Apps_4_0, label = "Android 1 ~ 3", marker='s')
plt.plot(Year, Apps_4_1, label = "Android 4.0 ~ 4.4", marker='h')
plt.plot(Year, Apps_5, label = "Android 5", marker='p')
plt.plot(Year, Apps_6, label = "Android 6", marker='D')
plt.plot(Year, Apps_7, label = "Android 7", marker='v')
plt.plot(Year, Apps_8, label = "Android 8", marker='o')
plt.legend()

file_name_9 = 'Line_Chart_Android_OS.png'
# change the current working
# directory
my_path_9 = os.path.abspath(file_name_9)
if os.path.exists(my_path_9):
  os.remove(my_path_9)
plt.savefig(my_path_9, transparent=True)
plt.close('all')
