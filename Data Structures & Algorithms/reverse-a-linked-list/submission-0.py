# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev_node = None # None
        curr_node = head # 0
        next_node = head.next # 1

        while next_node is not None:
            curr_node.next = prev_node # 0 -> None, 1->0->None, 2->1->0->None
            prev_node = curr_node # 0 -> None, 1->0->None, 2->1->0->None
            curr_node = next_node # 1->2->3->None, 2->3->None, 3->None
            next_node = next_node.next #2->3->None, 3->None, None
        curr_node.next = prev_node
        return curr_node
        