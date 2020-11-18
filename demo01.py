#!/usr/bin/python
# -*-coding:utf-8 -*-
 
import copy
a = [1, 2, 3, 4, ['a', 'b']] #原始对象
 
b = a                       #赋值，传对象的引用
c = copy.copy(a)            #对象拷贝，浅拷贝
d = copy.deepcopy(a)        #对象拷贝，深拷贝
 
a.append(5)                 #修改对象a
a[4].append('c')            #修改对象a中的['a', 'b']数组对象
 
print( 'a = ', a )
print( 'b = ', b )
print( 'c = ', c )
print( 'd = ', d )



import copy

# lis = [12,39,10,5,11,66]  #一维列表
# lis.append(['I','like','python'])  #添加 ['I','like','python']
# li = copy.copy(lis)  #浅度拷贝
# print(lis)  #输出：[12,39,10,5,11,66,['I','like','python']]   变成一个二维列表
# lis[6][2] = 'you'  
# lis[1]=00
# print(lis)  #[12,0,10,5,11,66,['I','like','you']]
# print(li)   #[12,39,10,5,11,66,['I','like','you']]


lis = [12,39,10,5,11,66]  #一维列表
lis.append(['I','like','python'])  #添加 ['I','like','python']
# li = lis.copy()  #浅拷贝
li2 = copy.deepcopy(lis)  #深拷贝
print(lis)  #输出：[12,39,10,5,11,66,['I','like','python']]   变成一个二维列表
lis[6][2] = 'you'  
lis[1]=00
print(lis)  #[12,0,10,5,11,66,['I','like','you']]   原列表
# print(li)   #[12,39,10,5,11,66,['I','like','you']]   浅拷贝后得到的列表
print(li2)   #[12, 39, 10, 5, 11, 66, ['I', 'like', 'python']]   深度拷贝后得到的列表





# a = [1, 2, 3, 4]
# for x in a:
#     a.remove(x)
# print(a)
 
# b = [1, 2, 3, 4]
# for i in b:
#     b.pop()
# print(b)
 
# c = [1, 2, 3, 4]
# for i in range(len(c)):
#     del c[0]
# print(c)

#字符串转数组
str1 = '1,2,3'
arr = str1.split(',')
arr1=list(str1)
print(arr)
print(arr1)

#数组转字符串
arr = ['a','b']
str2 = ','.join(arr)
print(str2)

"""
lstrip() 方法用于截掉字符串左边的空格或指定字符。
"""


"""
reverse()
python中列表的内置方法，用于列表中数据的反转
比如4321->1234
"""

# #递归代码模板
# def recursion(level,param1,param2):
#     #recursion terminator
#     #递归终止条件
#     if level>MAX_LEVEL:
#         process_result
#         return
    
#     #process logic in current level
#     #处理当前层逻辑
#     process(level,data...)

#     #drill down
#     #下一层
#     self.recursion(level+1,p1)

#     #reverse the current level status if needed


"""
剪绳子
基础知识：
N>0, N=n1+n2+...+nk
1. 假设ni>=5,3*(ni-3)>=ni?
    3ni-9>=ni?
    2ni>=9?
2. ni=4,4=2*2
3. 2*2*2<3*3（即最多有两个2，3尽可能多）
利用 n%3 取余==1 2 0
"""


"""
转化为位运算：
1. 向下取整n//2 等价于 右移一位n<<1
2. 取余数n%2 等价于 判断二进制最右一位值是否为1 n&1
"""


"""
10**n 即10的n次方
"""


"""
正则表达式匹配
用动态规划的方法求解
状态表示：f[i][j] 表示s[i,...]和p[j,...]相匹配

状态转移：
1. p[j]是正常字符，f[i][j]= s[i]==p[j]&&f[i+1][j+1]
2. p[j]是'.',f[i][j]=f[i+1][j+1]
3. p[j]是'*',f[i][j]=f[i][j+2]||f[i+1][j]

f[n][m]=true
"""