# 最大子序列的和
# 分为连续子序列和非连续子序列
# https://www.jb51.net/article/164664.htm


lst = [-2 ,6, -1, 5, 4, -7, 2, 3]


# 连续
# 1.动态规划
# 使用dp[i] 表示 第i个结尾的连续子序列的最大和
# 分为两种情况
# ①子序列中只有一个元素 即 dp[i] = lst[i]
# ②子序列中有多个元素 ，此时  dp[i] = dp[i-1]+lst[i]
# dp = [0] * len(lst)
# dp[0] = lst[0]
# for i in range(len(lst)):
#     dp[i] = max(lst[i],dp[i-1]+lst[i])
# print(max(dp)) # 14
# 2.正常方法版
# max_recard = 0
# max_num = lst[0]
# for i in range(len(lst)):
#     max_recard += lst[i]
#     max_num = max(max_num,max_recard)
#     if max_recard < 0:
#         max_recard = 0
# print(max_num) # 14




# 非连续
# 使用分治法
# def get3sum(x,y,z):
#     max = x
#     if max < y:
#         max = y
#     if max < z:
#         max = z
#     return max
# def solution(lst):
#     if len(lst) < 2:
#         return lst[0]
#     else:
#         p = len(lst) // 2
#         left = lst[:p]
#         right = lst[p:]
#         sum_left = solution(left)
#         sum_right = solution(right)
#         return get3sum(sum_left,sum_right,sum_left+sum_right)
#
# print(solution(lst)) # 20

# 同样是分治法解决连续

def maxSubArray(lst):
    left = 0
    right = len(lst) - 1
    maxSum = divide(left,right,lst)
    return maxSum
def divide(left,right,lst):
    if left == right:
        return lst[left]
    center = (left+right) // 2
    leftMaxSum = divide(left,center,lst)
    rightMaxSum = divide(center+1,right,lst)

    leftBorderSum = lst[center]
    leftSum = lst[center]
    for i in range(center-1,left-1,-1):
        leftSum += lst[i]
        if leftSum > leftBorderSum:
            leftBorderSum = leftSum

    rightBorderSum = lst[center+1]
    rightSum = lst[center+1]
    for i in range(center+2,right+1):
        rightSum += lst[i]
        if rightSum > rightBorderSum:
            rightBorderSum = rightSum

    return max(leftMaxSum,rightMaxSum,leftBorderSum+rightBorderSum)

print(maxSubArray(lst))