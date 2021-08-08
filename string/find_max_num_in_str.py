# 描述
# 输入一个字符串，返回其最长的数字子串，以及其长度。若有多个最长的数字子串，则将它们全部输出（按原字符串的相对位置）
# 本题含有多组样例输入。
#
# 输入描述：
# 输入一个字符串。
#
# 输出描述：
# 输出字符串中最长的数字字符串和它的长度，中间用逗号间隔。如果有相同长度的串，则要一块儿输出（中间不要输出空格）。
#
# 示例1
# 输入：
# abcd12345ed125ss123058789
# a8a72a6a5yy98y65ee1r2
#
# 输出：
# 123058789,9
# 729865,2
def fun(s):

    res = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            j = i
            while i < len(s) and s[i].isdigit():
                i = i + 1
            num = s[j:i]
            res.append(num)
        else:
            i += 1
    new_res = ""
    max_res = sorted(res,key=lambda x:len(x),reverse=True)
    count = len(max_res[0])
    for i in res:
        if len(i) == count:
            new_res += i
    print(new_res+","+str(count))
print(fun("a8a72a6a5yy98y65ee1r2"))
