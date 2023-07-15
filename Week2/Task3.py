def func(*data):

    uni_rec = 0
    for i in range(len(data)):

#抓取 第i個字串 及 第1個字元
        current_string = data[i]
        second_char = current_string[1]
        
#預設字串都是獨一無二的
        is_unique = True
        
        for j in range(len(data)):
#不能跟自己比 且 與比較對象重複
            if i != j and data[j][1] == second_char:
                is_unique = False
                break

        if is_unique:
            print(current_string)
            uni_rec =  uni_rec + 1
    
#比較完後發現字元沒有獨一無二的狀況
    if uni_rec == 0:
        print("沒有")



func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

