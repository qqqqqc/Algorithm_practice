# 插入排序
import random


def insertion_sort(data_list):
    if len(data_list) < 2:
        return data_list
    else:
        for i in range(len(data_list)):
            for j in range(i-1,-1,-1):
                if data_list[j] > data_list[j+1]:
                    data_list[j],data_list[j+1] = data_list[j+1],data_list[j]

    return data_list


data_list = [random.randint(1,10000) for i in range(10)]
print(insertion_sort(data_list))