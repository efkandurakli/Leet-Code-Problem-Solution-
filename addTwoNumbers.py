# Definition for singly-linked list.

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

    def get_val(self):
        return self.val

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next




class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_to_head(self, value):
        new_node = ListNode(value)
        new_node.set_next(self.head)
        self.head = new_node


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """ :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current = l1
        factor = 1
        value = 0
        while (current != None):
            value += current.val * factor
            current = current.next
            factor *= 10

        factor = 1
        current = l2
        while (current != None):
            value += current.val * factor
            current = current.next
            factor *= 10

        retList = ListNode(value % 10)
        current = retList

        while (value >= 10):
            value /= 10
            current.next = ListNode(value % 10)
            current = current.next

        return retList



sol = Solution()


list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(3)

list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)


retList = sol.addTwoNumbers(list1,list2)

current = retList

while (current != None):
    print(int(current.val))
    current = current.next

