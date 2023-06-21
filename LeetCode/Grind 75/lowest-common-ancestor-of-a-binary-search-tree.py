# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        My solution, 00:41:45 elapsed
        """
        def bs(start: 'TreeNode', target: int) -> List['TreeNode']:
            result = []

            while 1:  # p and q always exist
                result.append(start)

                if target == start.val:
                    return result
                elif target > start.val:  # go right
                    start = start.right
                else:  # go left
                    start = start.left

            return result

        p_visit = bs(root, p.val)
        q_visit = bs(root, q.val)

        pp = len(p_visit) - 1
        qp = len(q_visit) - 1

        while pp >= 0 and qp >= 0:
            if pp < qp:
                qp -= 1
            elif pp > qp:
                pp -= 1
            else:
                if p_visit[pp].val == q_visit[qp].val:
                    return p_visit[pp]

                pp -= 1
                qp -= 1

        return None

        """
        I misunderstood problem. LCA is not about val, just most closed common ancestor
        """
        # def bs(start: 'TreeNode', target: int) -> List[int]:
        #     result = []

        #     while 1: # p and q always exist
        #         result.append(start)

        #         if target == start.val:
        #             return result
        #         elif target > start.val: # go right
        #             start = start.right
        #         else: # go left
        #             start = start.left

        #     return result

        # p_visit = bs(root, p.val)
        # q_visit = bs(root, q.val)

        # p_dict = {}
        # for x in p_visit:
        #     p_dict[x.val] = True

        # min_node = q_visit[0]

        # for x in q_visit:
        #     if x.val in p_dict:
        #         if min_node.val > x.val:
        #             min_node = x

        # return min_node
