# 判断链表是否有环

# 快慢指针法


class Node():
    def __init__(self,val):
        self.data = val
        self.next = None

class Solution():
    def is_loop(self, node):
        is_loop = False
        if node is None:
            return
        else:
            p = q = node
            while p.next is not None and p.next.next is not None:
                p = p.next.next
                q = q.next
                if p == q:
                    print("有环")
                    is_loop = True
                    break
            if is_loop:
                cur = node
                while cur != p:
                    p = p.next
                    cur = cur.next
                return cur
            else:
                print("无环")
                return False

node = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
node5 = Node(6)
node6 = Node(7)

node.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
# node6.next = node3
s = Solution()

res = s.is_loop(node)
if res:
    print(res.data)