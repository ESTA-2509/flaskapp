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

category_names = ['1', '2','3', '4', '5']
results={'': results_1}
Average_Rating_apps = (results_1[0]+results_1[1]*2+results_1[2]*3+results_1[3]*4+results_1[4]*5)/All_apps_json
Average_Rating_apps = round(Average_Rating_apps,1)

def survey(results, category_names):
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(18, 0.8))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.2,
                label=colname, color=color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 0),
              loc='upper left', fontsize='15')
    return fig, ax
survey(results, category_names)
Average_Rating_apps=3.7
sql="INSERT INTO `result` (Date, Average_Rating_apps ) VALUES (CURRENT_TIMESTAMP,"+str(Average_Rating_apps)+");"
mycursor.execute(sql)
mydb.commit()
# change the current working
file_name_2 = 'bar_Chart.png'
# directory
my_path_2 = os.path.abspath(file_name_2)
if os.path.exists(my_path_2):
  os.remove(my_path_2)
plt.savefig(my_path_2, transparent=True)
plt.close('all')
