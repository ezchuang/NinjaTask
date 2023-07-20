import urllib.request as request
import json
import csv
import user_defined

# load in data
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)

# 抓取所需區域
data_list = data["result"]["results"]


# 景點資料(只取第⼀張圖檔的網址)
with open("attraction.csv", mode = "w", newline = "", encoding = "utf-8") as csv_file:
    user_defined.creat_attraction(csv_file, data_list)
    
        
# 以鄰近的捷運站分群
with open("mrt.csv", mode = "w", newline = "", encoding = "utf-8") as csv_file:
    user_defined.creat_mrt(csv_file, data_list)