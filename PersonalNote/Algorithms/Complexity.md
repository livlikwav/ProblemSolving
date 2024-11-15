# Complexity

- Time
- Space

Big-O Notation
최악의 경우를 기준으로 성능을 평가한다.

문제의 제약조건(시간, 메모리) 를 확인하고,
그에 맞는 효율적인 알고리즘을 선택해야 한다.

## Time

일반적으로 1s 에 1억 번 연산이 가능하다고 가정한다. (10^8)

예를 들어 n=10^6 인 경우, O(n) 알고리즘은 사용 가능하나, O(n^2) 알고리즘은 사용 불가능하다.

> gpt4o

제약 조건에 따른 시간 복잡도 추정 기준
1초에 대략적으로 1억 회 연산을 수행할 수 있다고 가정하면 다음과 같은 기준을 세울 수 있습니다.

| 입력 크기 n (제약 조건) | 권장 시간 복잡도 |
| -- | -- |
| n ≤ 10 | O(n!) 또는 O(2^n) 가능 |
| n ≤ 20 | O(2^n) 가능 |
| n ≤ 100 | O(n^3) 이하 추천 |
| n ≤ 1,000 | O(n^2) 이하 추천 |
| n ≤ 100,000 | O(n log n) 이하 추천 |
| n ≤ 10^6 | O(n) 이하 추천 |
| n ≤ 10^9 | O(log n) 이하 추천 |

언어별 성능 차이

- Python은 상대적으로 느려서 1초당 10^7 ~ 10^8 정도의 연산을 기준으로 하는 것이 좋습니다.
- Golang과 Java는 비슷하며, 1초당 10^8 정도의 연산을 기준으로 계산하면 적절합니다.

문제 제약조건을 보고 시간 복잡도 추정하는 방법
예를 들어 입력 크기(n)가 100,000이라고 가정하면:

- Python: O(n log n) 이하 추천 (O(n^2)는 대부분 시간 초과 발생)
- Java, Golang: O(n log n) 이하로 구현할 때 안정적

예시

- 재귀 호출 (예: 피보나치): O(2^n), 단 메모이제이션 적용 시 O(n)
- 이진 탐색 또는 균형 이진 트리: O(log n)

## Space

알고리즘이 실행될 때 사용하는 메모리 양을 측정한다.
입력 데이터의 크기와
추가적으로 사용하는 메모리에 따라 결정된다.

- O(1)
  - 추가 메모리를 거의 사용하지 않는 경우
- O(n)
  - 입력 크기에 비례하여 메모리를 사용하는 경우
- O(n^2)
  - 2차원 배열이나 중첩된 데이터 구조를 사용할 때 발생

`int[n] arr // 공간 복잡도 O(n)`
