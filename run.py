import os
owd = os.getcwd()
os.chdir("static/chart/")
from page_index.lineChart import *
from page_index.pieChart import *
from page_index.barChart import *
from page_index.barChart_freevspaid import *
from page_index.download_apps import *
from page_rating.barChart_1 import *
from page_rating.barChart_2 import *
from page_cate.Top_10 import *
from page_cate.Top_10_lower import *
from page_android.linechart1 import *
from page_android.chart2 import * 
from page_cate.Cate import *
os.chdir(owd)
print("endstep1")