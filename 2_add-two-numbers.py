# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_number, l2_number = 0, 0
        l1_current, l2_current = l1, l2
        digit = 0
        while(l1_current != None):
            l1_number += l1_current.val * 10 ** digit
            digit += 1
            l1_current = l1_current.next

        digit = 0
        while (l2_current != None):
            l2_number += l2_current.val * 10 ** digit
            digit += 1
            l2_current = l2_current.next

        summation = l1_number + l2_number
        digit_list = []
        while( summation != 0):
            most_significant = summation % 10
            digit_list.append(most_significant)
            summation  = summation // 10

        if len(digit_list) == 0:
            digit_list.append(0)

        start_ListNode = ListNode(digit_list[0])
        current_ListNode = start_ListNode

        for i in digit_list[1:]:
            current_ListNode.next = ListNode(i)
            current_ListNode = current_ListNode.next
        return start_ListNode




solution = Solution()
print(solution.addTwoNumbers(ListNode(0), ListNode(0)))