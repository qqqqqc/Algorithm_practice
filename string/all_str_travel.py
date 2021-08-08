# 字符串全排列
#递归思想
def permutation(s):
    if len(s) == 1:
        return [s]
    else:
        res = []
        for i in range(len(s)):
            for j in permutation(s[:i]+s[i+1:]):
                tmp = s[i] + j
                # print(tmp)
                if tmp not in res:
                    res.append(tmp)
        return res
result = permutation("abc")
print(result)