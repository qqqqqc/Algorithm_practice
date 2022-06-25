# 最大连续子序列的和
# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

# 解题

# 以dp[i]表示nums[i]为结尾的子序列的和
# 由于nums[i]必须要选取，那么前面子序列的和是不是正数就要讨论
# 如果dp[i-1] <= 0 那么 dp[i] = nums[i]
# 如果dp[i-1] > 0 那么 dp[i] = nums[i]+dp[i-1]



class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        res.append(nums[0])
        i = 1
        while i < len(nums):
            if res[-1] > 0:
                res.append(res[-1]+nums[i])
            else:
                res.append(nums[i])
            i += 1
        return max(res)

nums = [5,4,-1,7,8]
print(Solution().maxSubArray(nums))