# 链表倒叙

class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

def solution(node):
    if node is None:
        return
    else:
        next = node #用来保存待反序的第一个节点
        pre = node  #用来保存已经反序的第一个节点
        while node:
            next = node.next
            node.next = pre
            pre = node
            node = next
        return pre






# 递归

def sloution_recursion(node):
    if node is None:
        return
    if node.next is None:
        return node
    head = sloution_recursion(node.next)
    node.next.next = node.next
    node.next = None
    return head