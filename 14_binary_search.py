def binary_search(alist,item):
    """二分查找，递归，产生一个新的列表"""
    n = len(alist)
    mid = n//2
    if n > 0:
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid],item)
        else:
            return binary_search(alist[mid+1:],item)
    return False

if __name__ == "__main__":
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binary_search(li,55))
    print(binary_search(li,100))


def binary_search_2(alist,item):
    """二分查找，非递归（不是产生新列表，只能在原有列表上操作）"""
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first+last)//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False

if __name__ == "__main__":
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binary_search_2(li,26))
    print(binary_search_2(li,100))

    