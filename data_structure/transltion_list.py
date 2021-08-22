# 链表向右平移n个位置



class Node():
    def __init__(self,val):
        self.data = val
        self.next = None

class Solution():
    def transltion_list(self,node,n):
        if node is None:
            return node
        else:
            i = 1
            cur = node
            while cur.next:
                i += 1
                cur = cur.next
            cur.next = node
            n = n % i
            while n:
                cur = cur.next
                node = node.next
                n -= 1
            cur.next = None
            return node

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
s = Solution()
res = s.transltion_list(node,4)
while res:
    print(res.data)
    res = res.next