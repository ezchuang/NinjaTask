// 手機畫面右上角 icon 動作
export function popup_menu(){
    let popup = document.getElementsByClassName("headline_right_mini")[0];
    
    let popup_content = popup.getElementsByClassName("hidden_items")[0];
    popup_content.style.display = (popup_content.style.display === "flex")? "none" : "flex";
}

// 生成 item 1 ~ 4
export function generateMenu(className, num){
    let obj = document.getElementsByClassName(className)[0];
    for (let i = 1; i <= num; i++){
        let childTag = document.createElement("a");
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
export function addElements(className, data_original){
    data_original.then(data => {
        console.log(data)
        let obj = document.getElementsByClassName(className)[0];
        let start = gen.next().value
        let end = gen.next().value
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
            
            // 將建立的元素添加到父元素中

            childTag.appendChild(imgItem);
            childTag.appendChild(starItem);
            childTag.appendChild(strItem);
        };
    });
};


// generator
export function* next_item(num){
    let keeper = 0
    yield keeper
    keeper += 3
    yield keeper
    while (keeper < 25){
        yield keeper
        keeper = num + keeper
        yield keeper;
        // console.log(keeper, "turn")
    }
}

const gen = next_item(12)
