def get_number(index):
    q = index/2
    r = index%2

    if r == 0:  #整除=偶數
        print(q*3)

    else:       #單數
        print((q+0.5)*3+1)





get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15
#There is a number sequence: 0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15, …