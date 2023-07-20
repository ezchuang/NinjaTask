import uer_defined from "./uer_defined.js";


// 連接 API 的 .json
let url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
const data_original = fetch(url)
    .then(response => response.json())
    .then(data => data.result.results)
    .then(function(data){
        // 整理資料
        let data_temp = {};
        const data_cluster_temp = [];
        for (let index = 0; index < data.length; index++){
            // data_temp 初始化
            data_temp = {};
            data_temp["stitle"] = data[index]["stitle"];
            // 切網址，先取前後再切分
            let end = data[index]["file"].toLowerCase().indexOf(".jpg") + 4;
            let start = data[index]["file"].toLowerCase().lastIndexOf("http", end-1);
            data_temp["file"] = data[index]["file"].substr(start, end);
            // 推進去 array 中
            data_cluster_temp.push(data_temp)
        } 
        return data_cluster_temp;
    })


// 網頁啟動執行
document.addEventListener("DOMContentLoaded", function() {
    // 生成 item 1 ~ 4
    uer_defined.generateMenu("headline_right", 4)
    uer_defined.generateMenu("hidden_items", 4)
    
    // 生成主畫面圖片
    uer_defined.addElements("img_upper", data_original);
    uer_defined.addElements("img_main", data_original);
});

// "隱藏選單" 按鈕監聽
document.querySelector(".headline_right_mini").addEventListener("click", () => {
    uer_defined.popup_menu()
})

// "Load More" 按鈕監聽
document.querySelector(".more").addEventListener("click", () => {
    // 添加元素，並 "非同步" 檢查元素是否達到資料上限
    uer_defined.addElements('img_main', data_original).then(data => uer_defined.hideButton(data))
})