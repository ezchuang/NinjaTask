function func(...data){
    // 建立空陣列
    var sentance = [];
    var fullName
    var secondWord;
    // 遍歷函式參數中每個字符串
    for (var i = 0;i<=data.length-1;i++){
        fullName = data[i].split();
        splitName = data[i].split("");
        // 取得字符串中的第二個字
        secondWord = splitName[1];
        // console.log(secondWord);
        if(secondWord){
            sentance.push(secondWord);
        } 
    }
    // console.log(sentance);

    // 計算sentance中每個字符出現的次數
    var word = {};
    for (var j = 0;j<=sentance.length-1;j++){
        key = sentance[j];
            if(word[key]){
                // 假設word中有該字符
                word[key]++;
            }else{
                word[key]=1;
            }
    }
    var res = "沒有"
    for(var m = 0;m < Object.keys(word).length;m++){
        times = Object.values(word);
        keyWord = Object.keys(word);
        if(times[m] != 1){
            continue;
        }
        // for (var x=0; x<data.length; x++){
        //     if (keyWord[m] === data[x][1]){
        //         res = data[x];
        //     }
        // }
        for (var x=0; x<data.length; x++){
            if (data[x].includes(keyWord[m])){
                res = data[x];
            }
            console.log(data[x].includes(keyWord[m]))
        }
    }
    console.log(res)
}

func("彭⼤牆", "王明雅", "吳明");
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花");
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") // 沒有


// var, let , comments
// int = 1,2,3,10000,-1100000
// float = 1.1, 0.8.
// string = 
// array == List = [ 1, 2, 3 ]  size = 3, index =0,1,2
// // list == ListNode =    next_root  = root -> next
// dict = {key:value, ...}
// dict[key] = value
// set_a = set()
// set_a.add()

// key = 1
// value = "asdaqwrasfa"

// set <- key 
// .add(1)
// .add(1)
// .add(2)
// .add(2)
// .add(1)
// .add(1)
// .add(1)

// print(set) == { 1, 2 }

// tuple = ( 1, 2 )


calculateSumOfBonus({"employees":[]} == data)
data["...."] = data.value



calculateSumOfBonus({
    "employees":[
        {
        "name":"John",
        "salary":"1000USD",
        "performance":"above average",
        "role":"Engineer"
        },
        {
        "name":"Bob",
        "salary":60000,
        "performance":"average",
        "role":"CEO"
        },
        {
        "name":"Jenny",
        "salary":"50,000",
        "performance":"below average",
        "role":"Sales"
        }
    ]
}); // call calculateSumOfBonus function