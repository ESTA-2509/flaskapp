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
#Thống kê số lượng apps theo lượt tải
sql="select count(*) from `apps` WHERE (`minInstalls` <= 1000);"
mycursor.execute(sql)
All_apps_1_json = mycursor.fetchone()
All_apps_1 = json.dumps(All_apps_1_json)
All_apps_1 = All_apps_1.replace("[", "")
All_apps_1 = All_apps_1.replace("]", "")
All_apps_1=int(All_apps_1)

sql="select count(*) from `apps` WHERE (`minInstalls` <= 100000 AND `minInstalls` > 1000 );"
mycursor.execute(sql)
All_apps_2_json = mycursor.fetchone()
All_apps_2 = json.dumps(All_apps_2_json)
All_apps_2 = All_apps_2.replace("[", "")
All_apps_2 = All_apps_2.replace("]", "")
All_apps_2=int(All_apps_2)

sql="select count(*) from `apps` WHERE (`minInstalls` <= 1000000 AND `minInstalls` > 100000 );"
mycursor.execute(sql)
All_apps_3_json = mycursor.fetchone()
All_apps_3 = json.dumps(All_apps_3_json)
All_apps_3 = All_apps_3.replace("[", "")
All_apps_3 = All_apps_3.replace("]", "")
All_apps_3=int(All_apps_3)

sql="select count(*) from `apps` WHERE ( `minInstalls` > 1000000 );"
mycursor.execute(sql)
All_apps_4_json = mycursor.fetchone()
All_apps_4 = json.dumps(All_apps_4_json)
All_apps_4 = All_apps_4.replace("[", "")
All_apps_4 = All_apps_4.replace("]", "")
All_apps_4=int(All_apps_4)

#Thống kê số lượng apps Free theo lượt tải
sql="select count(*) from `apps` WHERE (`minInstalls` <= 1000) AND (`free`=1);"
mycursor.execute(sql)
Free_apps_1_json = mycursor.fetchone()
Free_apps_1 = json.dumps(Free_apps_1_json)
Free_apps_1 = Free_apps_1.replace("[", "")
Free_apps_1 = Free_apps_1.replace("]", "")
Free_apps_1=int(Free_apps_1)

sql="select count(*) from `apps` WHERE (`minInstalls` <= 100000 AND `minInstalls` > 1000 ) AND (`free`=1);"
mycursor.execute(sql)
Free_apps_2_json = mycursor.fetchone()
Free_apps_2 = json.dumps(Free_apps_2_json)
Free_apps_2 = Free_apps_2.replace("[", "")
Free_apps_2 = Free_apps_2.replace("]", "")
Free_apps_2=int(Free_apps_2)

sql="select count(*) from `apps` WHERE (`minInstalls` <= 1000000 AND `minInstalls` > 100000 ) AND (`free`=1);"
mycursor.execute(sql)
Free_apps_3_json = mycursor.fetchone()
Free_apps_3 = json.dumps(Free_apps_3_json)
Free_apps_3 = Free_apps_3.replace("[", "")
Free_apps_3 = Free_apps_3.replace("]", "")
Free_apps_3=int(Free_apps_3)

sql="select count(*) from `apps` WHERE ( `minInstalls` > 1000000 ) AND (`free`=1);"
mycursor.execute(sql)
Free_apps_4_json = mycursor.fetchone()
Free_apps_4 = json.dumps(Free_apps_4_json)
Free_apps_4 = Free_apps_4.replace("[", "")
Free_apps_4 = Free_apps_4.replace("]", "")
Free_apps_4=int(Free_apps_4)

#Thống kê số lượng apps Trả phí theo lượt tải
sql="select count(*) from `apps` WHERE (`minInstalls` <= 1000) AND (`free`=0);"
mycursor.execute(sql)
Paid_apps_1_json = mycursor.fetchone()
Paid_apps_1 = json.dumps(Paid_apps_1_json)
Paid_apps_1 = Paid_apps_1.replace("[", "")
Paid_apps_1 = Paid_apps_1.replace("]", "")
Paid_apps_1=int(Paid_apps_1)

sql="select count(*) from `apps` WHERE (`minInstalls` <= 100000 AND `minInstalls` > 1000 ) AND (`free`=0);"
mycursor.execute(sql)
Paid_apps_2_json = mycursor.fetchone()
Paid_apps_2 = json.dumps(Paid_apps_2_json)
Paid_apps_2 = Paid_apps_2.replace("[", "")
Paid_apps_2 = Paid_apps_2.replace("]", "")
Paid_apps_2=int(Paid_apps_2)

sql="select count(*) from `apps` WHERE (`minInstalls` <= 1000000 AND `minInstalls` > 100000 ) AND (`free`=0);"
mycursor.execute(sql)
Paid_apps_3_json = mycursor.fetchone()
Paid_apps_3 = json.dumps(Paid_apps_3_json)
Paid_apps_3 = Paid_apps_3.replace("[", "")
Paid_apps_3 = Paid_apps_3.replace("]", "")
Paid_apps_3=int(Paid_apps_3)

sql="select count(*) from `apps` WHERE ( `minInstalls` > 1000000 ) AND (`free`=0);"
mycursor.execute(sql)
Paid_apps_4_json = mycursor.fetchone()
Paid_apps_4 = json.dumps(Paid_apps_4_json)
Paid_apps_4 = Paid_apps_4.replace("[", "")
Paid_apps_4 = Paid_apps_4.replace("]", "")
Paid_apps_4=int(Paid_apps_4)

# set width of bar
barWidth = 0.25
fig, ax = plt.subplots(figsize =(14, 6))
 
# set height of bar
All_apps = [All_apps_1, All_apps_2, All_apps_3, All_apps_4]
Free_apps = [Free_apps_1, Free_apps_2, Free_apps_3, Free_apps_4]
Paid_apps = [Paid_apps_1, Paid_apps_2, Paid_apps_3, Paid_apps_4]
 
# Set position of bar on X axis
br1 = np.arange(len(All_apps))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
 
rects1 =plt.bar(br1, All_apps, color ='r', width = barWidth, edgecolor ='grey', label ='Tổng số ứng dụng')
rects2 =plt.bar(br2, Free_apps, color ='g', width = barWidth, edgecolor ='grey', label ='Tổng số ứng dụng miễn phí')
rects3 =plt.bar(br3, Paid_apps, color ='b', width = barWidth, edgecolor ='grey', label ='Tổng số ứng dụng trả phí')

# Adding Xticks
plt.xlabel('Số lượt tải', fontweight ='bold', fontsize = 15)
plt.ylabel('Tổng số ứng dụng', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(All_apps))], ['<=1000', '1000 - 100000', '100000 - 1000000', '>1000000'])

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)
plt.legend()
fig.tight_layout()
file_name_4 = 'Download_apps_1.png'
my_path_4 = os.path.abspath(file_name_4)
if os.path.exists(my_path_4):
  os.remove(my_path_4)
plt.savefig(my_path_4, transparent=True)
plt.close('all')