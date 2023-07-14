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
    // // let bonus = 0;
    for (let employee of data["employees"]){
        // 薪水數值前處理
        employee["salary"] = employee["salary"].replace(",", "");
        if (employee["salary"].match("USD") != null){
            str_a = employee["salary"].replace(/[^\d]/g, "")
            console.log(str_a)
            str_b = employee["salary"].replace(/[^\d.-]/g, "")
            console.log(str_b)
        };
    };
};

console.log("=== Task 2 ===")
calculateSumOfBonus({
    "employees":[
        {
        "name":"John",
        "salary":"1000.-USD.-",
        "performance":"above average",
        "role":"Engineer"
        }
    ]
}); // call calculateSumOfBonus function

