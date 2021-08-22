# 快速排序
# 利用分治法(先分后治最后合)
# 快排中分取列表中的中间值，进行大小比较分为大中小三个小列表，递归进行，到最小规模时就很容易得到问题的解,再进行合并就得到最终的解

import random

def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        p = lst[len(lst) // 2]
        left = [i for i in lst if i < p]
        middle = [i for i in lst if i == p]
        right = [i for i in lst if i > p]
        return quick_sort(left) + middle + quick_sort(right)


lst = [random.randint(1,100000) for i in range(100)]

res = quick_sort(lst)
print(res)