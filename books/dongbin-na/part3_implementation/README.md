# 문자열 압축 오답노트

## 210103

답과 정확히 동일하다. 그냥 내가 문자열을 매번 생성하지 않았을 뿐.
그렇다면 왜 틀렸을까? 구현에 있어서 세부적으로 오동작이 있는 것임.
구현 문제의 경우 차라리 문제 진짜 그대로 똑같이 구현하는 것이 나을 수도 있겠다.

>> 문제는 시간 초과일 수도 있다!
2,7,17,18,20,21,23,27
>> 응 아니야
2,5,7,17,18,20,21,23,27

### 테스트 케이스 참고

xxxxxxxxxxyyy
-> 10x3y -> 5
a
-> a -> 1
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-> 100x -> 4
zxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-> z100x -> 5
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxz
-> 100xz -> 5
bbaabaaaab
8 2b2ab4ab
zzzbbabbabba
7 zzz3bba

### 기존 코드 개선 후 해결

(개선1: count 10, 100, 100 제대로 출력)
(개선2: len(s) // 2 + 1에서 "a"가 제대로 안되므로 다시 len(s)로 회귀)

다행히 속은 시원해졌다...  
하지만 구현 문제의 경우, 앞으로 이렇게 임의로 다르게 풀지 않기.  
시간 복잡도 문제가 없다면 **굳이 문제 요구와 다르게 풀 필요가 없다.**
