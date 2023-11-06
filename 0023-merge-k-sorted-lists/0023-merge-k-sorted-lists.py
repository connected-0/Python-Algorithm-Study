# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        flat_list=[]
        for linked_list in lists:
            while linked_list:
                flat_list.append(linked_list.val)
                linked_list=linked_list.next

        flat_list.sort()

        dummy_head=ListNode(0)
        current=dummy_head
        for val in flat_list:
            current.next=ListNode(val)
            current=current.next

        return dummy_head.next
