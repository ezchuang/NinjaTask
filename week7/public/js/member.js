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
async function generateMsg(targetId, max, mem_id){
    const msgs = (await (await fetch(`/getMsg/${msg_pointer}`)).json()).data
    let target = document.querySelector(targetId)
    for (data of msgs){
        let msg_id = data.id, id = data.member_id, accountname = data.name, content = data.content, msgLike = data.like_count, msgTime = data.time
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
        // 將 msg_id 帶到 全域變數 msg_pointer 上
        msg_pointer = msg_id
    }
}

// 檢查是否還有 message 能生成
function check_next(msg_min, msg_pointer){
    if (msg_pointer > msg_min){
        return
    }
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

// 刪除複核
function check_id(form, mem_id){
    id = form.querySelector("input").value
    // 刪除時驗證身分，防爆
    if (id != mem_id){
        alert("不要偷刪別人的東西啦!")
        return false
    }
    return confirm("確認要刪除您寶貴的留言嗎?")
}


// 網頁生成時執行
document.addEventListener("DOMContentLoaded", function(){
    generateMsg("#msgZone", 10, mem_id)
})

// Load More Func
document.querySelector("#more_button").addEventListener("click", function(){
    generateMsg("#msgZone", 10, mem_id)
    check_next(msg_min, msg_pointer)
})

// 搜尋使用者名稱
document.querySelector("#findName").addEventListener("click", async function(){
    let input = document.querySelector("#username_to_name").value
    let res = await (await fetch(`/api/member?username=${input}`)).json()
    if (! res.data){
        res = "無此使用者"
    }else{
        res = `${res.data.name} (${input})`
    }
    document.querySelector("#show_name").textContent = res
})

// 更新使用者名稱
document.querySelector("#renewName").addEventListener("click", async function(){
    let input = document.querySelector("#new_name").value
    let res = await (await fetch(`/api/member`,{
        method: "PATCH",
        headers: {
            // "Content-type": "application/json; charset=utf-8",
            "Content-type": "application/json",
        },
        body: JSON.stringify({
            "name" : input,
        }),
    })).json()
    res = Object.keys(res)[0]
    if (res == "error"){
        document.querySelector("#show_res").textContent = "更新失敗"
    }else{
        document.querySelector("#show_res").textContent = "更新成功"
        let welcome_tag = document.querySelector("#welcome")
        welcome_tag.textContent = welcome_tag.textContent.replace(name_show, input)
        name_show = input
    }
})