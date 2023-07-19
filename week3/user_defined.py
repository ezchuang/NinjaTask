import csv


def creat_attraction(new_file, target_data):
    # dump step 1 建立 writer 物件
    writer = csv.writer(new_file)

    # 造 item names 景點名稱,區域,經度,緯度,第⼀張圖檔網址
    # landscape_new = {"景點名稱", "區域", "經度", "緯度", "第⼀張圖檔網址"}
    # writer.writerow(landscape_new.keys())
    
    # 資料整理
    for landscape in target_data:
        # .index() return 找到的第一個符合 sub_str 的 起始 index 的 int
        # .rindex() return 找到的最後一個符合 sub_str 的 起始 index 的 int
        # .index() 與 .rindex() 搜尋失敗會 raise ValueError
        landscape_new = {} # 資料轉殖用

        # dump step 2 擷取所需資料
        # 景點名稱
        landscape_new["stitle"] = landscape["stitle"]
        # 區域
        cut_off = landscape["address"].index("區")
        landscape_new["address"] = landscape["address"][cut_off - 2 : cut_off + 1]
        # 經度
        landscape_new["longitude"] = landscape["longitude"]
        # 緯度
        landscape_new["latitude"] = landscape["latitude"]
        # 第⼀張圖檔網址，cut_off_start, cut_off_end 搜尋字串前後位置，並擷取出來
        try:
            cut_off_end = landscape["file"].lower().index(".jpg") + 4
            cut_off_start = landscape["file"][:cut_off_end].lower().rindex("http")
            landscape_new["file"] = landscape["file"][cut_off_start : cut_off_end]
        except:
            landscape_new["file"] = ""
        
        # dump step 3 該 row 的 dict 建立完成，寫入至 new_csv
        writer.writerow( landscape_new.values() )



def creat_mrt(new_file, target_data):
    writer = csv.writer(new_file)
    mrt_stop_dict = {} # 資料轉殖 & 輸出用
    # 建立資料
    for landscape in target_data:
        if landscape["MRT"] == None:
            continue
        # 資料不存在，新建 (站牌 key) & (value 為 array["景點名稱"])
        if landscape["MRT"] not in mrt_stop_dict:
            mrt_stop_dict[ landscape["MRT"] ] = [ landscape["stitle"] ]
        # 資料存在，key 對應之 value array 新增 "景點名稱"
        else:
            mrt_stop_dict[ landscape["MRT"] ].append( landscape["stitle"] )
    # dump
    for mrt_stop in mrt_stop_dict:
        # 將 "捷運站名稱" 保存在第一排
        row_output = [mrt_stop] + mrt_stop_dict[mrt_stop]
        writer.writerow(row_output)