# 求平方根
#
# 根据平方数的性质——连续n个奇数相加的结果一定是平方数。
# 如：9=1+3+5；
# 16=1+3+5+7；
# 所以，不断的进行奇数相加，并判断x大小即可。代码如下：


def square(s):
    s = int(s)
    k = 1
    n = 0
    while s > 0:
         s = s - k
         k = k + 2
         n += 1
    return n - 1

print(square(15))