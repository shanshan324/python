class Node(object):
    """节点"""
    def __init__(self,item):
        self.elem = item
        self.next = None
        self.prev = None

class Doublelinklist(object):
    """双链表"""
    def __init__(self,node=None):
        self.__head = node      #__a表示私有变量
    
    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

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
        node.next.prev = node
        #上两行代码也可以改变一下执行顺序
        #self.__head.prev = node
        #self.__head = node
    
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
            node.prev = cur


    def insert(self,pos,item):
        """指定位置添加元素
        :param post 
        """
        if pos <=0:
            self.add(item)    #在头部添加节点，使用头插法
        elif pos > (self.length()-1): 
            self.append(item) #在尾部添加节点，使用尾插法
        else:
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            #当循环退出后，cur指向pos位置
            node = Node(item)
            node.next = cur
            node.prev = cur.prev

            cur.prev.next = node
            cur.prev = node
            #上两行代码还可以写成
            #cur.prev = node
            #node.prev.next = node


    def remove(self,item):
        """删除节点"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                #先判断此节点是否是头节点
                #头节点
                if cur == self.__head: #代表第一个节点
                    self.__head = cur.next
                    if cur.next: 
                        #判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
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


if __name__=="__main__":
    dll = Doublelinklist()
    print(dll.is_empty())
    print(dll.length())

    dll.append(1)
    print(dll.is_empty())
    print(dll.length())

    dll.append(2)
    dll.add(8)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    # 8 1 2 3 4 5 6
    dll.insert(-1,9)   # 9 8 1 2 3 4 5 6
    dll.travel()
    dll.insert(3,100)  # 9 8 1 100 2 3 4 5 6
    dll.travel()
    dll.insert(10,200) # 9 8 1 100 2 3 4 5 6 200
    dll.travel()
    dll.remove(5) # 9 8 1 100 2 3 4 5 6 200
    dll.travel()
 
