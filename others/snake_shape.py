# 蛇形矩阵
# 描述
# 蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
#
# 例如，当输入5时，应该输出的三角形为：
#
# 1 3 6 10 15
#
# 2 5 9 14
#
# 4 8 13
#
# 7 12
#
# 11
#
#
# 输入描述：
# 输入正整数N（N不大于100）
#
# 输出描述：
# 输出一个N行的蛇形矩阵。


def snakeShape(n):
    res = [[0 for i in range(n)] for j in range(n)]
    initVal = 1
    for i in range(n):
        for j in range(i+1):
            res[i-j][j] = initVal
            initVal += 1

    for d in res:
        end = len(d) - 1
        for i,v in enumerate(d):
            if v != 0:
                print(v,end=" ")
            if i == end:
                print()

snakeShape(5)