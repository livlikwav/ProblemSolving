# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### Voted #2
    # 이게 내가 원하던 코드 같다. 제일 간결하다. if 문을 줄이고 one liner 를 잘 사용했다. 아이디어는 완전 동일하다.
    # 그리고 Tree depth 구하는 depth() 함수 잘 봐둬야겠다. 제일 간결하고 명확하다. max(left, right) + 1 이다.
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        l = self.depth(root.left)
        r = self.depth(root.right)
        return (
            (abs(l - r) < 2)
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def depth(self, node):
        if node == None:
            return 0
        return max(self.depth(node.left), self.depth(node.right)) + 1

    ### Voted #1
    # 나랑 핵심 아이디어는 동일하다. balanced binary tree 정의 그대로 구현했다.
    # 단, unbalanced 를 찾으면 빨리 종료하도록, 그리고 코드를 간결하게 구현했다.
    # Height() 라고 하지만, 해당 코드 내에 isBalanced 개념이 들어있어서 클린 코드 관점에서는 잘 모르겠다.
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.Height(root) >= 0

    def Height(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
            return -1
        return max(leftheight, rightheight) + 1

    ### THIRD SOLUTION
    # recursive 하게 구현했다가 function call stack 넘어갈까봐 stack bfs 로 다시 구현해봄
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bfs(subtree: Optional[TreeNode]) -> int:
            if subtree == None:
                return 0
            if subtree.left == None and subtree.right == None:
                return 1

            stack = []
            if subtree.left != None:
                stack.append((2, subtree.left))
            if subtree.right != None:
                stack.append((2, subtree.right))

            max_val = -1
            while stack:
                h, node = stack.pop()
                max_val = max(max_val, h)

                if node.left != None:
                    stack.append((h + 1, node.left))
                if node.right != None:
                    stack.append((h + 1, node.right))
            return max_val

        def is_balanced(subtree: Optional[TreeNode]) -> bool:
            if subtree == None:
                return True
            if abs(bfs(subtree.left) - bfs(subtree.right)) >= 2:
                return False

            return is_balanced(subtree.left) and is_balanced(subtree.right)

        return is_balanced(root)

        ### SECOND SOLUTION
        # 사실 반쯤 실패한 풀이이다. TC, SC 를 고려하지 않고 구현했다. Submit 하고 기도 메타를 시전했다.
        # 최악의 경우를 완전 이진 트리라고 생각하고, 매번 대략 5000개 모든 노드 탐색해서 height 구한다고 가정하면
        # O(N^2) 으로 보인다. (height 가 O(N) 이고, is_balanced 가 모든 노드에 대해서 반복하니까)
        # 다행히 call stack 이 넘치지 않았다. height 구하는 코드는 bfs 의 stack 구현법으로 변경 가능할 것 같다.
        #
        # 처음 구현한 코드는 실패했다. 모든 node 에 대해서 balanced 를 만족해야한다는 조건을 구현하지 않아서이다.
        # 이것은 balanced binary tree (= is height balanced) 의 개념을 확실히 이해하지 않았었기 때문이다.
        def height(subtree: Optional[TreeNode]) -> int:
            if subtree == None:
                return 0
            if subtree.left == None and subtree.right == None:
                return 1

            return 1 + max(height(subtree.left), height(subtree.right))

        def is_balanced(subtree: Optional[TreeNode]) -> bool:
            if subtree == None:
                return True
            if abs(height(subtree.left) - height(subtree.right)) >= 2:
                return False

            return is_balanced(subtree.left) and is_balanced(subtree.right)

        return is_balanced(root)

        ### FIRST FAILED SOLUTION (GREEDY 이거나, D&C 가 아닌 또 법칙을 찾으려고 하는 실수를 범했다.)
        # if root == None:
        #     return True

        # min_val = int(1e9)
        # max_val = -1
        # q = [(1, root)] # height, node

        # while q:
        #     height, node = q.pop()

        #     if node.left == None and node.right == None: # is leaf
        #         min_val = min(min_val, height)
        #         max_val = max(max_val, height)
        #         continue

        #     if node.left != None:
        #         q.append((height + 1, node.left))
        #     if node.right != None:
        #         q.append((height + 1, node.right))
        # print(min_val, max_val)
        # if max_val - min_val < 2:
        #     return True
        # return False
