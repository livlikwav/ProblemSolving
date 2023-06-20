class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  # O(3N)
        """
        My solution, 문제 footer 에 unicode 도 풀 수 있도록 해보라기에 그렇게 짰다. count sort 식으로 짜진 않고 dict 사용했으니 괜찮을듯. 어쨌든 문자 가짓수 최대 2*10^4
        """
        sd = {}
        for x in s:  # O(N)
            if x in sd:
                sd[x] += 1
            else:
                sd[x] = 1

        for x in t:  # O(N)
            if x in sd:
                sd[x] -= 1
            else:
                return False

        for x in sd.values():  # O(N)
            if x != 0:
                return False
        return True
        """
        Voted #1 python 3
        근데 이렇게 풀면 유니코드는 대응 못함. O(26N) 인데, 영어 소문자라 26이지 유니코드 4byte 였으면 불가능 O(2^32N)
        """
        # In case of different length of thpse two strings...
        if len(s) != len(t):
            return False
        for idx in set(s):
            # Compare s.count(l) and t.count(l) for every index i from 0 to 26...
            # If they are different, return false...
            if s.count(idx) != t.count(idx):
                return False
        return True     # Otherwise, return true...
        """
        Voted #2
        Python 에서는 key 존재 여부를 in 연산자로 직접 확인해야하고, 이를 해결하기 위해 dict.setdefault(), collections.defaultdict 같은 해결책이 있다.
        접근 방식은 결국 나 솔루션과 동일하다. 그리고 all(iterable) 이라는 내장 함수 있는것도 알았다.
        """
        tracker = collections.defaultdict(int)
        for x in s:
            tracker[x] += 1
        for x in t:
            tracker[x] -= 1
        return all(x == 0 for x in tracker.values())
