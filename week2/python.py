# def func(*data):
#     d = {}
#     # '大':['彭⼤牆'],
#     # '明':['王明雅']
#     # '明':['王明雅', '吳明']
#     for name in data:
#         # 1. 中間名如果不在d 裡面
#         if name[1] not in d:
#             # 建立 key & 賦予 value
#             d[name[1]] = [name]
#             # {'明' : ['王明雅']}
#         else:
#             # 既有 key，針對 value 修正
#             d[name[1]].append(name) 
#             # {'明' : ['王明雅', '吳明']}

#         res = []
#         for name in d:
#             if len(d[name])==1:
#                 res = d[name]

#         if len(res)!=1:
#             print("沒有")
#         elif len(res)==1:
#             print(res[0])



# # 用for迴圈掃過整個d
# # 如果 長度 == 1, 印出名字
# # 如果沒有, 印沒有
# func("彭⼤牆", "王明雅", "吳明")  # print 彭⼤牆
# func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花花
# func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
# 哇中間註解變好大
# 我目前這樣印出來是把東西都放進去
# 所以後面我還要再寫一個if?



# 0,1,2,3,4,5....
# ....5,4,3,2,1,0
# 0,1,2,3,4,5...

# 5->4->3->2->1->0
# -4,+1,-4,+1,-4


# [0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15]
# a(5) == 10 == a(4) + 4 # n == 奇數
# a(5) - 4 == 6 == a(4) # n == 奇數


# a(0) == 0
# a(5) == a(4) + 4 # n == 奇數
# a(4) == a(3) - 1 # n == 偶數


def recursive(a): # 遞迴
    if a == 0:
        return 0
    # 偶數
    if a % 2 == 0:
        return recursive(a-1) - 1
    # 奇數
    else:
        return recursive(a-1) + 4

def counter(index):
    print(recursive(index))
    
counter(13)



# print(recursive(13))
# a = recursive(13)
# print(a)

# 0->1->2->3->4->5
# +4,-1,+4,-1,+4