class Queue(object):
    """队列"""
    def __init__(self):
        #构造容器，存储数据
        self.__list = []

    def enqueue(self,item):
        """往队列中添加一个item的元素"""
        self.__list.append(item)
    
    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列大小"""
        return len(self.__list)

if __name__ == "__main__":
    s = Queue()  #实例化，使用的时候需要构造栈的对象
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())