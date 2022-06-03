# 称砝码问题
# 描述
# 现有n种砝码，重量互不相等，分别为 m1,m2,m3…mn ；
# 每种砝码对应的数量为 x1,x2,x3...xn 。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。
# 注：称重重量包括 0
# 1 <= n <= 10  1 <= m <= 2000  1<= x <= 10
# 输入描述：
# 对于每组测试数据：
# 第一行：n --- 砝码的种数(范围[1,10])
# 第二行：m1 m2 m3 ... mn --- 每种砝码的重量(范围[1,2000])
# 第三行：x1 x2 x3 .... xn --- 每种砝码对应的数量(范围[1,10])
# 输出描述：
# 利用给定的砝码可以称出的不同的重量数
#
# 示例1
# 输入：
# 2
# 1 2
# 2 1
# 输出：
# 5
# 说明：
# 可以表示出0，1，2，3，4五种重量。


def solution():
    n = int(input())
    mlist = list(map(int,input().split()))
    xlist = list(map(int,input().split()))
    lst = []
    for i in range(n):
        lst += [mlist[i]] * xlist[i]
    weights = {0}
    for i in lst:
        for j in list(weights):
            weights.add(i+j)
    print(weights)
solution()