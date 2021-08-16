#  购物单问题
# https://www.nowcoder.com/practice/f9c6f980eeec43ef85be20755ddbeaf4?tpId=37&&tqId=21239&rp=1&ru=/ta/huawei&qru=/ta/huawei/question-ranking




def get_input_goods(x,y):
    return [x,x*y]

def get_price_important(key,value,annexes):
    price = []
    important = []
    price.append(value[0])
    important.append(value[1])
    if key in annexes:
        price.append(value[0]+annexes[key][0][0])
        important.append(value[1]+annexes[key][0][1])
        if len(annexes[key]) == 2:
            price.append(value[0] + annexes[key][1][0])
            important.append(value[1] + annexes[key][1][1])
            price.append(value[0] + annexes[key][1][0] + annexes[key][0][0])
            important.append(value[1] + annexes[key][1][1] +annexes[key][0][1])
    return price,important
m,n = list(map(int,input().split()))
main_goods = {}
annexes = {}
list_ = [0] * (m+1)
for i in range(n):
    x,y,z = list(map(int,input().split()))
    pi = get_input_goods(x,y)
    if z == 0:
        main_goods[i+1] = pi
    else:
        if z in annexes:
            annexes[z].append(pi)
        else:
            annexes[z] = [pi]

for key,value in main_goods.items():
    price,important = get_price_important(key,value,annexes)
    for j in range(m,-1,-10):
        for k in range(len(price)):
            if j - price[k] >= 0:
                list_[j] = max(list_[j],list_[j-price[k]]+important[k])

print(list_[m])