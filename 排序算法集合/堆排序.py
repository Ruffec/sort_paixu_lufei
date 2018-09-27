# -*- coding:utf-8 _*-  
"""
Created on 2018/08/27 

@Author: Ruffec

"""
"""
堆排序是利用堆（大顶堆或小顶堆都可）的性质，每次从堆顶取一个元素，然后对堆重新调整，
最后完成排序的排序算法，时间复杂度和快速排序、归并排序一样都是O(n*log n)。
并且堆的最坏时间复杂度和最优时间复杂度都是O(n*log n)，比较稳定。由于需要建立一个堆，
所以空间复杂度是n。
"""
def sift_down(arr, start, end):
    root = start
    while True:
        # 从root开始对最大堆调整
        child = 2 * root + 1
        if child > end:
            break
        # 找出两个child中较大的一个
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            # 最大堆小于较大的child，交换顺序
            arr[root], arr[child] = arr[child], arr[root]
            # 正在调整的节点设置为root
            root = child
        else:
            # 无需调整的时候， 退出
            break

def heap_sort(arr):
    # 从最后一个有子节点的孩子还是调整最大堆
    first = len(arr) // 2 - 1
    for start in range(first, -1, -1):
        sift_down(arr, start, len(arr) - 1)

    # 将最大的放到堆的最后一个，堆-1， 继续调整排序
    for end in  range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)

l = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
print(l)
heap_sort(l)
print(l)

# 使用heapq
from heapq import heappush, heappop
def heap_sort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]
alist = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print("heap实现：", heap_sort(alist))