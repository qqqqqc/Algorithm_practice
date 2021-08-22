# 删除链表倒数第k个结点


class Node():
    def __init__(self,val):
        self.data = val
        self.next = None


class Solution():
    # 第一种方法 先让快指针走k   然后快慢指针一起走，当快指针走到链表尽头结点时，慢指针的下一个节点就是要删除的结点
    # def remove_list_reserve_k_node(self,node,k):
    #     if node is None:
    #         return node
    #     else:
    #         p = q = node
    #         for i in range(k):
    #             p = p.next
    #         if not p:
    #             return node.next
    #
    #         while p.next:
    #             p = p.next
    #             q = q.next
    #         q.next = q.next.next
    #         return node
    # 第二种方法  使用字典记录
    def remove_list_reserve_k_node(self,node,k):
        if node is None:
            return node
        else:
            d = {}
            i = 0
            cur = node
            while cur:
                d[i] = cur
                cur = cur.next
                i += 1
            if i == k:
                return node.next
            elif k == 1:
                d[i-k-1].next = None
            else:
                d[i-k-1].next = d[i-k+1]
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
res = s.remove_list_reserve_k_node(node,7)
while res:
    print(res.data)
    res = res.next