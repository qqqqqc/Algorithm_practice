# 题目描述
# 身高体重排序
# 身高从低到高，身高相同体重从轻到重，体重相同维持原来顺序
#
# 示例
# 输入：
# 4
# 100 100 120 130
# 40 30 60 501
# 输出：
#
# 2 1 3 4
# 输入：
# 3
# 90 110 90
# 45 60 45
# 输出：
# 1 3 2


# 为了方便已经把输入内容变成变量保存


def height_and_weight_sort(l1,l2):
    l3 = l1.copy()
    l3.sort()
    res = [0] * len(l1)
    res1 = []
    i = 0
    while i < len(l3):
        if l3.count(l3[i]) == 1:
            index = l1.index(l3[i])
            res1.append([l3[i],l2[index]])
            i += 1
        else:
            x = l3.count(l3[i])
            ll = []
            for j in range(len(l1)):
                if l3[i] == l1[j]:
                    ll.append(l2[j])
            ll.sort()
            for j in range(x):
                res1.append([l3[i],ll[j]])
            i += x

    for i in range(len(l1)):
        index = res1.index([l1[i],l2[i]])
        res[i] = index + 1
        res1[index] = 0
    print(res)

l1 = [100,100,120,130]
l2 = [40,30,60,501]
height_and_weight_sort(l1, l2)