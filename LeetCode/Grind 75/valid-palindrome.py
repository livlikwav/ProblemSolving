class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        My solution (but 2 loop)
        """
        s = s.lower()
        p = ""
        for i in range(0, len(s)):
            if s[i].isalnum() and not s[i] == " ":
                p += s[i]

        for i in range(0, len(p)):
            j = len(p) - i - 1

            if p[i] != p[j]:
                return False

        return True
        """
        Two lines pythonic solution
        """
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]
        """
        Two pointer and optimization
        """
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i, j = i+1, j-1
        return True
