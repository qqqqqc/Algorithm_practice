# 有兴趣的可以去关注下B站的 背包背包九讲(是男人就看背包就九讲哈哈哈哈哈哈哈哈)
# 问题描述
# 有n个物品，它们有各自的体积和价值，现有给定容量的背包，如何让背包里装入的物品具有最大的价值总和？
#
# 面对每个物品，我们只有选择拿取或者不拿两种选择，不能选择装入某物品的一部分，也不能装入同一物品多次。称为01背包问题，此外还有多重背包与完全背包问题。
#
# 为方便讲解和理解，下面讲述的例子均先用具体的数字代入，即：eg：number＝4，capacity＝8
#
# i（物品编号）     1    2    3    4
# w（体积）        2    3    4    5
# v（价值）        3    4    5    6

# 分析
# 我们不妨设一些变量表示 Vi表示第 i 个物品的价值，Wi表示第 i 个物品的体积，定义V(i,j)当前背包容量 j，
# 在面对下一个物品时，选择只有装或者不装，所以是01
# 先讨论不装的情况 此时背包的容量为 V(i-1,j)
# 在讨论装的情况 V(i-1，j-w[i]) + v[i]
# 我们再讨论什么时候装，什么时候不装，什么时候在装与不装之间犹豫
# ①当前背包容量小于第i个时，肯定是不装
# ②当前背包容量大于等于第i个时，这个时候就比较犹豫了，
# 装了也不一定达到当前最优价值，所以在装与不装之间选择最优的一个 max(V(i-1,j),V(i-1，j-w[i]) + v[i])

n = 4                     # 商品的数量
w= [2 , 3 , 4 , 5]			# 商品的体积2、3、4、5
v = [3 , 4 , 5 , 6]		# 商品的价值3、4、5、6
c = 8				        # 背包大小
dp = [[0 for i in range(c+1)]for j in range(n+1)] # 初始化二维数组

for i in range(1,n+1):
    for j in range(1,c+1):
        if j < w[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i-1]]+v[i-1])

# for i in dp:
#     print(i)
# 最优解回溯
#  其实就是dp[i][j] > dp[i-1][j]
# 字面解释就是 当背包容量相同时，第 i > i-1 说明有物品放进来了

x = [False for i in range(n)]
j = c
for i in range(n,0,-1):
    if dp[i][j] > dp[i-1][j]:
        x[i-1] = True
        j -= w[i-1]

for i in range(n):
    if x[i]:
        print(i+1)  # 2,4
