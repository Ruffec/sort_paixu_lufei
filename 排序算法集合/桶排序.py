#-*- coding:utf-8 _*-  
'''
Created on 2018/09/06 

Author Ruffec

'''
# 桶排序
# 为了节省空间和时间，我们需要指定要排序的数据中最小以及最大的数字的值，来方便桶排序算法的运算。
def sort(arr):
    result = []
    for index in range(0,len(arr)):
        result.append(0)
    for index in range(len(arr)):
        counter = result[arr[index]]+1
        result[arr[index]]=counter
    return result

if __name__ == '__main__':
    arr = [1,3,5,7,9,2,9,4,6,8,0,1,1,3,2,2,2,2]
    print("initial array:\n", arr)
    print("桶排序 result array:")
    arr = sort(arr)
    for item in range(len(arr)):
        if arr[item]!=0:
            step = arr[item]
            while step>0:
                print(item, end=" ")
                step-=1