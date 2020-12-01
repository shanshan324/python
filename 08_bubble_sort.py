def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
        #外层循环控制走几次，j表示第几次走这个过程，一共走n-1次
        count = 0
        for i in range(0,n-1-j):
            #内层循环控制从头走到尾
            #构造一个游标i，表示列表的下标
            #range()左闭右开
            #一共n个元素，下标从0-(n-1)，游标到n-2的位置停下，但因为range()是左闭右开，所以range(0,n-1)
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        if count==0:
            return


if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    bubble_sort(li)
    print(li)
