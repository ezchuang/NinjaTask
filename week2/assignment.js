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
    
    }
findAndPrint({
"Bob":"My name is Bob. I'm 18 years old.",
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.",
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week",
"Jenny":"Good morning."
});




function calculateSumOfBonus(data){
    // write down your bonus rule in comments
    // your code here, based on your own rules
    }
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



function func(...data){
    // your code here
    }
func("彭⼤牆", "王明雅", "吳明"); // print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有



function getNumber(index){
    // your code here
    }
getNumber(1); // print 4
getNumber(5); // print 10
getNumber(10); // print 15


function findIndexOfCar(seats, status, number){
    // your code here
    }
findIndexOfCar([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2); // print 4
findIndexOfCar([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
findIndexOfCar([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2