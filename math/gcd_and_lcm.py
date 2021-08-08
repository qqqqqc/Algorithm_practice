# 最大公约数 gcd
# 最小公倍数 lcm


def gcd(a,b):
    if b > a:
        a,b = b,a
    while b:
        a,b = b,a%b
    return a
def lcm(a,b):
    return a*b // gcd(a,b)

print(lcm(5,7))