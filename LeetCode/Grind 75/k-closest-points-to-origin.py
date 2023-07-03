import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        MY SOLUTION, 9m elapsed TC O(NlogN + KlogN) SC O(N)
        N 이 10^4 였어서 TC O(N^2) 인 경우에 TIME EXCEEDED 가능성이 있었다.
        그래서 삽입 NlogN, 삭제 KlogN 을 생각해서 바로 min heap 을 떠올려서 적용했다.

        지금 생각해보니, 일단 쭉 삽입하고, sort NlogN 으로 한 다음에 앞에서부터 K 개 뽑아도 될 것 같다.
        """
        heap = []  # min heap is default

        for point in points:
            x, y = point[0], point[1]
            dis = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

            heapq.heappush(heap, (dis, x, y))

        result = []
        for i in range(k):
            dis, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result
        """
        Voted #1 TC(NlogK) SC(K)
        핵심 아이디어는 내 솔루션과 동일하다. 디테일이 추가되어 좀 최적화 된 버전이다. 
        K 개를 원하므로, max heap 을 사용하고, 삽입 시 K 개가 넘어가면 heappushpop 을 사용하는 것이다.
        정확한 거리 값이 아니라 비교만 하면 되므로, math.sqrt 도 생략했다.
        그리고 K 개만 유지하므로 삭제 연산이 필요없이 heap 그대로 리턴한다.

        heappushpop 은 일단 넣고 뺀다. 그래서 새로 넣은 값이 가장 크면 바로 빠지게 된다.
        """
        heap = []

        for x, y in points:
            dist = -(x * x + y * y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [(x, y) for (dist, x, y) in heap]
        """
        Voted #2
        당연하게도 그냥 sorting 도 방법이 있었다. O(NlogN)
        """
        points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)
        return points[:K]
        """
        Voted #3
        이 글이 흥미로웠는데, 이 문제를 라이브코딩이라 생각하고 각 솔루션을 제시했을 때 인터뷰어의 기대를 제시해줌.
        그리고 제일 마지막 단의 알고리즘도 소개해줌. Quick-Select 이다.
        TC O(N) best-case, O(N^2) worst case, O(1) Space

        필자: 인터뷰에서 이걸 구현하는건 좋은 것은 아니야. 하지만 이러한 알고리즘도 시도해볼만 하다고 얘기하는건 좋은 신호이다.
        partition 함수가 무엇을 하고, select 함수가 무엇을 하고 ... 이런것들을 설명하고, 다 구현하지는 않아도 된다.
        이걸 통해 너는 TC 와 SC 를 트레이드 오프할 수 있음을 보여준다.
        """
        import heapq
        import math

        # quick select O(N), worst case O(n2)
        def parition(l, r, pivot_index):
            # move pivot to end
            pivot = points[pivot_index][0] ** 2 + points[pivot_index][1] ** 2
            points[pivot_index], points[r] = points[r], points[pivot_index]
            # now start moving elements less than pivot to left and greater to right
            store_index = l
            for i in range(l, r):
                if (points[i][0] ** 2 + points[i][1] ** 2) < pivot:
                    points[store_index], points[i] = points[i], points[store_index]
                    store_index += 1

            # now store_index has the place that pivot should be stored in, swap with pivot elemented
            points[store_index], points[r] = points[r], points[store_index]
            return store_index

        def select(l, r, k):
            if l < r:
                pivot_index = random.randint(l, r)
                pivot_index = partition(l, r, pivot_index)

                if pivot_index == k:
                    return
                if pivot_index < k:
                    select(pivot_index + 1, r, k)
                else:
                    select(l, pivot_index - 1, k)

        select(0, len(points) - 1, k)

        return points[:k]
