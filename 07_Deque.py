class Deque(object):
    """双端队列"""
    def __init__(self):
        #构造容器，存储数据
        self.__list = []

    def add_front(self,item):
        """从头部添加一个item的元素"""
        self.__list.insert(0,item)

    def add_rear(self,item):
        """从尾部添加一个item的元素"""
        self.__list.insert(0,item)
    
    def pop_front(self):
        """从头部删除一个元素"""
        return self.__list.pop(0)

    def pop_rear(self):
        """从尾部删除一个元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列大小"""
        return len(self.__list)

if __name__ == "__main__":
    s = Deque()  #实例化，使用的时候需要构造栈的对象
