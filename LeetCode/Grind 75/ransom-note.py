class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Voted #1 오 무슨 이런게 있네
        https://www.daleseo.com/python-collections-counter/
        collections 모듈의 Counter 클래스이다.
        중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 나오는지가 저장된 객체를 얻게 된다.
        dict 를 확장한 Counter 라는 객체 리턴한다. !! 산술/집합 연산이 가능한게 신기하다 !!
        & 교집합 | 합집합.
        교집합을 해서 st1 이 st2 에 포함되는지 확인한다. 만약 st2 에 충분한 char 가 없으면 == st1 이 실패할 것이니까.
        """
        from collections import Counter

        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False
        """
        Voted #2 이건 string.count() 메소드를 사용했네. 근데 이거 O(N) 이다 (당연히 순차탐색이니 확실하다). 비효율적.
        TC O(N) = O(26N)
        """
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True
        """
        MY SOLUTION, 8m elapsed
        문자 길이 최대 10^5 이라서 간단하게 loop 로 풀었다.
        TC O(2N) SC O(1) = O(26 * 2)

        english lowcase only 니까 26자만 사용하면 된다. ASCII byte 로 26 len [] 만들어서 체크할 수도 있었을듯.
        단, python 에서 ASCII 변환이 잘 안해봤어서 이렇게 간단하게 품.
        """
        randict = {}
        for c in ransomNote:  # O(N)
            if c in randict:
                randict[c] += 1
            else:
                randict[c] = 1

        madict = {}
        for c in magazine:  # O(N)
            if c in madict:
                madict[c] += 1
            else:
                madict[c] = 1

        for k in randict:  # O(1) = 26
            if k not in madict or randict[k] > madict[k]:
                return False

        return True
