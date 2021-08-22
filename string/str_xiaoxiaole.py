# 哈哈.消消乐英语不知道用啥表达
# 下面方法名(函数)也不用了吧

def solution(s):
    del_str = ""
    res = []
    for i in s:
        if len(res) == 0:
            if del_str == "":
                res.append(i)
            else:
                res.append(i)
                del_str = ""
        else:
            if i == del_str:
                continue
            elif res[-1] == i:
                del_str = res.pop()
            else:
                res.append(i)
                del_str = ""

    return res

print("".join(solution("abcccbxezzzrf7788fn")))