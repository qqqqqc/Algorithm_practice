#描述
# 输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。
#
# 数据范围：输入的字符串长度满足 1 \le n \le 1000 \1≤n≤1000
#
# 输入描述：
# 输入一行字符串，可以有空格
#
# 输出描述：
# 统计其中英文字符，空格字符，数字字符，其他字符的个数
#
# 示例1
# 输入：
# 1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\][
# 输出：
# 26
# 3
# 10
# 12


def solution():
    input_str = input().strip("\n")
    other = 0
    num = 0
    space = 0
    m = 0
    for i in input_str:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            m += 1
        elif i == " ":
            space += 1
        else:
            other += 1
    print(m)
    print(space)
    print(num)
    print(other)

soultion()