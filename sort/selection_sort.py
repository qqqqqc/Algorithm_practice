
# 选择排序
import random


def selection_sort(data_lsit):
    for i in range(len(data_lsit)):
        min = i
        for j in range(i+1,len(data_lsit)):
            if data_lsit[i] > data_lsit[j]:
                min = j
        if min != i:
            data_lsit[i],data_lsit[min] = data_lsit[min],data_lsit[i]

    return data_lsit


data_lsit = [random.randint(1,100000) for i in range(20)]

print(selection_sort(data_lsit))

