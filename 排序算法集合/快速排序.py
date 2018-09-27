# -*- coding:utf-8 _*-  
"""
Created on 2018/08/27 

@Author: Ruffec

"""
"""
    算法导论上的快速排序采用分治算法，步骤如下：
1.选取一个数字作为基准，可选取末位数字
2.将数列第一位开始，依次与此数字比较，如果小于此数，将小数交换到左边，
  最后达到小于基准数的在左边，大于基准数的在右边，分为两个数组
3.分别对两个数组重复上述步骤
"""


# TODO:第一种
def QuickSort(arr, firstIndex, lastIndex):
    if firstIndex < lastIndex:
        divIndex = Partition(arr, firstIndex, lastIndex)
        QuickSort(arr, firstIndex, divIndex)
        QuickSort(arr, divIndex + 1, lastIndex)
    else:
        return


def Partition(arr, firstIndex, lastIndex):
    i = firstIndex - 1
    for j in range(firstIndex, lastIndex):
        if arr[j] <= arr[lastIndex]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[lastIndex] = arr[lastIndex], arr[i + 1]
    return i


# TODO：第二种
def quick_sort(ll):
    if len(ll) <= 1:
        return ll
    return quick_sort([i for i in ll[1:] if i < ll[0]]) + ll[0:1] + quick_sort([i for i in ll[1:] if i >= ll[0]])


arr = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]
print("initial array:\n", arr)
QuickSort(arr, 0, len(arr)-1)
print("第一种result array:\n", arr)
print("第二种result array:\n", quick_sort(arr))
