from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
        else:
            return False



head = [3,2,0,-4]
pos = 1
