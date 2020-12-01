class Node(object):
    """构造节点"""
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    """二叉树"""
    def __init__(self):
        # 构造一个根节点
        self.root = None
    
    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        # 队列存放的就是要处理、遍历的数据
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)


    def preorder(self,node):
        """先序遍历：根-左-右
            node指的根节点
        """
        if node is None:
            return
        # 打印根节点的元素
        print(node.elem,end=" ")
        # 遍历左边的子树
        self.preorder(node.lchild)
        # 遍历右边的子树
        self.preorder(node.rchild)


    def inorder(self,node):
        """中序遍历：左-根-右
            node指的根节点
        """
        if node is None:
            return
        # 遍历左边的子树
        self.inorder(node.lchild)
        # 打印根节点的元素
        print(node.elem,end=" ")
        # 遍历右边的子树
        self.inorder(node.rchild)


    def postorder(self,node):
        """后序遍历：左-右-根
            node指的根节点
        """
        if node is None:
            return
        # 遍历左边的子树
        self.postorder(node.lchild)
        # 遍历右边的子树
        self.postorder(node.rchild)
        # 打印根节点的元素
        print(node.elem,end=" ")   



if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")
    tree.preorder(tree.root)
    print(" ")
    tree.inorder(tree.root)
    print(" ")
    tree.postorder(tree.root)