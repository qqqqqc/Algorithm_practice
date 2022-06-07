# 输入形如 AB-ABC-cABd-Cb@的字符串，输入待分隔长度k；要求输出保留第一个"-"前面的字符串格式，后面
# 的每k个字符一分格，每三个字符中，大写字母数多的三个字母转大写，小写字母较多的三个字母转小写，一样多的不处理

# 实例

# 输入
# AB-ABC-cABd-Cb@

# 输出
# AB-AB-CC-AB-dc-b@

# 说明

# 1.AB-保留
# 2.ABCcABdCb@ 每三个字符一组判断大小
# 3.ABC -> ABC
# 4.cBA -> CBA
# 5.dCb -> dcb
# 6 @ -> @
input_s = "AB-ABC-cABd-Cb@"

k = 2

input_str = input_s.split("-")
head = input_str[0]
body = "-".join(input_str[1:])
body = body.replace("-","")
tmp = ""
for i in range(0,len(body),3):
    line = body[i:i+3]
    count1 = 0
    count2 = 0

    for l in line:
        if "a" <= l <= "z":
            count1 += 1
        if "A" <= l <= "Z":
            count2 += 1

    if count1 > count2:
        tmp += line.lower()
    elif count1 < count2:
        tmp += line.upper()
    else:
        tmp += line

res = []
for t in range(0,len(tmp),k):
    res.append(tmp[t:t+k])

print(head+"-"+"-".join(res))