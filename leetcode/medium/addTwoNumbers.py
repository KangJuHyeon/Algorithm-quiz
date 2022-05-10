# 문제 해결 방법
# Linked List python 구현 부분을 많이 보고 따라해보려고 노력
# 입력 값을 for문으로 뽑아보려고 했지만, 아니였음

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_value = 0
        l2_value = 0

        num = 1
        while l1:
            l1_value += l1.val * num
            l1 = l1.next
            num *= 10
        
        num = 1
        while l2:
            l2_value += l2.val * num
            l2 = l2.next
            num *= 10

        out_value = l1_value + l2_value

        header = None
        linked_list = None
        for c in str(out_value):
            if not header:
                header = ListNode(int(c))
                linked_list = header
            else:
                curNode = ListNode(int(c), linked_list)
                linked_list = curNode

        return linked_list
print(Solution().addTwoNumbers([2,4,3], [5,6,4]))
