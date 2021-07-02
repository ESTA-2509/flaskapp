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
results_1 = []
sql="select count(*) from `apps`"
mycursor.execute(sql)
All_apps = mycursor.fetchone()
All_apps_json = json.dumps(All_apps)
All_apps_json = All_apps_json.replace("[", "")
All_apps_json = All_apps_json.replace("]", "")
All_apps_json = int(All_apps_json)

sql="select count(*) from `apps` WHERE `score` <= 1.0"
mycursor.execute(sql)
Rating_apps_json = mycursor.fetchone()
Rating_1 = json.dumps(Rating_apps_json)
Rating_1 = Rating_1.replace("[", "")
Rating_1 = Rating_1.replace("]", "")
Rating_1=int(Rating_1)
results_1.append(int(Rating_1))

sql="select count(*) from `apps` WHERE `score` <= 2.0 AND `score` > 1.0 "
mycursor.execute(sql)
Rating_apps_json = mycursor.fetchone()
Rating_1 = json.dumps(Rating_apps_json)
Rating_1 = Rating_1.replace("[", "")
Rating_1 = Rating_1.replace("]", "")
Rating_1=int(Rating_1)
results_1.append(int(Rating_1))

sql="select count(*) from `apps` WHERE `score` <= 3.0 AND `score` > 2.0"
mycursor.execute(sql)
Rating_apps_json = mycursor.fetchone()
Rating_1 = json.dumps(Rating_apps_json)
Rating_1 = Rating_1.replace("[", "")
Rating_1 = Rating_1.replace("]", "")
Rating_1=int(Rating_1)
results_1.append(int(Rating_1))

sql="select count(*) from `apps` WHERE `score` <= 4.0 AND `score` > 3.0"
mycursor.execute(sql)
Rating_apps_json = mycursor.fetchone()
Rating_1 = json.dumps(Rating_apps_json)
Rating_1 = Rating_1.replace("[", "")
Rating_1 = Rating_1.replace("]", "")
Rating_1=int(Rating_1)
results_1.append(int(Rating_1))

sql="select count(*) from `apps` WHERE `score` <= 5.0 AND `score` > 4.0"
mycursor.execute(sql)
Rating_apps_json = mycursor.fetchone()
Rating_1 = json.dumps(Rating_apps_json)
Rating_1 = Rating_1.replace("[", "")
Rating_1 = Rating_1.replace("]", "")
Rating_1=int(Rating_1)
results_1.append(int(Rating_1))


# creating the dataset
data = {'<=1.0':results_1[0], '1.0 - 2.0':results_1[1], '2.0 - 3.0':results_1[2],
        '3.0 - 4.0':results_1[3],'4.0 - 5.0':results_1[4]}
courses = list(data.keys())
values = list(data.values())
  
fig, ax = plt.subplots(figsize =(10, 6))
 
# creating the bar plot
rects1 = plt.bar(courses, values, color ='ORANGE', width = 0.4)
ax.bar_label(rects1, padding=3)
plt.xlabel("ĐIỂM ĐÁNH GIÁ")
plt.ylabel("SỐ LƯỢNG ỨNG DỤNG")
file_name_5 = 'RATING_APPS_1.png'
# change the current working
# directory
my_path_5 = os.path.abspath(file_name_5)
if os.path.exists(my_path_5):
  os.remove(my_path_5)
plt.savefig(my_path_5, transparent=True)
plt.close('all')