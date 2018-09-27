# -*- coding:utf-8 _*-  
"""
Created on 2018/08/27 

@Author: Ruffec

"""
"""
     归并排序采用分而治之的原理：
一、将一个序列从中间位置分成两个序列；
二、在将这两个子序列按照第一步继续二分下去；
三、直到所有子序列的长度都为1，也就是不可以再二分截止。这时候再两两合并成一个有序序列即可。
"""
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1
    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)

a = [14, 2, 34, 43, 21, 19]
print(merge_sort(a))