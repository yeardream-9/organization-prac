def compare_num(com_num, usr_num)
    strike = 0
    ball = 0
    for i in range(0,4): ## Com index 
        for j in range(0,4): ## usr index
            if com_num[i] == usr_num[j]:
                if i == j :
                    strike+=1
                    continue
                else:
                    ball+=1
                    continue
    return strike, ball

