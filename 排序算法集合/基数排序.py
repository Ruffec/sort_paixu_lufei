#-*- coding:utf-8 _*-  
'''
Created on 2018/09/06 

Author Ruffec

'''
"""
基数排序
    基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。
    由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。
"""
#基于桶排序的基数排序
def radix_sort(lst):
    bucket = [[], [], [], [], [], [], [], [], [], []]  # can not use [[]]*10
    bucket1 = [[], [], [], [], [], [], [], [], [], []]
    for i in lst:
        bucket[i % 10].append(i)
    lst1 = []
    for b in bucket:
        lst1.extend(b)
    for i in lst1:
        bucket1[i // 10 % 10].append(i) # 原始是bucket1[i / 10 % 10].append(i)  但会报类型错误 不是int类型
    lst2 = []
    for b in bucket1:
        lst2.extend(b)
    return lst2


if __name__ == "__main__":
    lst = [17, 4, 56, 38, 9, 91]
    print("initial array:\n", lst)
    print("基数排序 result array:\n", radix_sort(lst))
