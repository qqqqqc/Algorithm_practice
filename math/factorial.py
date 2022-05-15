# 计算n的阶乘和




def soultion(n):
    tmp = 1
    res = 0
    for i in range(1,n+1):
        tmp = tmp * i
        res += tmp

    return tmp


print(soultion(5))