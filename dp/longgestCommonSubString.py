# 最长公共字串
# 相对于最长公共子序列少一个考虑的条件




def longgestCommonSubString(a,b):
    dp = [[0 for i in range(len(b)+1)] for j in range(len(a)+1)]

    row = 0
    col = 0

    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                row = i
                col = j


    # 回溯
    res = ""
    i = row
    j = col

    while i > 0 and j > 0:
        if dp[i][j] == 0:
            break

        i -= 1
        j -= 1
        res += a[i]

    return res[::-1]





if __name__ == '__main__':
    print(longgestCommonSubString("weraasdfaswer","asdfas"))