# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
print(Solution().deleteDuplicates([1,1,2]))
print(Solution().deleteDuplicates(ListNode([1,1,2]).__dict__['next']))
print(Solution().deleteDuplicates([1,1,2,3,3]))