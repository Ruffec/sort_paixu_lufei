# -*- coding:utf-8 _*-  
"""
Created on 2018/08/27 

@Author: Ruffec

"""
"""
    基本思想
先将序列分成较多个子序列分别进行排序，再分成较少个子序列分别进行排序，
直到最后为一个序列排序
希尔排序采用每隔固定距离选取一个数的方法划分子序。其中间隔距离称为增量
例如：增量为3的时候，褐色为一个子序列，黄色为一个子序列，灰色为一个子序列 
"""
def shell_insert_sort(a, dk):
    n = len(a)
    for k in range(dk):                     # 间距取dk，一共可以组成dk个子序列
        for i in range(k + dk, n, dk):      #第0，dk,2dk....为一组
            temp = a[i]                      # 记录待插入的元素值
            j = i - dk                       # 子序列的前一个元素
            while j >= k and a[j] > temp:    # 寻找插入的位置
                a[j + dk] = a[j]
                j = j - dk
            a[j + dk] = temp                # 插入
            showarr(a)
def shell_sort(a):
    n = len(a)
    dk = n // 2       # 取第一个dk，长度的一半
    while dk >= 1:
        shell_insert_sort(a, dk)
        dk = dk // 2
def showarr(arr):
    n = len(arr)
    for j in range(n):
        print(arr[j], end=" ")
    print("\n")

a = [49, 38, 65, 97, 76, 13, 27, 49, 55, 4]
shell_sort(a)
