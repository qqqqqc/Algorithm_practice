# 输入
# 1 输入IP地址
# 2 输入10进制型的IP地址
#
# 输出描述：
# 输出
# 1 输出转换成10进制的IP地址
# 2 输出转换后的IP地址
#
# 示例1
# 输入：
# 10.0.3.193
# 167969729
# 输出：
# 167773121
# 10.3.3.193


def num2ip(num):
    bin_s = bin(int(num))[2:].zfill(32)
    res = []
    for i in range(4):
        res.append(str(int(bin_s[i*8:8*(i+1)],2)))
    result = ".".join(res)
    print(result)

def ip2num(ip):
    ip_list = ip.split(".")
    res = ""
    for i in ip_list:
        res += bin(int(i))[2:].zfill(8)

    print(int(res,2))

num2ip("167969729")