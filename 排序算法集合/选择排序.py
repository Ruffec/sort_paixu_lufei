# -*- coding:utf-8 _*-  
"""
Created on 2018/08/27 

@Author: Ruffec

"""
"""
    选择排序（Selection sort）
选择排序：一种简单直观的排序算法。
工作原理：首先在未排序序列中找到最小（大）元素，
         存放到排序序列的起始位置，然后，再从剩余的未排序的元素中继续寻找最小（大）元素，
         然后放到已排序的末尾。直到所有元素均排序完毕。
优点：选择排序与数据移动有关。如果某个元素位于正确的最终位置上，
      则它不会被移动。选择排序每次交换一对元素，它们当中至少有一个将被一道其最终位置上，
      因为对n个元素的表进行排序总共进行至多n-1次交换。在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种。
时间复杂度分析  <-----
最优时间复杂度：O(n^2) 
最坏时间复杂度：O(n^2) 
稳定性：不稳定（考虑升序每次选择最大的情况）
"""
# list 传递的参数，order排序 默认为1，升序，否则降序，仅支持整数类型
def select_sort(alist):
    n = len(alist)
    # 外层循环控制循环次数
    for j in range(0, n -1):
        # 假设找到的最小元素下标为j
        min_index = j
        # 寻找最小元素的过程
        for i in range(j + 1, n):
            # 假设最小下标的值， 大于循环中一个元素，那么就改变最小值的下标
            if alist[min_index] > alist[i]:
                min_index = i
        # 为了容错处理，因为循环一开始就假设把最小值的下标j赋值给变量min_index
        if j != min_index:
            # 在不停的循环中，不停的交换两个不一样大小的值
            alist[min_index], alist[j] = alist[j], alist[min_index]

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("原列表为：%s" % alist)
select_sort(alist)
print("新列表为：%s" % alist)