from flask import Flask, Markup, render_template
app = Flask(__name__)
import numpy as np
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
#Thống kê lượng đánh giá 1 sao theo lượt tải
sql="select count(*) from `apps` WHERE (`minInstalls` <= 1000) AND (`score` <= 1.0);"
mycursor.execute(sql)
One_star_apps_1_json = mycursor.fetchone()
One_star_apps_1 = json.dumps(One_star_apps_1_json)
One_star_apps_1 = One_star_apps_1.replace("[", "")
One_star_apps_1 = One_star_apps_1.replace("]", "")
One_star_apps_1=int(One_star_apps_1)


sql="select count(*) from `apps` WHERE (`minInstalls` <= 100000 AND `minInstalls` > 1000 ) AND (`score` <= 1.0);"
mycursor.execute(sql)
One_star_apps_2_json = mycursor.fetchone()
One_star_apps_2 = json.dumps(One_star_apps_2_json)
One_star_apps_2 = One_star_apps_2.replace("[", "")
One_star_apps_2 = One_star_apps_2.replace("]", "")
One_star_apps_2=int(One_star_apps_2)


sql="select count(*) from `apps` WHERE (`minInstalls` <= 1000000 AND `minInstalls` > 100000) AND (`score` <= 1.0);"
mycursor.execute(sql)
One_star_apps_3_json = mycursor.fetchone()
One_star_apps_3 = json.dumps(One_star_apps_3_json)
One_star_apps_3 = One_star_apps_3.replace("[", "")
One_star_apps_3 = One_star_apps_3.replace("]", "")
One_star_apps_3=int(One_star_apps_3)


sql="select count(*) from `apps` WHERE (`minInstalls` > 1000000 ) AND (`score` <= 1.0);"
mycursor.execute(sql)
One_star_apps_4_json = mycursor.fetchone()
One_star_apps_4 = json.dumps(One_star_apps_4_json)
One_star_apps_4 = One_star_apps_4.replace("[", "")
One_star_apps_4 = One_star_apps_4.replace("]", "")
One_star_apps_4=int(One_star_apps_4)



#Thống kê lượng đánh giá 1-2 sao theo lượt tải
sql5="select count(*) from `apps` WHERE (`minInstalls` <= 1000) AND (`score` > 1.0 AND `score` <= 2.0);"
mycursor.execute(sql5)
Two_star_apps_1_json = mycursor.fetchone()
Two_star_apps_1 = json.dumps(Two_star_apps_1_json)
Two_star_apps_1 = Two_star_apps_1.replace("[", "")
Two_star_apps_1 = Two_star_apps_1.replace("]", "")
Two_star_apps_1=int(Two_star_apps_1)


sql6="select count(*) from `apps` WHERE (`minInstalls` <= 100000 AND `minInstalls` > 1000) AND (`score` > 1.0 AND `score` <= 2.0);"
mycursor.execute(sql6)
Two_star_apps_2_json = mycursor.fetchone()
Two_star_apps_2 = json.dumps(Two_star_apps_2_json)
Two_star_apps_2 = Two_star_apps_2.replace("[", "")
Two_star_apps_2 = Two_star_apps_2.replace("]", "")
Two_star_apps_2=int(Two_star_apps_2)


sql7="select count(*) from `apps` WHERE (`minInstalls` <= 1000000 AND `minInstalls` > 100000) AND (`score` > 1.0 AND `score` <= 2.0);"
mycursor.execute(sql7)
Two_star_apps_3_json = mycursor.fetchone()
Two_star_apps_3 = json.dumps(Two_star_apps_3_json)
Two_star_apps_3 = Two_star_apps_3.replace("[", "")
Two_star_apps_3 = Two_star_apps_3.replace("]", "")
Two_star_apps_3=int(Two_star_apps_3)


sql8="select count(*) from `apps` WHERE (`minInstalls` > 1000000 ) AND (`score` > 1.0 AND `score` <= 2.0);"
mycursor.execute(sql8)
Two_star_apps_4_json = mycursor.fetchone()
Two_star_apps_4 = json.dumps(Two_star_apps_4_json)
Two_star_apps_4 = Two_star_apps_4.replace("[", "")
Two_star_apps_4 = Two_star_apps_4.replace("]", "")
Two_star_apps_4=int(Two_star_apps_4)


#Thống kê lượng đánh giá 2-3 sao theo lượt tải
sql9="select count(*) from `apps` WHERE (`minInstalls` <= 1000) AND (`score` > 2.0 AND `score` <= 3.0);"
mycursor.execute(sql5)
Three_star_apps_1_json = mycursor.fetchone()
Three_star_apps_1 = json.dumps(Three_star_apps_1_json)
Three_star_apps_1 = Three_star_apps_1.replace("[", "")
Three_star_apps_1 = Three_star_apps_1.replace("]", "")
Three_star_apps_1=int(Three_star_apps_1)

sql10="select count(*) from `apps` WHERE (`minInstalls` <= 100000 AND `minInstalls` > 1000) AND (`score` > 2.0 AND `score` <= 3.0);"
mycursor.execute(sql6)
Three_star_apps_2_json = mycursor.fetchone()
Three_star_apps_2 = json.dumps(Three_star_apps_2_json)
Three_star_apps_2 = Three_star_apps_2.replace("[", "")
Three_star_apps_2 = Three_star_apps_2.replace("]", "")
Three_star_apps_2=int(Three_star_apps_2)

sql11="select count(*) from `apps` WHERE (`minInstalls` <= 1000000 AND `minInstalls` > 100000) AND (`score` > 2.0 AND `score` <= 3.0);"
mycursor.execute(sql7)
Three_star_apps_3_json = mycursor.fetchone()
Three_star_apps_3 = json.dumps(Three_star_apps_3_json)
Three_star_apps_3 = Three_star_apps_3.replace("[", "")
Three_star_apps_3 = Three_star_apps_3.replace("]", "")
Three_star_apps_3=int(Three_star_apps_3)

sql12="select count(*) from `apps` WHERE (`minInstalls` > 1000000 ) AND (`score` > 2.0 AND `score` <= 3.0);"
mycursor.execute(sql8)
Three_star_apps_4_json = mycursor.fetchone()
Three_star_apps_4 = json.dumps(Three_star_apps_4_json)
Three_star_apps_4 = Three_star_apps_4.replace("[", "")
Three_star_apps_4 = Three_star_apps_4.replace("]", "")
Three_star_apps_4=int(Three_star_apps_4)

#Thống kê lượng đánh giá 3-4 sao theo lượt tải
sql5="select count(*) from `apps` WHERE (`minInstalls` <= 1000) AND (`score` > 3.0 AND `score` <= 4.0);"
mycursor.execute(sql5)
Four_star_apps_1_json = mycursor.fetchone()
Four_star_apps_1 = json.dumps(Four_star_apps_1_json)
Four_star_apps_1 = Four_star_apps_1.replace("[", "")
Four_star_apps_1 = Four_star_apps_1.replace("]", "")
Four_star_apps_1=int(Four_star_apps_1)

sql6="select count(*) from `apps` WHERE (`minInstalls` <= 100000 AND `minInstalls` > 1000) AND (`score` > 3.0 AND `score` <= 4.0);"
mycursor.execute(sql6)
Four_star_apps_2_json = mycursor.fetchone()
Four_star_apps_2 = json.dumps(Four_star_apps_2_json)
Four_star_apps_2 = Four_star_apps_2.replace("[", "")
Four_star_apps_2 = Four_star_apps_2.replace("]", "")
Four_star_apps_2=int(Four_star_apps_2)


sql7="select count(*) from `apps` WHERE (`minInstalls` <= 1000000 AND `minInstalls` > 100000) AND (`score` > 3.0 AND `score` <= 4.0);"
mycursor.execute(sql7)
Four_star_apps_3_json = mycursor.fetchone()
Four_star_apps_3 = json.dumps(Four_star_apps_3_json)
Four_star_apps_3 = Four_star_apps_3.replace("[", "")
Four_star_apps_3 = Four_star_apps_3.replace("]", "")
Four_star_apps_3=int(Four_star_apps_3)

sql8="select count(*) from `apps` WHERE (`minInstalls` > 1000000 ) AND (`score` > 3.0 AND `score` <= 4.0);"
mycursor.execute(sql8)
Four_star_apps_4_json = mycursor.fetchone()
Four_star_apps_4 = json.dumps(Four_star_apps_4_json)
Four_star_apps_4 = Four_star_apps_4.replace("[", "")
Four_star_apps_4 = Four_star_apps_4.replace("]", "")
Four_star_apps_4=int(Four_star_apps_4)

#Thống kê lượng đánh giá 4-5 sao theo lượt tải
sql5="select count(*) from `apps` WHERE (`minInstalls` <= 1000) AND (`score` > 4.0 AND `score` <= 5.0);"
mycursor.execute(sql5)
Five_star_apps_1_json = mycursor.fetchone()
Five_star_apps_1 = json.dumps(Five_star_apps_1_json)
Five_star_apps_1 = Five_star_apps_1.replace("[", "")
Five_star_apps_1 = Five_star_apps_1.replace("]", "")
Five_star_apps_1=int(Five_star_apps_1)


sql6="select count(*) from `apps` WHERE (`minInstalls` <= 100000 AND `minInstalls` > 1000) AND (`score` > 4.0 AND `score` <= 5.0);"
mycursor.execute(sql6)
Five_star_apps_2_json = mycursor.fetchone()
Five_star_apps_2 = json.dumps(Five_star_apps_2_json)
Five_star_apps_2 = Five_star_apps_2.replace("[", "")
Five_star_apps_2 = Five_star_apps_2.replace("]", "")
Five_star_apps_2=int(Five_star_apps_2)


sql7="select count(*) from `apps` WHERE (`minInstalls` <= 1000000 AND `minInstalls` > 100000) AND (`score` > 4.0 AND `score` <= 5.0);"
mycursor.execute(sql7)
Five_star_apps_3_json = mycursor.fetchone()
Five_star_apps_3 = json.dumps(Five_star_apps_3_json)
Five_star_apps_3 = Five_star_apps_3.replace("[", "")
Five_star_apps_3 = Five_star_apps_3.replace("]", "")
Five_star_apps_3=int(Five_star_apps_3)


sql8="select count(*) from `apps` WHERE (`minInstalls` > 1000000 ) AND (`score` > 4.0 AND `score` <= 5.0);"
mycursor.execute(sql8)
Five_star_apps_4_json = mycursor.fetchone()
Five_star_apps_4 = json.dumps(Five_star_apps_4_json)
Five_star_apps_4 = Five_star_apps_4.replace("[", "")
Five_star_apps_4 = Five_star_apps_4.replace("]", "")
Five_star_apps_4=int(Five_star_apps_4)

all_One_star_apps=One_star_apps_1+ One_star_apps_2+ One_star_apps_3+ One_star_apps_4
all_Two_star_apps=Two_star_apps_1 + Two_star_apps_2 + Two_star_apps_3 + Two_star_apps_4
all_Three_star_apps=Three_star_apps_1 + Three_star_apps_2 + Three_star_apps_3 + Three_star_apps_4
all_Four_star_apps=Four_star_apps_1 + Four_star_apps_2 + Four_star_apps_3 + Four_star_apps_4
all_Five_star_apps=Five_star_apps_1 + Five_star_apps_2 + Five_star_apps_3 + Five_star_apps_4
category_names = ['<=1000', '1000 - 100000','100000 - 1000000', '>1000000']
results = {
    '0 - 1.0': [One_star_apps_1/all_One_star_apps, One_star_apps_2/all_One_star_apps, One_star_apps_3/all_One_star_apps, One_star_apps_4/all_One_star_apps],
    '1.0 - 2.0': [Two_star_apps_1/all_Two_star_apps, Two_star_apps_2/all_Two_star_apps, Two_star_apps_3/all_Two_star_apps, Two_star_apps_4/all_Two_star_apps],
    '2.0 - 3.0': [Three_star_apps_1/all_Three_star_apps, Three_star_apps_2/all_Three_star_apps, Three_star_apps_3/all_Three_star_apps, Three_star_apps_4/all_Three_star_apps],
    '3.0 - 4.0': [Four_star_apps_1/all_Four_star_apps, Four_star_apps_2/all_Four_star_apps, Four_star_apps_3/all_Four_star_apps, Four_star_apps_4/all_Four_star_apps],
    '4.0 - 5.0': [Five_star_apps_1/all_Five_star_apps, Five_star_apps_2/all_Five_star_apps, Four_star_apps_3/all_Five_star_apps, Four_star_apps_4/all_Five_star_apps]
}# set width of bar
barWidth = 0.15
fig, ax = plt.subplots(figsize =(14, 6))
 
# set height of bar
Star_1 = [One_star_apps_1, Two_star_apps_1, Three_star_apps_1, Four_star_apps_1,Five_star_apps_1]
Star_2 = [One_star_apps_2, Two_star_apps_2, Three_star_apps_2, Four_star_apps_2, Five_star_apps_2]
Star_3 = [One_star_apps_3, Two_star_apps_3, Three_star_apps_3, Four_star_apps_3, Five_star_apps_3]
Star_4 = [One_star_apps_4, Two_star_apps_4, Three_star_apps_4, Four_star_apps_4, Five_star_apps_4] 

# Set position of bar on X axis
br1 = np.arange(len(Star_1))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]

rects1 =plt.bar(br1, Star_1, color ='r', width = barWidth, edgecolor ='grey', label ='<=1000')
rects2 =plt.bar(br2, Star_2, color ='green', width = barWidth, edgecolor ='grey', label ='1000-100000')
rects3 =plt.bar(br3, Star_3, color ='yellow', width = barWidth, edgecolor ='grey', label ='100000-1000000')
rects4 =plt.bar(br4, Star_4, color ='cyan', width = barWidth, edgecolor ='grey', label ='>1000000')

# Adding Xticks
plt.xlabel('Đánh giá ứng dụng', fontweight ='bold', fontsize = 15)
plt.ylabel('Tổng số ứng dụng', fontweight ='bold', fontsize = 15)
plt.xticks([r + 1.5*barWidth for r in range(len(Star_1))], ['0 - 1.0','1.0 - 2.0','2.0 - 3.0','3.0 - 4.0', '4.0 - 5.0'])

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)
ax.bar_label(rects4, padding=3)

plt.legend()
fig.tight_layout()

file_name_6 = 'RATING_APPS_2.png'
# change the current working
my_path_6 = os.path.abspath(file_name_6)
if os.path.exists(my_path_6):
  os.remove(my_path_6)
plt.savefig(my_path_6, transparent=True)
plt.close('all')
