# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        lis = []
        while head:
            lis.append(head.val)
            head=head.next
        maxi = 0
        for i in range(len(lis)//2):
            if (lis[i]+lis[-1-i])>maxi:
                maxi = lis[i]+lis[-1-i]
        return maxi
