class ListNode:
    def __init__(self, x):
        self.val  = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        # Need a pivot
        current = head # input
        while current:
            runner = current.next
            while runner and current.val == runner.val: # Only duplicated node
                runner = runner.next # Remove it
            current.next = runner
            current = runner
        return head

"""
Runtime: 32 ms, faster than 96.33% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List.
"""
