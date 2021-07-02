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
#Thống kê số lượng apps Free theo lượt tải
sql="select count(*) from `apps` WHERE (`minInstalls` <= 1000) AND (`price`= 0);"
mycursor.execute(sql)
Free_apps_1_json = mycursor.fetchone()
Free_apps_1 = json.dumps(Free_apps_1_json)
Free_apps_1 = Free_apps_1.replace("[", "")
Free_apps_1 = Free_apps_1.replace("]", "")
Free_apps_1=int(Free_apps_1)

sql="select count(*) from `apps` WHERE (`minInstalls` <= 100000 AND `minInstalls` > 1000 ) AND (`price`= 0);"
mycursor.execute(sql)
Free_apps_2_json = mycursor.fetchone()
Free_apps_2 = json.dumps(Free_apps_2_json)
Free_apps_2 = Free_apps_2.replace("[", "")
Free_apps_2 = Free_apps_2.replace("]", "")
Free_apps_2=int(Free_apps_2)

sql="select count(*) from `apps` WHERE (`minInstalls` <= 1000000 AND `minInstalls` > 100000 ) AND (`price`= 0);"
mycursor.execute(sql)
Free_apps_3_json = mycursor.fetchone()
Free_apps_3 = json.dumps(Free_apps_3_json)
Free_apps_3 = Free_apps_3.replace("[", "")
Free_apps_3 = Free_apps_3.replace("]", "")
Free_apps_3=int(Free_apps_3)

sql="select count(*) from `apps` WHERE (`minInstalls` > 1000000 ) AND (`price`= 0);"
mycursor.execute(sql)
Free_apps_4_json = mycursor.fetchone()
Free_apps_4 = json.dumps(Free_apps_4_json)
Free_apps_4 = Free_apps_4.replace("[", "")
Free_apps_4 = Free_apps_4.replace("]", "")
Free_apps_4=int(Free_apps_4)


#Thống kê số lượng apps giá <$1 theo lượt tải
sql5="select count(*) from `apps` WHERE (`minInstalls` <= 1000) AND (`price`>0) AND (`price`<= 1);"
mycursor.execute(sql5)
Paid1_apps_1_json = mycursor.fetchone()
Paid1_apps_1 = json.dumps(Paid1_apps_1_json)
Paid1_apps_1 = Paid1_apps_1.replace("[", "")
Paid1_apps_1 = Paid1_apps_1.replace("]", "")
Paid1_apps_1=int(Paid1_apps_1)

sql6="select count(*) from `apps` WHERE (`minInstalls` <= 100000 AND `minInstalls` > 1000 ) AND (`price`>0) AND (`price`<= 1);"
mycursor.execute(sql6)
Paid1_apps_2_json = mycursor.fetchone()
Paid1_apps_2 = json.dumps(Paid1_apps_2_json)
Paid1_apps_2 = Paid1_apps_2.replace("[", "")
Paid1_apps_2 = Paid1_apps_2.replace("]", "")
Paid1_apps_2=int(Paid1_apps_2)

sql7="select count(*) from `apps` WHERE (`minInstalls` <= 1000000 AND `minInstalls` > 100000 ) AND (`price`>0) AND (`price`<= 1);"
mycursor.execute(sql7)
Paid1_apps_3_json = mycursor.fetchone()
Paid1_apps_3 = json.dumps(Paid1_apps_3_json)
Paid1_apps_3 = Paid1_apps_3.replace("[", "")
Paid1_apps_3 = Paid1_apps_3.replace("]", "")
Paid1_apps_3=int(Paid1_apps_3)

sql8="select count(*) from `apps` WHERE (`minInstalls` > 1000000 ) AND (`price`>0) AND (`price`<= 1);"
mycursor.execute(sql8)
Paid1_apps_4_json = mycursor.fetchone()
Paid1_apps_4 = json.dumps(Paid1_apps_4_json)
Paid1_apps_4 = Paid1_apps_4.replace("[", "")
Paid1_apps_4 = Paid1_apps_4.replace("]", "")
Paid1_apps_4=int(Paid1_apps_4)

#Thống kê số lượng apps <10$ theo lượt tải
sql9="select count(*) from `apps` WHERE (`minInstalls` <= 1000) AND (`price`>1) AND (`price`<=2.5);"
mycursor.execute(sql5)
Paid2_apps_1_json = mycursor.fetchone()
Paid2_apps_1 = json.dumps(Paid2_apps_1_json)
Paid2_apps_1 = Paid2_apps_1.replace("[", "")
Paid2_apps_1 = Paid2_apps_1.replace("]", "")
Paid2_apps_1=int(Paid2_apps_1)

sql10="select count(*) from `apps` WHERE (`minInstalls` <= 100000 AND `minInstalls` > 1000 ) AND (`price`>1) AND (`price`<=2.5);"
mycursor.execute(sql6)
Paid2_apps_2_json = mycursor.fetchone()
Paid2_apps_2 = json.dumps(Paid2_apps_2_json)
Paid2_apps_2 = Paid2_apps_2.replace("[", "")
Paid2_apps_2 = Paid2_apps_2.replace("]", "")
Paid2_apps_2=int(Paid2_apps_2)

sql11="select count(*) from `apps` WHERE (`minInstalls` <= 1000000 AND `minInstalls` > 100000 ) AND (`price`>1) AND (`price`<=2.5);"
mycursor.execute(sql7)
Paid2_apps_3_json = mycursor.fetchone()
Paid2_apps_3 = json.dumps(Paid2_apps_3_json)
Paid2_apps_3 = Paid2_apps_3.replace("[", "")
Paid2_apps_3 = Paid2_apps_3.replace("]", "")
Paid2_apps_3=int(Paid2_apps_3)

sql12="select count(*) from `apps` WHERE (`minInstalls` > 1000000 ) AND (`price`>1) AND (`price`<=2.5);"
mycursor.execute(sql8)
Paid2_apps_4_json = mycursor.fetchone()
Paid2_apps_4 = json.dumps(Paid2_apps_4_json)
Paid2_apps_4 = Paid2_apps_4.replace("[", "")
Paid2_apps_4 = Paid2_apps_4.replace("]", "")
Paid2_apps_4=int(Paid2_apps_4)


#Thống kê số lượng apps giá >$10 theo lượt tải
sql5="select count(*) from `apps` WHERE (`minInstalls` <= 1000) AND (`price`>2.5);"
mycursor.execute(sql5)
Paid3_apps_1_json = mycursor.fetchone()
Paid3_apps_1 = json.dumps(Paid3_apps_1_json)
Paid3_apps_1 = Paid3_apps_1.replace("[", "")
Paid3_apps_1 = Paid3_apps_1.replace("]", "")
Paid3_apps_1=int(Paid3_apps_1)

sql6="select count(*) from `apps` WHERE (`minInstalls` <= 100000 AND `minInstalls` > 1000 ) AND (`price`>2.5);"
mycursor.execute(sql6)
Paid3_apps_2_json = mycursor.fetchone()
Paid3_apps_2 = json.dumps(Paid3_apps_2_json)
Paid3_apps_2 = Paid3_apps_2.replace("[", "")
Paid3_apps_2 = Paid3_apps_2.replace("]", "")
Paid3_apps_2=int(Paid3_apps_2)

sql7="select count(*) from `apps` WHERE (`minInstalls` <= 1000000 AND `minInstalls` > 100000 ) AND (`price`>2.5);"
mycursor.execute(sql7)
Paid3_apps_3_json = mycursor.fetchone()
Paid3_apps_3 = json.dumps(Paid3_apps_3_json)
Paid3_apps_3 = Paid3_apps_3.replace("[", "")
Paid3_apps_3 = Paid3_apps_3.replace("]", "")
Paid3_apps_3=int(Paid3_apps_3)

sql8="select count(*) from `apps` WHERE (`minInstalls` > 1000000 ) AND (`price`>2.5);"
mycursor.execute(sql8)
Paid3_apps_4_json = mycursor.fetchone()
Paid3_apps_4 = json.dumps(Paid3_apps_4_json)
Paid3_apps_4 = Paid3_apps_4.replace("[", "")
Paid3_apps_4 = Paid3_apps_4.replace("]", "")
Paid3_apps_4=int(Paid3_apps_4)

all_Free_apps=Free_apps_1+ Free_apps_2+ Free_apps_3+ Free_apps_4
all_Paid1_apps=Paid1_apps_1 + Paid1_apps_2 + Paid1_apps_3 + Paid1_apps_4
if all_Paid1_apps == 0:
  all_Paid1_apps = 1
all_Paid2_apps=Paid2_apps_1 + Paid2_apps_2 + Paid2_apps_3 + Paid2_apps_4
if all_Paid2_apps == 0:
  all_Paid2_apps = 1
all_Paid3_apps=Paid3_apps_1 + Paid3_apps_2 + Paid3_apps_3 + Paid3_apps_4
if all_Paid3_apps == 0:
  all_Paid3_apps = 1
print(all_Paid3_apps)
category_names = ['<=1000', '1000-100000','100000-1000000', '>1000000']
results = {
    'Free': [Free_apps_1/all_Free_apps, Free_apps_2/all_Free_apps, Free_apps_3/all_Free_apps, Free_apps_4/all_Free_apps],
    '0$ - 1$': [Paid1_apps_1/all_Paid1_apps, Paid1_apps_2/all_Paid1_apps, Paid1_apps_3/all_Paid1_apps, Paid1_apps_4/all_Paid1_apps],
    '1$ - 2.5$': [Paid2_apps_1/all_Paid2_apps, Paid2_apps_2/all_Paid2_apps, Paid2_apps_3/all_Paid2_apps, Paid2_apps_4/all_Paid2_apps],
    'Over 2.5$': [Paid3_apps_1/all_Paid3_apps, Paid3_apps_2/all_Paid3_apps, Paid3_apps_3/all_Paid3_apps, Paid3_apps_4/all_Paid3_apps]
}
results1 = {
    'Free': [Free_apps_1, Free_apps_2, Free_apps_3, Free_apps_4],
    '0$ - 1$': [Paid1_apps_1, Paid1_apps_2, Paid1_apps_3, Paid1_apps_4],
    '1$ - 2.5$': [Paid2_apps_1, Paid2_apps_2, Paid2_apps_3, Paid2_apps_4],
    'Over 2.5$': [Paid3_apps_1, Paid3_apps_2, Paid3_apps_3, Paid3_apps_4]
}
def survey(results, category_names):
    labels= list(results.keys())
    data = np.array(list(results.values()))
    data_1 = np.array(list(results1.values()))
    labels_1= list(results1.keys())
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels_1, widths, left=starts, height=0.5,
                        label=colname, color=color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')
    return fig, ax
survey(results, category_names)
file_name_3 = 'bar_Chart_page_freevspaid.png'
# change the current working
# directory
my_path_3 = os.path.abspath(file_name_3)
if os.path.exists(my_path_3):
  os.remove(my_path_3)
plt.savefig(my_path_3, transparent=True)
plt.close('all')
