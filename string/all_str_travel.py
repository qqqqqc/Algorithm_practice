# 字符串全排列
# 回溯算法
# https://leetcode.cn/problems/permutations/solution/by-huan-huan-20-hblf/
#递归思想

def permutation(s):
    path = []
    res = []
    uesd = [False for _ in range(len(s))]

    def backtracking(s,path,uesd):
        if len(path) == len(s):
            res.append("".join(path[:]))
            return

        for i in range(len(s)):
            if uesd[i]:
                continue

            path.append(s[i])
            uesd[i] = True
            backtracking(s,path,uesd)
            path.pop()
            uesd[i] = False

    backtracking(s, path, uesd)
    return res
