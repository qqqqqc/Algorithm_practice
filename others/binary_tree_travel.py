# 描述
# 根据给定的二叉树结构描述字符串，输出该二叉树按照中序遍历结果字符串。中序遍历顺序为:左根右
# 注意
# 1.字母待变节点值，左右括号内包含该节点的子节点
# 2.左右子节点使用括号分隔，逗号前为空则表示左子节点为空，没有逗号则表示右子节点为空
# 3.二叉树的节点树不超过100
# 输入"a{b{d,e{g,h{,l}}},c{f}}" 为了方便处理，代码中直接写死为字符串
# 输出 dbgehlafc

class Node():
    def __init__(self,data):
        self.root = data
        self.left = None
        self.right = None


def get_node(node):
    if type(node) == Node:
        return node
    elif node:
        return Node(node)
    else:
        return None

def get_root(stack):
    j = len(stack) - 1
    while j >= 0:
        if stack[j] == "{":
            break
        j -= 1

    if stack[j:][1] == ",":
        left_ = None

    else:
        left_ = get_node(stack[j:][1])

    if stack[j:][-1] == "," or "," not in stack[j:]:
        right_ = None
    else:
        right_ = get_node(stack[j:][-1])

    stack = stack[:j]
    root_ = get_node(stack.pop())
    root_.left = left_
    root_.right = right_
    stack.append(root_)
    return stack

tree = "a{b{d,e{g,h{,l}}},c{f}}"
stack = []

for t in tree:
    if t == "}":
        stack = get_root(stack)
    else:
        stack.append(t)


queue = [stack[0]]
res = []
tree_type = type(stack[0])
while queue:
    cur = queue.pop()
    if type(cur) != tree_type:
        res.append(cur)
        continue
    if cur.right is not None:
        queue.append(cur.right)
    queue.append(cur.root)
    if cur.left is not None:
        queue.append(cur.left)

print("".join(res))