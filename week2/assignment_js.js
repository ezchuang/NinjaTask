// === Task 1 ===
// Time complexity O(n*m), n: key數量, m: value的字串長
function findAndPrint(messages){
    // write down your judgment rules in comments
    /*
    符合以下條件的字句(避免 not 的出現):
        1. f"m {n} years old", n > 17
        2. "m a college student"
        3. "m of legal age"
        4. "will vote for"
    */

    // your code here, based on your own rules
    for (let key in messages){
        for (let sub_msg of ["m 18 years old", "m a college student", "m of legal age", "will vote for"]){
            // 找不到對應子字串
            if (messages[key].search(sub_msg) === -1){
                continue;
            }
            // 找到並輸出
            console.log(key);
        }
    }
}


console.log("=== Task 1 ===")
findAndPrint({
    "Bob":"My name is Bob. I'm 18 years old.",
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.",
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning."
});



// === Task 2 ===
// Time complexity O(n*m), n: employees人數, m: salary字串長度
function calculateSumOfBonus(data){
    // write down your bonus rule in comments
    /*
    performance:
        (performance : weight)
        above average : 1.2
        average : 1
        below average : 0.8
    role:
        CEO : 1.2
        Sales : 1.1
        Engineer : 1
    rate:
        bonus: 
            salary * performance * role * (10000 / sum of salary * 1.2 * 1.2)
    */
    // your code here, based on your own rules
    let salary_sum = 0, bonus_sum = 0, weight_list = [];
    let performance_weight = {"above average" : 1.2, "average" : 1.0, "below average" : 0.8}
    let role_weight = {"CEO" : 1.2, "Sales" : 1.1, "Engineer" : 1.0}
    // let bonus = 0;
    for (let employee of data["employees"]){
        // 薪水數值前處理
        if (typeof employee["salary"] === "string"){
            employee["salary"] = employee["salary"].replace(",", "");
            if (employee["salary"].match("USD") != null){
                employee["salary"] = Number(employee["salary"].replace("USD", "")) * 30
            }else{
                employee["salary"] = Number(employee["salary"])
            };
        };
        // 加總薪水
        salary_sum += employee["salary"]
        // 計算權重(初始化)
        bonus_weight = 1;
        // 計算 performance 權重
        bonus_weight *= performance_weight[ employee["performance"] ]
        // 計算 role 權重
        bonus_weight *= role_weight[ employee["role"] ]
        // 計算各員應有份額
        weight_list.push( employee["salary"] * bonus_weight );
    };
    // 確保各位的獎金不會有小數(四捨五入)
    for (let weight of weight_list){
        bonus = weight * 10000 / (salary_sum * 1.2 * 1.2);
        // bonus.toFixed() return 整數的"String"
        bonus = Number(bonus.toFixed());
        bonus_sum += bonus;
    };
    // res
    console.log(bonus_sum);
};

console.log("=== Task 2 ===")
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


// === Task 3 ===
// Time complexity O(n), n: data中人數
function func(...data){
    // your code here
    let middle_name_dict = new Map(); // 針對中間文字計數
    let full_name = new Map(); // 逆推回名子
    let res = [];
    let temp = 0;
    // console.log(middle_name_dict, full_name);
    for (let name of data){
        // 中間字是否在 middle_name_dict
        if (! middle_name_dict.has(name[1])){
            middle_name_dict.set(name[1], 1);
            full_name.set(name[1], name);
        }else{
            temp = middle_name_dict.get(name[1]) + 1;
            middle_name_dict.set(name[1], temp);
        };
    };
    // 反向搜尋找出全名
    for ([middle_name, num] of middle_name_dict){
        if (num > 1){
            continue;
        };
        res.push(full_name.get(middle_name));
    };
    // res 為 array，檢查並將元素取出
    if (res.length != 0){
        for (s of res){
            console.log(s);
        };
    }else{
        console.log("沒有");
    };
};

console.log("=== Task 3 ===")
func("彭⼤牆", "王明雅", "吳明"); // print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有


// === Task 4 ===
// Time complexity O(n), n: index (因index為逐次-1迭代)
function getNumber(index){
    // your code here
    let res = 0;
    for(let i = 1; i <= index; i++){
        // 奇數
        if (i % 2 > 0){
            res += 4;
        // 偶數
        }else{
            res -= 1;
        };
    };
    console.log(res);
};

console.log("=== Task 4 ===")
getNumber(1); // print 4
getNumber(5); // print 10
getNumber(10); // print 15



// === Task 5 ===
// Time complexity O(n), n: 車廂數目
function findIndexOfCar(seats, status, number){
    // your code here
    let res = -1;
    for (let i = 0; i < status.length; i++){
        // 不服務的跳過
        if (status[i] == 0){
            continue;
        };
        // 位置不夠的跳過
        if (seats[i] < number){
            continue;
        };
        // 若有符合上述條件的第一次做初始化
        if (res == -1){
            res = i;
        // 若有位置更貼合人數的，刷新res
        }else if (seats[i] < seats[res]){
            res = i;
        };
    }
    console.log(res)
};

console.log("=== Task 5 ===")
findIndexOfCar([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2); // print 4
findIndexOfCar([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
findIndexOfCar([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2