# 归并排序
# 利用分治法
# 将列表不断细分成最小的单位，然后每个单位分别排序，排序完毕后合并，重复以上过程最后就可以得到排序结果。



def merge(left,right):
    res = []
    i = j = 0
    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])
    return res

def merge_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        p = len(lst) // 2
        left = merge_sort(lst[:p])
        right = merge_sort(lst[p:])
        return merge(left,right)

import random
lst = [random.randint(1,10000) for i in range(100)]
print(merge_sort(lst))