// 生成元素
function generateMsg(targetId, max, msgs, mem_id){
    let target = document.querySelector(targetId)
    let counter = 0
    for (data of msgs){
        let msg_id = data[0], id = data[1], accountname = data[2], content = data[3]
        // 邊界條件測試
        counter += 1
        if (counter >= max){
            break
        }
        // 建立結構
        let childTag = document.createElement("form");
        target.appendChild(childTag)
        let nameTagFrame = document.createElement("div")
        let nameTag = document.createElement("div")
        let msgTag = document.createElement("div")
        childTag.appendChild(nameTagFrame)
        nameTagFrame.appendChild(nameTag)
        childTag.appendChild(msgTag)
        // 添加刪除按鈕
        let deleteTag
        if (id != mem_id){
            deleteTag = document.createElement("div")
            deleteTag.classList.add("blank_item")
        }else{
            deleteTag = document.createElement("button")
            deleteTag.classList.add("delete")
            deleteTag.appendChild(document.createTextNode("X"))
            // 插入表單元素(隱藏的)，提送用
            let invisible_1 = document.createElement("input")
            childTag.appendChild(invisible_1)
            invisible_1.setAttribute("type", "hidden")
            invisible_1.setAttribute("name", "id")
            invisible_1.setAttribute("value", id)
            let invisible_2 = document.createElement("input")
            childTag.appendChild(invisible_2)
            invisible_2.setAttribute("type", "hidden")
            invisible_2.setAttribute("name", "msg_id")
            invisible_2.setAttribute("value", msg_id)
        }
        nameTagFrame.appendChild(deleteTag)
        // 賦予 Class
        // childTag.setAttribute("id", id)
        childTag.classList.add("msg_rows")
        nameTagFrame.classList.add("nameTagFrame")
        nameTag.classList.add("name")
        msgTag.classList.add("msg")
        // 賦予內容
        childTag.setAttribute("onsubmit", "return check_id(this, mem_id)") // for 確認刪除資料
        childTag.setAttribute("action", "/deleteMessage")
        childTag.setAttribute("method", "POST")
        nameTag.appendChild(document.createTextNode(accountname + " : "))
        msgTag.appendChild(document.createTextNode(content))
    }
}

// 表單送出檢查
function check_blank(){
    if (! document.querySelector("#message").value){
        alert("can't send blank message")
        return false
    }
    return true
}

// 刪除覆核
function check_id(form, mem_id){
    id = form.querySelector("input").value
    // 刪除時驗證身分，防爆
    if (id != mem_id){
        alert("不要偷刪別人的東西啦!")
        return false
    }
    return confirm("確認要刪除您寶貴的留言嗎?")
    // return true
}

// 網頁生成時執行
document.addEventListener("DOMContentLoaded", async function(){
    let msgs = await (await fetch("/getMsg")).json()
    generateMsg("#msgZone", 10, msgs, mem_id)
})