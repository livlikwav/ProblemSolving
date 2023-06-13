# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    FAIL-23-06-14
    python 의 기초를 몰라서 틀렸다. python 은 pointer 가 없다.
    python 은 모든게 object 이다. 모든 object 는 mutable 이거나 immutable 이다.
    python 은 variable 이 없고 name 만 있을 뿐이다.
    문제 자체는 어렵지 않았다. merge sort 가 생각나는 문제.
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        x, y = list1, list2
        node = result = ListNode()

        while x != None and y != None:
            if x.val < y.val:
                node.next = x
                node = x
                x = x.next
            else:
                node.next = y
                node = y
                y = y.next

        if x == None:
            while y != None:
                node.next = y
                node = y
                y = y.next

        if y == None:
            while x != None:
                node.next = x
                node = x
                x = x.next

        return result.next

        # hot 1 solution
        cur = dummy = ListNode()
        while list1 and list2:  # 해당 pyobject 가 None 인지 이러한 문법으로 확인할 수 있다.
            if list1.val < list2.val:
                cur.next = list1
                # tuple 으로 우변이 먼저 evaluate 되고 할당되므로 이러한 문법이 가능하다.
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            # 이렇게 None 이 아닌걸 넣는것도 oneline if statement 로 가능하다.
            cur.next = list1 if list1 else list2

        return dummy.next
