import urllib.request as req
import bs4

# 撈出網址內的資料(全部)
def get_page_data(url):
    # 不確定功能
    request = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # 用 bs4 解析html
    root = bs4.BeautifulSoup(data, "html.parser")
    return root

# 網址判斷
def url_catcher(url, page_datas,index):
    if index == 0:
        return url
    next_link_tag = page_datas.find("a", string = "‹ 上頁")
    return "https://www.ptt.cc" + next_link_tag["href"]
    

# 個別抓資料並賦予
def get_data(page_datas, data_cluster):
    # 尋找 class="title" 的 div 標籤 
    pages = page_datas.find_all("div", class_ = "r-ent")

    for page in pages:
        data_row = []
        # 抓 title
        title = page.find("div", class_ = "title")
        if not title.a:
            continue
        data_row.append(title.a.string)
        # 抓 讚數
        gp = page.find("div", class_ = "nrec")
        if not gp.span:
            data_row.append("")
        else:
            data_row.append(gp.span.string)
        # 抓 發布時間
        inner_page = "https://www.ptt.cc" + title.a["href"]
        inner_time = get_page_data(inner_page).find_all("span", class_ = "article-meta-value")
        if len(inner_time) < 4:
            data_row.append("")
        else:
            data_row.append(inner_time[3].string)
        data_cluster.append(data_row)
    return data_row
    
# 初始資料
url = "https://www.ptt.cc/bbs/movie/index.html" # 起始 url
data_cluster = [] # 最終要輸出的資料
page_datas = None # get_page_data() 撈到的 整個 html

for index in range(3):
    # 更改網址
    url = url_catcher(url, page_datas, index)
    # 撈出網址內的資料
    page_datas = get_page_data(url)
    # 個別抓資料並賦予
    get_data(page_datas, data_cluster)


with open("./movie.txt", mode = "w", newline = "", encoding = "utf-8") as txt_file:
    # 逐列寫入，資料間用 "\r\n" 分開
    for row in data_cluster:
        # 逐項寫入，資料間用 "," 分開
        for index in range(len(row)):
            # 最後一行不加 ","
            if index >= len(row)-1:
                txt_file.writelines(row[index])
                continue
            txt_file.writelines(row[index] + ",")
        # 當列完成加上迴車字符
        txt_file.writelines("\r\n")