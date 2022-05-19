# 二叉树的遍历
# 包括深度和广度
# 深度包括前序(根左右)中序(左根右)后序(左右根)



class Node():
    def __init__(self,data):
        self.root = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None


    def add(self,i):
        """
        二叉树层级添加节点
        :param i: 需要添加节点的值
        :return:
        """
        node = Node(i)
        if self.root is None:
            self.root = node
            return
        else:
            queue = [self.root]
            while queue:
                cur = queue.pop(0)
                if cur.left is None:
                    cur.left = node
                    return
                else:
                    queue.append(cur.left)
                if cur.right is None:
                    cur.right = node
                    return
                else:
                    queue.append(cur.right)

    def level_travel(self):
        if self.root is None:
            return
        else:
            res = []
            queue = [self.root]
            while queue:
                tmp = []
                res.append([node.root for node in queue])
                for node in queue:
                    if node.left is not None:
                        tmp.append(node.left)
                    if node.right is not None:
                        tmp.append(node.right)
                queue = tmp

            return res

    def preorder_travel(self,node):
        if node is None:
            return
        else:
            res = []
            queue = [node]
            while queue:
                cur = queue.pop()
                if cur.right is not None:
                    queue.append(cur.right)
                if cur.left is not None:
                    queue.append(cur.left)
                res.append(cur.root)
            return res

    def inorder_travel(self,node):
        if node is None:
            return node
        else:
            res = []
            queue = [node]
            node_type = type(node)
            while queue:
                cur = queue.pop()
                if type(cur) != node_type:
                    res.append(cur)
                    continue
                if cur.right is not None:
                    queue.append(cur.right)
                queue.append(cur.root)
                if cur.left is not None:
                    queue.append(cur.left)
            return res

    def postorder_travel(self,node):
        if node is None:
            return node
        else:
            res = []
            queue = [node]
            node_type = type(node)
            while queue:
                cur = queue.pop()
                if type(cur) != node_type:
                    res.append(cur)
                    continue
                queue.append(cur.root)
                if cur.right is not None:
                    queue.append(cur.right)
                if cur.left is not None:
                    queue.append(cur.left)
            return res

b = BinaryTree()
for i in range(10):
    b.add(i)

print(b.level_travel())
print(b.preorder_travel(b.root))
print(b.inorder_travel(b.root))
print(b.postorder_travel(b.root))