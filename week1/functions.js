document.addEventListener("DOMContentLoaded", function() {
    addElements("img_upper", 3);
    addElements("img_main", 12);
});

function popup_menu(){
    var popup = document.getElementsByClassName("headline_right_mini")[0];

    var popup_content = popup.getElementsByClassName("hidden_items")[0];
    popup_content.style.display = (popup_content.style.display === "flex")? "none" : "flex";
}

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
            imgItem.src="image.jpg";
            imgItem.classList.add("img_shortcut");
        }else{
            imgItem.src="star_icon.png";
            imgItem.classList.add("img");
        };

        var strItem = document.createElement("div");
        if (className === "img_upper"){
            strItem.appendChild(document.createTextNode("Promotion "+ String(i)));
            strItem.classList.add("str_shortcut");
        }else{
            strItem.appendChild(document.createTextNode("Title "+ String(i)));
            strItem.classList.add("str");
        };

        // 將建立的元素添加到父元素中
        childTag.appendChild(imgItem);
        childTag.appendChild(strItem);
    };
}

