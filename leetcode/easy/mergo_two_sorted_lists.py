from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode():
        print("list1", list1)
        print("list2", list2)
        head = ListNode(-1)
        cursor = head

        while list1 != None and list2 != None:
            print("list1.val", list1.val)
            print("list2.val", list2.val)
            if list1.val <= list2.val:
                cursor.next = list1 # Update next node
                list1 = list1.next # Update list1
            else:
                cursor.next = list2 # Update next node
                list2 = list2.next # Update list2

            cursor = cursor.next # Move cursor

        # Last node
        if list1 != None:
            cursor.next = list1
        else:
            cursor.next = list2
        return head.next

print(Solution().mergeTwoLists(ListNode([1,2,4]), ListNode([1,3,4])))