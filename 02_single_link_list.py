"""
单链表
"""
class Node():
    """节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None

    
class SingleLinkLsit():
    """单链表"""
    def __init__(self,node=None):
        self.__head = node      #__a表示私有变量
    
    def is_empty(self):
        """链表是否为空"""
        return(self.__head==None)

    def length(self):
        """链表长度"""    #指存在多少个节点
        #cur游标，用来移动遍历节点，有遍历说明需要用到游标
        cur = self.__head
        #count记录数量
        count = 0
        while cur !=None:
            count +=1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur !=None:
            print(cur.elem,end=" ")
            cur = cur.next   #cur.next指的是下一个节点
        print("")  #换行
    
    def add(self,item):
        """链表头部添加元素，头插法"""  #有一个先后顺序，必须先让新节点的next指向原节点的elem，再将head指向新节点的elem
        node = Node(item)
        node.next = self.__head       #新节点的next指向head原本指向的节点
        self.__head = node
    
    def append(self,item):   #item指的是具体的数据，并不是节点
        """链表尾部添加元素，尾插法"""
        node = Node(item)    #构造节点，把数据放进去
        if self.is_empty():
            self.__head =node
        # if self.__head == None:
            """判断是否为空链表"""
        else:
            cur = self.__head
            while cur.next !=None:
                cur = cur.next
            cur.next = node


    def insert(self,pos,item):
        """指定位置添加元素
        :param post 
        """
        if pos <=0:
            self.add(item)    #在头部添加节点，使用头插法
        elif pos > (self.length()-1): 
            self.append(item) #在尾部添加节点，使用尾插法
        else:
            pre =self.__head  #python中等号表示指向，先处理=右边，self.__head这个变量所指向的是第一个节点，现在相当于把这个节点的位置赋值给pre
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            """
            分两步，先让node区域的next指向pre.next指向的区域，再让pre.next指向node
            node.next表示node这个节点的next区域
            pre.next表示pre这个游标指向的这个节点的next区域
            在python中"="理解为“指向”
            """
            node.next = pre.next
            pre.next = node
            


    def remove(self,item):
        """删除节点"""
        #用两个游标的写法
        pre = None
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                #先判断此节点是否是头节点
                #头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next
        # # #用一个游标的写法
        # # pre.next = pre.next.next
        # pre = self.__head
        # while pre !=None:
        #     if pre.elem == item:
        #         pre.next = pre.next.next
        #     else:
        #         pre = pre.next

    def search(self,item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__=="__main__":   #当前模块作为主程序运行时，执行if后的代码
    ll=SingleLinkLsit()
    # print(ll.is_empty())
    # print(ll.length())

    ll.append(1)
    # print(ll.is_empty())
    # print(ll.length())

    ll.append(2)
    # ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    # ll.insert(-1,9)   # 9 8 1 2 3 4 5 6
    # ll.travel()
    ll.insert(3,100)  # 9 8 1 100 2 3 4 5 6
    ll.travel()
    # ll.insert(10,200) # 9 8 1 100 2 3 4 5 6 200
    # ll.travel()



