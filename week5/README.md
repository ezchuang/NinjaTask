# Assignment - Week 5
## Request 2 Create Database and Table
- **在資料庫中，建立會員資料表，取名字為 member。**
![create table](./result/螢幕擷取畫面%202023-08-02%20022638.png)


## Request 3 CRUD
- **使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和**
  **password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。**
![insert into data](result/螢幕擷取畫面%202023-08-02%20022647.png)

- **使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。**
![show table member](result/螢幕擷取畫面%202023-08-02%20022702.png)

- **使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近**
  **到遠排序。**
![sort table member by time desc](result/螢幕擷取畫面%202023-08-02%20022717.png)

- **使⽤ SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料，並按照 time 欄**
  **位，由近到遠排序。( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )**
![get sorted data ordered 2~4](result/螢幕擷取畫面%202023-08-02%20022733.png)

- **使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。**
![data username = "test"](result/螢幕擷取畫面%202023-08-02%20022746.png)

- **使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。**
![data username = "test" and password = "test"](result/螢幕擷取畫面%202023-08-02%20022805.png)

- **使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改**
  **成 test2。**
![update member table where username = "test"](result/螢幕擷取畫面%202023-08-02%20022833.png)


## Request 4 Aggregate Functions
- **取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。**
![count of members](result/螢幕擷取畫面%202023-08-02%20022923.png)

- **取得 member 資料表中，所有會員 follower_count 欄位的總和。**
![sum of followers for all members](result/螢幕擷取畫面%202023-08-02%20022929.png)

- **取得 member 資料表中，所有會員 follower_count 欄位的平均數。**
![average of followers per member](result/螢幕擷取畫面%202023-08-02%20022946.png)


## Request 5 JOIN
- **在資料庫中，建立新資料表紀錄留⾔資訊，取名字為 message。**
![create table message](result/螢幕擷取畫面%202023-08-02%20023117.png)

- **使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者的姓名。**
![use inner join to show all data](result/螢幕擷取畫面%202023-08-02%20030433.png)

- **使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有**
  **留⾔，資料中須包含留⾔者的姓名。**
![use inner join to show data where username = "test"](result/螢幕擷取畫面%202023-08-02%20030600.png)

- **使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中**
  **欄位 username 是 test 的所有留⾔平均按讚數。**
![use inner join to show the average of like where username = "test"](result/螢幕擷取畫面%202023-08-02%20031326.png)