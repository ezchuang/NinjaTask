// 手機畫面右上角 icon 動作
function popup_menu(){
    var popup = document.getElementsByClassName("headline_right_mini")[0];
    
    var popup_content = popup.getElementsByClassName("hidden_items")[0];
    popup_content.style.display = (popup_content.style.display === "flex")? "none" : "flex";
}

// 生成 item 1 ~ 4
function generateMenu(className, num){
    var obj = document.getElementsByClassName(className)[0];
    for (var i=1; i<=num; i++){
        var childTag = document.createElement("a");
        if (className ==="headline_right"){
            childTag.classList.add("headline_item_right");
        }else{
            childTag.classList.add("hidden_item");
        }
        childTag.appendChild(document.createTextNode("Item " + String(i)))
        
        obj.appendChild(childTag);
    }
    
}

// 生成主畫面圖片
function addElements(className, num){
    var obj = document.getElementsByClassName(className)[0];
    for (var i=1; i <= num; i++){
        // 建立第一層分層tag
        var childTag = document.createElement("div");
        obj.appendChild(childTag);
        // 賦予class
        if (className === "img_upper"){
            childTag.classList.add("img_upper_item");
        }else{
            childTag.classList.add("img_item");
        };
        
        // 建立第二層物件
        var imgItem = document.createElement("img");
        if (className === "img_upper"){
            // 景點照片 - 縮圖
            imgItem.src="image.jpg";
            imgItem.classList.add("img_shortcut");
        }else{
            // 景點照片
            imgItem.src="star_icon.png";
            imgItem.classList.add("img");
        };
        
        var strItem = document.createElement("div");
        if (className === "img_upper"){
            // 景點名稱 - 縮圖
            strItem.appendChild(document.createTextNode("Promotion "+ String(i)));
            strItem.classList.add("str_shortcut");
        }else{
            // 景點名稱
            strItem.appendChild(document.createTextNode("Title "+ String(i)));
            strItem.classList.add("str");
        };
        
        // 將建立的元素添加到父元素中
        childTag.appendChild(imgItem);
        childTag.appendChild(strItem);
    };
}


// 連接 API 的 .json
let url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
let data = fetch(url).then(function(response){
    return response.json();
}).then(function(data){
    console.log(data);
})

// 網頁啟動執行
document.addEventListener("DOMContentLoaded", function() {
    // 生成 item 1 ~ 4
    generateMenu("headline_right", 4)
    generateMenu("hidden_items", 4)
    
    // 生成主畫面圖片
    addElements("img_upper", 3);
    addElements("img_main", 12);
});