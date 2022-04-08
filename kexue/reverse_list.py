# *_* coding=utf-8 *_*

'''
反转链表：
https://leetcode-cn.com/problems/reverse-linked-list/

实现了一个链表；并且用 迭代/递归 两种方法进行反转。

1. 迭代：时间复杂度 O(N)  空间复杂度 O(1)
2. 递归：时间复杂度 O(N)  空间复杂度 O(N)

'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList(object):
    # 通过一个list 初始化一个链表
    def __init__(self, l=[1, 2, 3, 4, 5, 6]):
        self.head = ListNode(l[0])
        cur = self.head
        for i in l[1:]:
            cur.next = ListNode(i)
            cur = cur.next
    
    def print_linked_list(self):
        # 为了保持链表 head 不被破坏
        temp_head = self.head
        while temp_head:
            print(temp_head.val)
            temp_head = temp_head.next


class Solution(object):
    # 遍历方式反转链表
    def reverse_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, pre = head, None
        while cur:
            # pre, pre.next, cur = cur, pre, cur.next
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    # 递归方式反转链表
    def reverse_list_recursion(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head
        node = self.reverse_list_recursion(head.next)
        head.next.next = head
        head.next = None
        return node


if __name__ == '__main__':
    ll = LinkedList(l=[1, 2, 3, 4, 5])
    print('------------------------------')
    print('before reverse')
    ll.print_linked_list()
    h = ll.head
    s = Solution()
    ll.head = s.reverse_list(h)
    print('------------------------------')
    print('after reverse: reverse_list()')
    ll.print_linked_list()
    print('------------------------------')
    ll.head = s.reverse_list_recursion(ll.head)
    print('after reverse: reverse_list_recursion()')
    ll.print_linked_list()

