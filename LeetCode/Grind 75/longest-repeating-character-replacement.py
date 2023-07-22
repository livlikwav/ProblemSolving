class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Voted #1 아이디어 자체는 나랑 동일하다!
        IDEA #1: 매번 sliding window 를 새로 계산하지 말고, dictionary 를 pointer 변화에 따라 업데이트하는게 시간 복잡도 면에서 효율적이다.
        IDEA #2: 굳이 모든 char 의 frequency 를 저장하지 않고, right - left + 1 해도 되었다.

        꿀팁: Python defaultdict 안쓰고 직접 not in 체크 후 초기화 할 때,
        나처럼 if-else 로 문장 3개 쓰지 말고, if not in 하면 그냥 0 으로 초기화하는게 더 간단해보이네!
        """
        l = 0
        c_frequency = {}
        longest_str_len = 0
        for i in range(len(s)):
            if not s[r] in c_frequency:
                c_frequency[s[r]] = 0
            c_frequency[s[r]] += 1

            # Replacements cost = cells count between left and right - highest frequency
            cells_count = r - l + 1
            if cells_count - max(c_frequency.values()) <= k:
                longest_str_len = max(longest_str_len, cells_count)
            else:
                c_frequency[s[l]] -= 1
                if not c_frequency[s[l]]:
                    c_frequency.pop(s[l])
                l += 1
        return longest_str_len
        """
        Voted #3 신기한 구현법
        꿀팁 #1: enumerate() 를 쓰면 idx, val 이라서 좀 더 편할지도
        꿀팁 #2: dictionary.get(key, default) 인가보다. 이것도 쓰기 편하다.
        아이디어 #1: window 자체를 저장할 필요도 없다. j 는 계속 앞으로 가는거고 i 만 빼거나 냅두거나 니까.
        """
        d = {}
        window = 0

        for i, char in enumerate(s):
            d[char] = d.get(char, 0) + 1
            if window + 1 - max(d.values()) <= k:
                window += 1
            else:
                d[s[i - window]] -= 1

        return window
        """
        MY SOLUTION: sliding window, 55min elapsed
        TC O(N) SC O(26) = O(1)
        왜 이렇게 짜칠까 코드가... 얼른 답안 보고 싶다 ㅠㅠ
        """
        i, j = 0, 1
        result = -1
        seen = {}
        seen[s[i]] = 1

        while j < len(s):
            if s[j] in seen:
                seen[s[j]] += 1
            else:
                seen[s[j]] = 1

            cnt_arr = list(seen.values())
            cnt = sum(cnt_arr) - max(cnt_arr)

            if cnt > k:
                seen[s[i]] -= 1
                i += 1
            else:
                result = max(result, j - i + 1)

            j += 1

        return result
