class Solution:
    def isValid(self, s: str) -> bool:
        # First solution by me
        left_stack = []
        d = {
            "(": 1,
            ")": -1,
            "[": 2,
            "]": -2,
            "{": 3,
            "}": -3,
        }

        for i in range(len(s)):
            val = d[s[i]]
            if val < 0:  # right
                if len(left_stack) == 0:  # left stack is empty
                    return False

                if left_stack.pop() + val != 0:  # diff pair
                    return False
            else:  # left
                left_stack.append(val)

        if len(left_stack) > 0:
            return False  # left is not empty

        return True

# Hot solution 1 by same idea but easy implementation
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for char in s:
#             if char == '(' or char == '{' or char == '[':
#                 stack.append(char)
#             else:
#                 if not stack:
#                     return False
#                 if char == ')' and stack[-1] == '(':
#                     stack.pop()
#                 elif char == '}' and stack[-1] == '{':
#                     stack.pop()
#                 elif char == ']' and stack[-1] == '[':
#                     stack.pop()
#                 else:
#                     return False
#         return not stack
