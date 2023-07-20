// 手機畫面右上角 icon 動作
function popup_menu(){
    // 指定標籤
    let popup_content = document.getElementsByClassName("hidden_items")[0];
    // toggle 動作
    popup_content.style.display = (popup_content.style.display === "flex")? "none" : "flex";
}

// 生成 item 1 ~ 4
function generateMenu(className, num){
    // 指定父標籤
    let obj = document.getElementsByClassName(className)[0];
    for (let i = 1; i <= num; i++){
        // 指定子標籤
        let childTag = document.createElement("a");
        // class 個別賦予
        if (className === "headline_right"){
            childTag.classList.add("headline_item_right");
        }else{
            childTag.classList.add("hidden_item");
        }
        // 生成字串後，加入子標籤內
        childTag.appendChild(document.createTextNode("Item " + String(i)));
        // 子標籤加入父標籤
        obj.appendChild(childTag);
    }
}

// 生成主畫面圖片
function addElements(className, data_original){
    data_original.then(data => {
        let obj = document.getElementsByClassName(className)[0];
        // 呼叫生成器產生 start / end
        let start = gen.next().value;
        let end = gen.next().value;
        // 確認數量沒有超標
        if (end > data.length){
            end = data.length;
        };
        for (let i = start; i < end; i++){

            // 建立第一層各 item 外框 tag
            let childTag = document.createElement("div");
            obj.appendChild(childTag);
            // 賦予 class
            if (className === "img_upper"){
                childTag.classList.add("img_upper_item");
            }else{
                childTag.classList.add("img_item");
            };
            
            // 建立景點照片
            let imgItem = document.createElement("img");
            if (className === "img_upper"){
                // 景點照片 - 縮圖
                imgItem.src = data[i].file;
                imgItem.classList.add("img_shortcut");
            }else{
                // 景點照片
                imgItem.src = data[i].file;
                imgItem.classList.add("img");
            };

            // 建立星星
            let starItem = document.createElement("img");
            if (className !== "img_upper"){
                // 加入星星
                starItem.src = "star_icon.png";
                starItem.classList.add("star");
            };

            // 建立景點名稱
            let strItem = document.createElement("div");
            if (className === "img_upper"){
                // 景點名稱 - 縮圖
                strItem.appendChild(document.createTextNode(data[i].stitle));
                strItem.classList.add("str_shortcut");
            }else{
                // 景點名稱
                strItem.appendChild(document.createTextNode(data[i].stitle));
                strItem.classList.add("str");
            };
            
            // 將建立的元素 " 依序 " 添加到父元素中
            childTag.appendChild(imgItem);
            childTag.appendChild(starItem);
            childTag.appendChild(strItem);
        };
    });
    return data_original
};

// 檢查數量是否達到極限，是否隱藏 Load More 按鈕
function hideButton(data){
    // 抓取指定 class 數量，縮圖 + 大圖
    let img_shortcut_num = document.getElementsByClassName("img_shortcut").length;
    let img_main_num = document.getElementsByClassName("img").length;
    // 比較數量，若相等 (大於) 則將此按鈕 (Load More) 隱藏
    if (img_shortcut_num + img_main_num >= data.length){
        document.querySelector(".more").style.display = "none";
        console.log("成功")
    };
};


// generator
function* next_item(num){
    let keeper = 0
    // 第一次執行會停在下方 yield keeper，生成第一個 Start
    yield keeper
    keeper += 3
    // 第二次執行會停在這，生成第一個 end
    yield keeper
    while (keeper < 99){
        // 後續執行會停在這，生成 Start
        yield keeper
        keeper = num + keeper
        // 後續執行會停在這，生成 end
        yield keeper;
    }
}

// 建立呼叫用變數，若不使用這個，直接呼叫 next_item(12)，每次都會從頭開始做
const gen = next_item(12)

export default {
    popup_menu : popup_menu,
    generateMenu : generateMenu,
    addElements : addElements,
    hideButton : hideButton
}