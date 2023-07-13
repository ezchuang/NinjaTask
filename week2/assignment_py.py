# === Task 1 ===
# Time complexity O(n*m), n: key數量, m: value的字串長
def find_and_print(messages) -> None:
    # write down your judgment rules in comments
    """
    符合以下條件的字句(避免 not 的出現):
        1. f"m {n} years old", n > 17
        2. "m a college student"
        3. "m of legal age"
        4. "will vote for"
    """

    # your code here, based on your own rules
    # 檢查子字串用
    def search_for_sub(s_sub, target) -> str:
        # 字串尾部檢查
        if s_sub[-3:] != target[-3:]:
            return search_for_sub(s_sub[:-1], target)
        # 字串頭部檢查
        elif s_sub[:2] != target[:2]:
            return search_for_sub(s_sub[1:], target)
        # 長度大於目標 -> 異常
        elif len(s_sub) > len(target):
            return search_for_sub(s_sub[1:], target)
        # 長度小於目標 -> 異常
        elif len(s_sub) < len(target):
            return target
        return s_sub
    
    # main
    for s in messages:
        for sub in ["m a college student", "m of legal age", "will vote for"]:
            if sub in messages[s]:
                print(s)
                break
        
        if "years old" in messages[s]:
            if search_for_sub(messages[s], "m 17 years old") > "m 17 years old":
                print(s)

print("=== Task 1 ===")            
find_and_print({
    "Bob":"My name is Bob. I'm 18 years old.",
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.",
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning."
})


# === Task 2 ===
# Time complexity O(n*m), n: employees人數, m: salary字串長度
def calculate_sum_of_bonus(data):
    # write down your bonus rules in comments
    """
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
            salary * performance * role * ( 10000 / (sum of salary * 1.2 * 1.2) )
            各員薪水 * 各員取得之權重 * ( 總獎金 / (總薪水 * 最高權重) )
    """

    # your code here, based on your own rules
    salary_sum, bonus_sum = 0, 0
    weight_list = []
    performance_weight = {"above average" : 1.2, "average" : 1.0, "below average" : 0.8}
    role_weight = {"CEO" : 1.2, "Sales" : 1.1, "Engineer" : 1.0}
    for employee in data["employees"]:
        # 薪水數值前處理
        if type(employee["salary"]) is str:
            # Try func ".translate(翻譯表)"
            # .translate({unicode of word you want to replace : repalce to what}, )
            employee["salary"] = employee["salary"].translate({ord(",") : None})
            if "USD" in employee["salary"]:
                # employee["salary"] = int(employee["salary"].replace("USD","")) * 30
                employee["salary"] = int(employee["salary"][:-3]) * 30
            else:
                employee["salary"] = int(employee["salary"])
        # 加總薪水
        salary_sum += employee["salary"]
        # 計算權重(初始化)
        bonus_weight = 1
        # 計算 performance 權重
        bonus_weight *= performance_weight[ employee["performance"] ]
        # 計算 role 權重
        bonus_weight *= role_weight[ employee["role"] ]
        # 計算各員應有份額
        weight_list.append( employee["salary"] * bonus_weight )
    # 確保各位的獎金不會有小數(四捨五入)
    for weight in weight_list:
        bonus = weight * 10000 / (salary_sum * 1.2 * 1.2)
        # 此處 bonus 是 float
        bonus = int(round(bonus, 0))
        bonus_sum += bonus
    # result
    print(bonus_sum)


print("=== Task 2 ===")
calculate_sum_of_bonus({
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
}) # call calculate_sum_of_bonus function


# === Task 3 ===
# Time complexity O(n), n: data中人數
def func(*data):
    # your code here
    middle_name_dict = {} # 針對中間文字計數
    full_name = {} # 逆推回名子
    res = []
    for name in data:
        # 中間字是否在 middle_name_dict
        if name[1] not in middle_name_dict:
            middle_name_dict[name[1]] = 1
            full_name[name[1]] = name
        else:
            middle_name_dict[name[1]] += 1
    # 反向搜尋找出全名
    for middle_name in middle_name_dict:
        if middle_name_dict[middle_name] > 1:
            continue
        res.append(full_name[middle_name])
    # res 為 list，檢查並將元素取出
    if len(res) != 0:
        for s in res:
            print(s)
    else:
        print("沒有")

print("=== Task 3 ===")
func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有


# === Task 4 ===
# Time complexity O(n), n: index (因index為逐次-1遞迴)
def get_number(index):
    # your code here
    def calculator(i):
        if i == 0:
            return 0 
        # 奇數
        if i % 2 > 0 :
            return calculator(i-1) + 4
        # 偶數
        else:
            return calculator(i-1) - 1
    print(calculator(index))

print("=== Task 4 ===")
get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15


# === Task 5 ===
# Time complexity O(n), n: 車廂數目
def find_index_of_car(seats, status, number):
    # your code here
    res = -1
    for i in range(len(status)):
        # 不服務的跳過
        if status[i] == 0:
            continue
        # 位置不夠的跳過
        if seats[i] < number:
            continue
        # 若有符合上述條件的第一次做初始化
        if res == -1:
            res = i
        # 若有位置更貼合人數的，刷新res
        elif seats[i] < seats[res]:
            res = i
    print(res)

print("=== Task 5 ===")
find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2
