# 题目描述
# 假设书本的叠放有这样的规则，当A书的长度和宽度都大于B书时，
# 可以将其B书置于A的上方，堆叠摆放，请设计一个程序，
# 根据输入的书本长宽，计算最多可以堆叠摆放多少本书？

# 示例 1
# 输入：
# 3
# 16 15
# 13 12
# 15 14
#
# 输出：3
#
# 说明
# 这里代表有3本书，第1本长宽分别为16和15，第2本长宽为13和12，第3本长宽为15和14，
# 它们可以按照 [13, 12],[15, 14],[16,15] 的顺序堆叠，所以输出3


# 为了方便已经把输入内容变成变量保存

books = [[10, 7], [1, 7], [10, 8], [13, 9], [1, 2], [20, 20], [14, 17], [20, 16],
          [20, 13], [15, 18], [11, 9], [11, 8], [19, 16]]

n = len(books)
tmp = sorted(books,key=lambda x:x[0])
dp = [1] * n
for i in range(1,len(tmp)):
    for j in range(i):
        if tmp[i][1] > tmp[j][1]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))



# m = 3
# l=[[16,15],[13,12],[15 ,14]]
#
# length = []
# high = []
#
# tmp = sorted(l,key=lambda x:x[0])
#
# for t in tmp:
#     length.append(t[0])
#     high.append(t[1])
# res = [[0,0]]
# for i in range(len(tmp)):
#     if length[i] > res[-1][0]:
#         a = high[i:]
#         if high[i] == min(a) and high[i] > res[-1][1]:
#             res.append([length[i],high[i]])
# print(res)
# print(len(res)-1)