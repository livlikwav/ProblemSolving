# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        MY SOLUTION, 12min elapsed
        조심해야할 것!! 엣지 케이스를 조심해야한다. head == None 을 submit 하기 전에 빼먹었다. 이런건 자주있는 일이니 잘 생각하자.

        문제 조건에 SC O(1), constant memory 가 있길래 오히려 힌트가 되었다.
        LinkedList 내 노드의 갯수가 10^4 개 미만 이므로 계속 cycle 내에서 돌리더라도 10^4 개 이상되면 return 하도록 시간 제한 내에 가능했다. (대부분 1초니까)

        평범한 방법으로는, Linked List 는 directed graph 이므로, DAG 를 판단하는데는 dfs 를 사용할 수 있다.
        Linked List 는 한 방향으로만 가므로, 더 간단할 것이었고, visited 에 val 을 저장해서, vistied == True 인데 Next 가 가리키면 cyclic 이라고 판단할 수 있다.
        """
        limit = int(1e4)
        cnt = 0

        if head == None:
            return False

        while head.next:
            cnt += 1
            if cnt >= limit:
                return True

            head = head.next

        return False
        """
        Voted #2 (#1 은 이상하다; pos 숨겨놓은거를 file open 으로 열어서 푼다)
        """
        # dictionary(HashMap) 사용: head 를 그냥 그대로 넣은게 인상깊다. 상관 없긴 하다.
        dictionary = {}
        while head:
            if head in dictionary:
                return True
            else:
                dictionary[head] = True
            head = head.next
        return False
        # two pointers: 음... 이건 좋은 방법인지 모르겠다. slow 랑 fast 2개 두고, 싹 돌려서 두 개 같은 경우=Cycle 찾는것 같은데 내 cnt 방법이 나은듯.
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        """
        Voted #3 근데 two pointers 라는 방법이 알고리즘 이름도 있나봐. 토끼와 거북이 알고리즘이네 ㅋㅋ
        single pointer 방법도 재미있다. val 에 None 으로 표시하는 방법이다.
        """
        # Approach 2 slow and fast pointers slow moves one step at a time, fast moves 2, if they ever meet, means there was a cycle,
        # Time -O(n), Space- O(1)
        # Floyd's Tortoise and Hare Algorithm
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        # Approch 3 single pointer, marking nodes as visited, makes use of fact that node value's are not None
        # Time -O(n), Space- O(1)
        slow = head
        while slow:
            if slow.val == None:
                # This was already visited
                return True
            slow.val = None  # a way to mark visited
            slow = slow.next
        return False
