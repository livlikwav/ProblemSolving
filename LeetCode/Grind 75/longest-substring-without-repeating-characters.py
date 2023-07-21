class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Voted#1
        IDEA: seen[char] = index
        -> when exist update left to seen_index + 1
        """
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            if s[r] not in seen:
                output = max(output, r - l + 1)
            else:
                if seen[s[r]] < l:
                    output = max(output, r - l + 1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output
        """
        My Solution: sliding window but brutal force
        left pointer be incremented just 1 by 1 sequentially
        and check uniqueness brute-force-likely
        """
        i, j = 0, 0
        d = {}
        result = 0
        current = 0

        while j < len(s):
            # print(s[i:j+1])
            d = {}
            isUnique = True
            for x in range(i, j + 1):
                if s[x] not in d:
                    d[s[x]] = 1
                else:
                    isUnique = False
                    break

            if isUnique:
                current = j - i + 1
                result = max(result, current)
                j += 1
            else:
                j += 1
                i += 1

        return result
