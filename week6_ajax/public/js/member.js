// 添加刪除按鈕
function generate_delete_button(id, mem_id, msg_id){
    // 加 Tag
    let deleteTag
    if (id != mem_id){
        deleteTag = document.createElement("div")
        deleteTag.classList.add("blank_item")
    }else{
        deleteTag = document.createElement("button")
        deleteTag.classList.add("delete")
        deleteTag.appendChild(document.createTextNode("X"))
        // deleteTag.setAttribute("value", msg_id)
        // 插入表單元素(隱藏的)，提送用
        let invisible_1 = document.createElement("input")
        deleteTag.appendChild(invisible_1)
        invisible_1.setAttribute("type", "hidden")
        invisible_1.setAttribute("name", "id")
        invisible_1.setAttribute("value", id)
        let invisible_2 = document.createElement("input")
        deleteTag.appendChild(invisible_2)
        invisible_2.setAttribute("type", "hidden")
        invisible_2.setAttribute("name", "msg_id")
        invisible_2.setAttribute("value", msg_id)
    }
    return deleteTag
}

// 帶小數的對整齊
function financial(x) {
    return Number.parseFloat(x).toFixed(1);
}

// Like 數值整理
function format_like(msgLike){
    if (msgLike >= 1000000){
        let msgLike_N = Number(msgLike)
        msgLike_N = financial(msgLike_N / 1000000)
        msgLike = String(msgLike_N) + " 百萬"
    }else if (msgLike >= 100000){
        let msgLike_N = Number(msgLike)
        msgLike_N = financial(msgLike_N / 100000)
        msgLike = String(msgLike_N) + " 十萬"
    }else if (msgLike >= 10000){
        let msgLike_N = Number(msgLike)
        msgLike_N = financial(msgLike_N / 10000)
        msgLike = String(msgLike_N) + " 萬"
    }
    return msgLike
}

// 生成元素
async function* generateMsg(targetId, max, mem_id){
    const msgs = await (await fetch("/getMsg")).json()
    let target = document.querySelector(targetId)
    let counter_1 = 0
    let counter_2 = 0

    console.log(msgs)
    for (data of msgs){
        let msg_id = data[0], id = data[1], accountname = data[2], content = data[3], msgLike = data[4], msgTime = data[5]
        // 邊界條件測試
        counter_1 += 1
        counter_2 += 1
        if (counter_2 >= msgs.length){
            break
        }
        if (counter_1 >= max){
            counter_1 -= max
            console.log(counter_2, msgs.length)
            yield
        }
        // 建立結構
        if (true){
        let childTag = document.createElement("form");
        target.appendChild(childTag)
        let nameTagFrame = document.createElement("div")
        let nameTag = document.createElement("div")
        let msgTag = document.createElement("div")
        let msgLikeTag = document.createElement("div")
        let msgTimeTag = document.createElement("div")
        childTag.appendChild(nameTagFrame)
        nameTagFrame.appendChild(nameTag)
        childTag.appendChild(msgTag)
        nameTagFrame.appendChild(msgLikeTag)
        childTag.appendChild(msgTimeTag)

        // 添加刪除按鈕
        const deleteTag = generate_delete_button(id, mem_id, msg_id)
        nameTagFrame.appendChild(deleteTag)

        // 賦予 Class
        // childTag.setAttribute("id", id)
        childTag.classList.add("msg_rows")
        nameTagFrame.classList.add("nameTagFrame")
        nameTag.classList.add("name")
        msgTag.classList.add("msg")
        msgLikeTag.classList.add("msgLike")
        msgTimeTag.classList.add("msgTime")
        // 賦予內容
        childTag.setAttribute("onsubmit", "return check_id(this, mem_id)") // for 確認刪除資料
        childTag.setAttribute("action", "/deleteMessage")
        childTag.setAttribute("method", "POST")
        nameTag.appendChild(document.createTextNode(accountname + " : "))
        msgLikeTag.appendChild(document.createTextNode(format_like(msgLike)))
        msgTag.appendChild(document.createTextNode(content))
        msgTimeTag.appendChild(document.createTextNode(msgTime))}
    }
    console.log(counter_2, msgs.length)
    let more_button = document.querySelector("#more_button")
    more_button.setAttribute("class", "hidden")
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

const generator = generateMsg("#msgZone", 10, mem_id)

// 網頁生成時執行
document.addEventListener("DOMContentLoaded", function(){
    generator.next()
})