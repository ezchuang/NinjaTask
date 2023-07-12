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
        // console.log(sentance[j]+"出現了"+word[key]+"次");
    }
    // console.log(word.values(), "1");
    console.log(Object.keys(word).length, "2");

    for(var m = 0;m<word.length;m++){
        times = word.values();
        keyWord = word.keys();
        if(times[m]===1){
            console.log(keyWord[m]);
        }
    }

}

func("彭⼤牆", "王明雅", "吳明");
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花");
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")