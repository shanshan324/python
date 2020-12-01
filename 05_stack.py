#这里用列表实现，列表是顺序表

class Stack(object):
    """栈"""
    def __init__(self):
        """构造一个容器"""
        self.__list = []


    def push(self,item):
        """添加一个新的元素item到栈顶"""
        self.__list.append(item)  #尾部追加


    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()


    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            """判断列表是否为空"""
            return self.__list[-1]  #-1表示返回最后一个元素
        else:
            return None


    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []
        # return not self.__list
        # 0,(),[],{}逻辑值上可以判断为假


    def size(self):
        """返回栈的元素"""
        return len(self.__list)



if __name__ == "__main__":
    s = Stack()  #实例化，使用的时候需要构造栈的对象
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())