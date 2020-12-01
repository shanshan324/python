# def quick_sort(alist,first,last):
#     if first>=last:
#         return
#     mid_value=alist[first]
#     low=first
#     high=last
#     while low<high:
#         while low<high and alist[high]>=mid_value:
#             high-=1
#         alist[low]=alist[high]
#         while low<high and alist[low]<mid_value:
#             low+=1
#         alist[high]=alist[low]
#     alist[low]=mid_value
#     quick_sort(alist,first,low)
#     quick_sort(alist,low+1,last)

# if __name__=="__main__":
#     li=[54,26,93,17,77,31,44,55,20]
#     print(li)
#     quick_sort(li,0,len(li)-1)
#     print(li)


# def bubble_sort(alist):
#     n=len(alist)
#     for j in range(n-1):
#         count=0
#         for i in range(n-1-j):
#             if alist[i]>alist[i+1]:
#                 alist[i],alist[i+1]=alist[i+1],alist[i]
#                 count+=1
#         if count==0:
#             return

# if __name__=="__main__":
#     li=[54,26,93,17,77,31,44,55,20]
#     print(li)
#     bubble_sort(li)
#     print(li)
                

# def select_sort(alist):
#     n=len(alist)
#     for j in range(n-1):
#         min_index=j
#         for i in range(j+1,n):
#             if alist[min_index]>alist[i]:
#                 min_index=i
#         alist[j],alist[min_index]=alist[min_index],alist[j] 

# if __name__=="__main__":
#     li=[54,26,93,17,77,31,44,55,20]     
#     print(li)
#     select_sort(li)
#     print(li)  


# def insert_sort(alist):
#     n=len(alist)
#     for j in range(1,n):
#         i=j
#         while i>0:
#             if alist[i]<alist[i-1]:
#                 alist[i],alist[i-1]=alist[i-1],alist[i]
#                 i-=1
#             else:
#                 break

# if __name__=="__main__":
#     li=[54,26,93,17,77,31,44,55,20]
#     print(li)
#     insert_sort(li)
#     print(li)


# def merge_sort(alist):
#     n=len(alist)
#     if n<=1:
#         return alist
#     mid=n//2
#     left_li=merge_sort(alist[:mid])
#     right_li=merge_sort(alist[mid:])
    
#     left_pointer,right_pointer=0,0
#     result=[]
#     while left_pointer<len(left_li) and right_pointer<len(right_li):
#         if left_li[left_pointer]<=right_li[right_pointer]:
#             result.append(left_li[left_pointer])
#             left_pointer+=1
#         else:
#             result.append(right_li[right_pointer])
#             right_pointer+=1
#     result+=left_li[left_pointer:]
#     result+=right_li[right_pointer:]
#     return result

# if __name__=="__main__":
#     li=[54,26,93,17,77,31,44,55,20]
#     print(li)
#     sorted_li=merge_sort(li)
#     print(sorted_li)


# class Node:
#     def __init__(self,x):
#         self.val=x
#         self.next=None
# class Solution:
#     def reversePrint(self,head):
#         if head==None:
#             return []
#         else:
#             return self.reversePrint(head.next)+[head.val]

# if __name__=="__main__":
#     head=Node(1)
#     head.next=Node(3)
#     head.next.next=Node(2)
#     b=Solution()
#     print(b.reversePrint(head))


# def moveZeroes(nums):
#     count=0
#     # for i in nums:
#     #     if i==0:
#     #         count+=1
#     #         nums.remove(i)
#     i=0
#     while i:
#         if nums[i]==0:
#             count+=1

#     for _ in range(count):
#         nums.append(0)
#     return nums


# def moveZeroes(nums):
#     # j=0
#     # for i in range(len(nums)):
#     #     if nums[i]:
#     #         nums[j],nums[i]=nums[i],nums[j]
#     #         j+=1
#     i,j=0,0
#     while i<len(nums) and j<len(nums):
#         if nums[i]:
#             nums[j],nums[i]=nums[i],nums[j]
#             j+=1
#         i+=1
#     return nums

# if __name__=="__main__":
#     nums=[0,1]
#     print(moveZeroes(nums))




# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.children=None

# class Solution:
#     def preorder(self, root):
#         res=[]
#         def traverse(root):
#             if not root:
#                 return
#             res.append(root.val)
#             for child in root.children:
#                 traverse(child)
#         traverse(root)
#         return res


# class TreeNode:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
# class Solution:
#     def pathSum(self,root,total):
#         ret = list()
#         path = list()
#         def dfs(root, total):
#             if not root:
#                 return
#             path.append(root.val)  #把当前节点加入到sublist中
#             total -= root.val
#             if not root.left and not root.right and total == 0:
#                 ret.append(path[:])
#             dfs(root.left, total)  #如果没到达叶子节点，就继续从他的左右两个子节点往下找
#             dfs(root.right, total)
#             path.pop()
        
#         dfs(root, total)
#         return ret

# if __name__=="__main__":
#     root=TreeNode(5)
#     root.left=TreeNode(4)
#     root.right=TreeNode(8)
#     root.left.left=TreeNode(11)
#     root.right.left=TreeNode(13)
#     root.right.right=TreeNode(4)
#     a=Solution()
#     print(a.pathSum(root,20))



"""动态规划类型的题目
01.在一个数组arr中，找出不相邻的数字，使得最后的和最大
"""
###递归dp
# def rec_opt(arr,i):
#     if i==0:
#         return arr[0]
#     elif i==1:
#         return max(arr[0],arr[1])
#     else:
#         A=rec_opt(arr,i-2)+arr[i]
#         B=rec_opt(arr,i-1)
#         return max(A,B)

###非递归dp
# import numpy as np
# def dp_opt(arr):
#     opt=np.zeros(len(arr))
#     opt[0]=arr[0]
#     opt[1]=max(arr[0],arr[1])
#     for i in range(2,len(arr)):
#         A=opt[i-2]+arr[i]
#         B=opt[i-1]
#         opt[i]=max(A,B)
#     return opt[len(arr)-1]

# if __name__=="__main__":
#     arr=[1,2,4,1,7,8,3]
#     #print(rec_opt(arr,6))
#     print(dp_opt(arr))

"""
02.给定一个正整数s，判断数组arr中，是否有一组数字加起来等于s
"""
# def rec_subset(arr,i,s):
#     if s==0:
#         return True
#     elif i==0:
#         return arr[0]==s
#     elif arr[i]>s:
#         return rec_subset(arr,i-1,s)
#     else:
#         A=rec_subset(arr,i-1,s-arr[i])
#         B=rec_subset(arr,i-1,s)
#         return max(A,B)

# if __name__=="__main__":
#     arr=[3,34,4,12,5,2]
#     print(rec_subset(arr,len(arr)-1,9))


"""起始位置"""
# class Solution:
#     def searchRange(self, nums, target):
#         res=[-1,-1]
#         l=0
#         r=len(nums)-1
#         while l<=r:
#             mid=l+(r-l)//2
#             if nums[mid]<target:
#                 l=mid+1
#             elif nums[mid]>target:
#                 r=mid-1
#             else:
#                 if mid-1<0 or nums[mid-1]<target:
#                     res[0]=mid
#                     break
#                 r=mid-1
#         l=0
#         r=len(nums)-1
#         while l<=r:
#             mid=l+(r-l)//2
#             if nums[mid]<target:
#                 l=mid+1
#             elif nums[mid]>target:
#                 r=mid-1
#             else:
#                 if mid+1==len(nums) or nums[mid+1]>target:
#                     res[1]=mid
#                     break
#                 l=mid+1
#         return res
# if __name__=="__main__":
#     nums=[5,7,7,8,8,10]
#     a=Solution()
#     print(a.searchRange(nums,8))



"""
找出数组中绝对值最小的数（数组是有序数组）
"""
# def findmin(nums):
#     n=len(nums)
#     l=0
#     r=n-1
#     if nums[0]>=0:
#         return nums[0]
#     elif nums[n-1]<0:
#         return abs(nums[n-1])
#     else:
#         while l<=r:
#             mid=l+(r-l)//2
#             if nums[mid]>=0:
#                 if nums[mid-1]>=0:
#                     r=mid-1
#                 else:
#                     if nums[mid]<abs(nums[mid-1]):
#                         return nums[mid]
#                     else:
#                         return abs(nums[mid-1])
#             else:
#                 if nums[mid+1]<0:
#                     l=mid+1
#                 else:
#                     if abs(nums[mid])<nums[mid+1]:
#                         return abs(nums[mid])
#                     else:
#                         return nums[mid+1]

# if __name__=="__main__":
#     # nums=[-11,-3,1,4,5,9,20,43,57]
#     # nums=[-12,-8,-5,-3,-2,-1,5,7,20]
#     # nums=[2,4,8,33,57,89,102]
#     nums=[-24,-12,-9,-5,-3]
#     print(findmin(nums))


# class LinkNode:
#     def __init__(self,val):
#         self.val=val
#         self.next=None
# class Solution:
#     """
#     判断链表是否有环
#     """
#     # def hascycle(self,head):
#     #     fast,slow=head,head
#     #     while fast:
#     #         fast=fast.next
#     #         if fast:
#     #             fast=fast.next
#     #         if fast==slow:
#     #             return True
#     #         slow=slow.next
#     #     return False


#     # def hascycle(self,head):
#     #     fast,slow=head,head
#     #     while fast and fast.next:
#     #         fast=fast.next.next
#     #         slow=slow.next
#     #         if fast==slow:
#     #             return True
#     #     return False

"""
判断环的长度：快慢指针相遇后继续移动，直到第二次相遇。
两次相遇间移动的次数即为环的长度
"""
    # def linklength(self,head):
    #     fast,slow=head,head
    #     length=0  #环的长度
    #     count=0  #相遇次数
    #     while fast and fast.next:
    #         fast=fast.next.next
    #         slow=slow.next
    #         length+=1
    #         if fast==slow:
    #             count+=1
    #             if count==1:
    #                 length=0
    #             if count==2:
    #                 return length
    #     return False


# if __name__=="__main__":
#     head=LinkNode(1)
#     head.next=LinkNode(2)
#     head.next.next=LinkNode(3)
#     head.next.next.next=head.next
#     a=Solution()
#     print(a.hascycle(head))
#     # print(a.linklength(head))


"""
用rand5()实现rand7()
rand5可以随机生成1,2,3,4,5
rand7可以随机生成1,2,3,4,5,6,7
将rand5映射到一个能产生更大随机数的randA，A>7
5*(rand5()-1)+rand5()：表示rand5产生1-5的数，-1就产生0到4的数，*5后可以产生的数是0,5,10,15,20，加上第二个rand5产生的1,2,3,4,5。
可以得到1到25，而且每个数都只由一种组合得到，即可以等概率生成1到25
"""
# import random
# def rand5():
#     return random.randint(1,5)

# def rand7():
#     res=25
#     while res>21:
#         res=5*(rand5()-1)+rand5()
#     return res%7+1



"""
机器人的运动范围
"""
# class Solution:
#     def movingCount(self, m: int, n: int, k: int) -> int:
#         # queue,visited=[(0,0,0,0)],set()
#         # while queue:
#         #     i,j,si,sj=queue.pop(0)
#         #     if i>=m or j>=n or k<si+sj or (i,j) in visited:
#         #         continue
#         #     visited.add((i,j))
#         #     queue.append((i+1,j,si+1 if (i+1)%10 else si-8,sj))
#         #     queue.append((i,j+1,si,sj+1 if (j+1)%10 else sj-8))
#         # return len(visited)

#         def isvaild(i,j,k):
#             s=0
#             while i!=0:
#                 s+=i%10
#                 i//=10
#             while j!=0:
#                 s+=j%10
#                 j//=10
#             return s<=k

#         queue,visited=[(0,0)],set()
#         while queue:
#             i,j=queue.pop(0)
#             if i>=m or j >=n or not isvaild(i,j,k) or (i,j) in visited:
#                 continue
#             visited.add((i,j))
#             queue.append((i+1,j))
#             queue.append((i,j+1))
#         return len(visited)

# if __name__=="__main__":
#     i,j,k=2,3,1
#     # i,j,k=3,1,0
#     a=Solution()
#     print(a.movingCount(i,j,k))


"""
剪绳子
"""
# class Solution:
#     def cuttingRope(self, n):
#         res=1
#         if n<=3:
#             return 1*(n-1)
#         if n%3==1:
#             res*=4
#             n-=4
#         if n%3==2:
#             res*=2
#             n-=2
#         while n:
#             res*=3
#             n-=3
#         return res
            
# if __name__=="__main__":
#     a=Solution()
#     n=10
#     print(a.cuttingRope(n))



"""
二进制中1的个数
"""
# class Solution:
#     def hammingWeight(self, n):
#         count=0
#         if n==0:
#             return 0
#         while n:
#             if n%2==1:
#                count+=1
#             n//=2
#         return count
# if __name__=="__main__":
#     a=Solution()
#     print(a.hammingWeight(9))



# class Solution:
#     def printNumbers(self, n):
#         res=[]
#         if n<=0:
#             return
#         for i in range(1,10**n):
#             res.append(i)
#         return res
# if __name__=="__main__":
#     a=Solution()
#     print(a.printNumbers(2))


# class Solution:
#     def spiralOrder(self, matrix):
#         if not matrix:
#             return []
#         l,r,t,b,res=0,len(matrix[0])-1,0,len(matrix)-1,[]
#         while True:
#             for i in range(l,r+1):
#                 res.append(matrix[t][i])  #left to right
#             t+=1
#             if t>b:
#                 break
#             for i in range(t,b+1):
#                 res.append(matrix[i][r])  #top to bottom
#             r-=1
#             if l>r:
#                 break
#             for i in range(r,l-1,-1):
#                 res.append(matrix[b][i])
#             b-=1
#             if t>b:
#                 break
#             for i in range(b,t-1,-1):
#                 res.append(matrix[i][l])
#             l+=1
#             if l>r:
#                 break
#         return res

# if __name__=="__main__":
#     matrix = [[1,2,3],[4,5,6],[7,8,9]]
#     a=Solution()
#     print(a.spiralOrder(matrix))



# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         i,j,res,mid=0,0,[],-1
#         while i<len(nums1) and j<len(nums2):
#             if nums1[i]<=nums2[j]:
#                 res.append(nums1[i])
#                 i+=1
#             else:
#                 res.append(nums2[j])
#                 j+=1
#         res+=nums1[i:]
#         res+=nums2[j:]
#         i,j=0,len(res)-1
#         mid=i+(j-i)//2
#         if len(res)%2:
#             ans=res[mid]
#         else:
#             ans=(res[mid]+res[mid+1])/2
#         return ans
# if __name__=="__main__":
#     a=Solution()
#     nums1=[1,2]
#     nums2=[3,4]
#     print(a.findMedianSortedArrays(nums1,nums2))

# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         def getKth(nums1,start1,end1,nums2,start2,end2,k):
#             len1=end1-start1+1
#             len2=end2-start2+1
#             if len1>len2:
#                 return getKth(nums2,start2,end2,nums1,start1,end1,k)
#             if len1==0:
#                 return nums2[start2+k-1]
#             if k==1:
#                 return min(nums1[start1],nums2[start2])
#             i=start1+min(len1,k//2)-1
#             j=start2+min(len2,k//2)-1
#             if nums1[i]>nums2[j]:
#                 return getKth(nums1,start1,end1,nums2,j+1,end2,k-(j-start2+1))
#             else:
#                 return getKth(nums1,i+1,end1,nums2,start2,end2,k-(i-start1+1))

#         n,m=len(nums1),len(nums2)
#         left,right=(n+m+1)//2,(n+m+2)//2
#         return (getKth(nums1,0,n-1,nums2,0,m-1,left)+getKth(nums1,0,n-1,nums2,0,m-1,right))
# if __name__=="__main__":
#     a=Solution()
#     nums1=[1,3,4,9]
#     nums2=[1,2,3,4,5,6,7,8,9,10]
#     print(a.findMedianSortedArrays(nums1,nums2))


# li = [
#    {"name": "xiaoming", "age": 22},
#    {"name": "xiaogang", "age": 13},
#    {"name": "limin", "age": 19},
#    {"name": "wkqlj", "age": 42},
#    {"name": "AA", "age": 2}
# ]
# import operator
# li.sort(key=operator.itemgetter('age'),reverse=False)
# print(li)

"""
遍历字典元素时要根据年龄进行比较，并交换字典中相应的元素的值（使用冒泡排序算法）O(N^2)
"""
# class Solution:
#     def bubble_sort(self,alist):
#         n=len(alist)
#         for j in range(n-1):
#             count=0
#             for i in range(0,n-1-j):
#                 if alist[i]["age"]>alist[i+1]["age"]:
#                     alist[i],alist[i+1]=alist[i+1],alist[i]
#                     count+=1
#             if count==0:
#                 return
#         return alist
# if __name__=="__main__":
#     a=Solution()
#     li = [{"name": "xiaoming", "age": 22},
#     {"name": "xiaogang", "age": 13},
#     {"name": "limin", "age": 19},
#     {"name": "wkqlj", "age": 42},
#     {"name": "AA", "age": 2}]
#     print(a.bubble_sort(li))


# class Solution:
#     def permutation(self,str):
#         c,res=list(s),[]
#         def dfs(x):
#             if x==len(c)-1:
#                 res.append(''.join(c))
#                 return
#             dic=set()
#             for i in range(x,len(c)):
#                 if c[i] in dic:
#                     continue
#                 dic.add(c[i])
#                 c[i],c[x]=c[x],c[i]
#                 dfs(x+1)
#                 c[i],c[x]=c[x],c[i]
#         dfs(0)
#         return res
# if __name__=="__main__":
#     s="abc"
#     a=Solution()
#     print(a.permutation(s))


# class Solution:
#     def majorityElement(self, nums):
#         # if not nums:
#         #     return
#         # length=len(nums)//2
#         # dic={}
#         # for i in set(nums):
#         #     dic[i]=nums.count(i)
#         #     if dic[i]>=length:
#         #         return i
#         votes=0
#         for num in nums:
#             if votes==0:
#                 x=num
#             if num==x:
#                 votes+=1
#             else:
#                 votes-=1
#         return x
# if __name__=="__main__":
#     nums=[1, 2, 3, 2, 2, 2, 5, 4, 2]
#     a=Solution()
#     print(a.majorityElement(nums))


# class Solution:
#     def getLeastNumbers(self, arr, k):
#         # if k>len(arr):
#         #     return
#         # arr.sort()
#         # res=[]
#         # for i in range(k):
#         #     res.append(arr[i])
#         # return res

#         def quick_sort(alist,first,last):
#             # mid_value=alist[last]
#             # i=first
#             # for j in range(first,last):
#             #     if alist[j]<=mid_value:
#             #         alist[i],alist[j]=alist[j],alist[i]
#             #         i+=1
#             # alist[i],alist[last]=alist[last],alist[i]
#             # return i

#             mid_value=alist[last]
#             low,high=first,last
#             while low<high:
#                 while low<high and alist[low]<=mid_value:
#                     low+=1
#                 alist[high]=alist[low]
#                 while low<high and alist[high]>mid_value:
#                     high-=1
#                 alist[low]=alist[high]
#             alist[high]=mid_value
#             return low
            
        
#         def quick_select(alist,first,last,k):
#             m=quick_sort(arr,first,last)
#             if k<m:
#                 quick_select(alist,first,m-1,k)
#             elif k==m:
#                 return
#             else:
#                 quick_select(alist,m+1,last,k)
        
#         if k==0:
#             return []
#         if k>=len(arr):
#             return arr
#         quick_select(arr,0,len(arr)-1,k)
#         res=[]
#         for i in range(k):
#             res.append(arr[i])
#         return res

# if __name__=="__main__":
#     arr=[0,1,2,1]
#     a=Solution()
#     print(a.getLeastNumbers(arr,1))

# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         j,res,dic=-1,0,{}
#         for i in range(len(s)):
#             if s[i] in dic:
#                 j=max(dic[s[i]],j)
#             dic[s[i]]=i
#             res=max(res,i-j)
#         return res
# if __name__=="__main__":
#     a=Solution()
#     s="abcabcbb"
#     print(a.lengthOfLongestSubstring(s))


# class Solution:
#     def reversePairs(self, nums):
#         count=0
#         n=len(nums)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if nums[i]>nums[j]:
#                     count+=1
#         return count
# if __name__=="__main__":
#     a=Solution()
#     nums=[7,5,6,4]
#     print(a.reversePairs(nums))

# class Solution:
#     def reversePairs(self, nums):
#         n=len(nums)
#         tmp=[0]*n
#         return self.merge(nums,tmp,0,len(nums)-1)
#     def merge(self,nums,tmp,l,r):
#         if l>=r:
#             return 0
#         mid=l+(r-l)//2
#         res=self.merge(nums,tmp,l,mid)+self.merge(nums,tmp,mid+1,r)
#         i,j,pos=l,mid+1,l
#         while i<=mid and j<=r:
#             if nums[i]<=nums[j]:
#                 tmp[pos]=nums[i]
#                 i+=1
#             else:
#                 tmp[pos]=nums[j]
#                 j+=1
#                 res+=(mid-i+1)
#             pos+=1
#         for k in range(i,mid+1):
#             tmp[pos]=nums[k]
#             pos+=1
#         for k in range(j,r+1):
#             tmp[pos]=nums[k]
#             res+=(mid-i+1)
#             pos+=1
#         nums[l:r+1]=tmp[l:r+1]
#         return res
# if __name__=="__main__":
#     a=Solution()
#     nums=[7,5,6,4]
#     print(a.reversePairs(nums))

# class Solution:
#     def search(self, nums, target):
#         if target not in nums:
#             return 0
#         dic={}
#         for i in nums:
#             dic[i]=nums.count(i)
#         for k,v in dic.items():
#             if k==target:
#                 return v
# if __name__=="__main__":
#     a=Solution()
#     nums=[5,7,7,8,8,10]
#     target=9
#     print(a.search(nums,target))





# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def maxDepth(self, root):
#         if not root:
#             return 0
#         stack,p,count,max_value=[],root,1,1
#         while p or stack:
#             while p:
#                 stack.append(p)
#                 p=p.left
#                 count+=1
#             max_value=max(max_value,count)
#             cur=stack.pop()
#             count-=1
#             p=cur.right
#         return max_value


# if __name__=="__main__":
#     head=TreeNode(3)
#     head.left=TreeNode(1)
#     head.left.right=TreeNode(2)
#     head.right=TreeNode(4)
#     a=Solution()
#     print(a.maxDepth(head))


class Solution:
    def reverseWords(self, s):
        s=s.strip()
        res=[]
        i=j=len(s)-1
        while i>=0:
            while i>=0 and s[i]!=' ':
                i-=1
            res.append(s[i+1:j+1])
            while s[i]==' ':
                i-=1
            j=i
        return " ".join(res)
if __name__=="__main__":
    a=Solution()
    s="the sky is blue"
    print(a.reverseWords(s))
