class Solution:
    """
    이런 sliding window, two pointers 와 같은 기본적인 조건 구현하는게 너무 안된다... 이런 유형만 계속 풀자.
    while loop 를 out of index 되지 않게 하는것도 잘 못하는것 같다. 정신차리자.
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Voted #3, two pointers, 하지만 set 을 사용했다. 직접 최적화를 구현하지 않고 자료구조를 활용했다.
        이게 내가 원하던 방법인데 M 으로 1 pointer 는 fix 하는게 문제였던 것 같다.
        아이디어 #1: i,l,r 무엇이 중복되더라도 상관없이 그냥 set 에 담는다.
        TC O(N^2) SC O(1) 파라미터는 공간복잡도에 포함하지 않으므로 현 함수의 공간복잡도는 상수
        """
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1

        return list(result)
        """
        Voted #2, two pointers, 왜 나는 틀리고 이건 맞았을까?
        아이디어 #1: i,j,k 중에서 i,j 의 중복을 체크하면 k 는 자동으로 중복 스킵된다.
        아이디어 #2: 코드가 매우 간결하다. if 문이 반복되고 복잡하지 않다. 내가 구현하면서도 코드가 더러워진다 싶으면 무언가 잘못되었다고 눈치채야한다.

        TC O(N^2), SC O(1)
        """
        nums.sort()  # sorting cause we need to avoid duplicates, with this duplicates will be near to each other
        l = []

        for i in range(len(nums)):  # this loop will help to fix the one number i.e, i
            if (
                i > 0 and nums[i - 1] == nums[i]
            ):  # skipping if we found the duplicate of i
                continue

            # now following the rule of the two pointers after fixing the one value i
            j = i + 1  # taking j pointer larget than i (as said in ques)
            k = len(nums) - 1  # taking k pointer from last
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1  # so take value less than previous
                elif s < 0:
                    j += 1  # so take value greater than previous
                else:
                    l.append(
                        [nums[i], nums[j], nums[k]]
                    )  # if sum s found equal to the target (0)
                    j += 1
                    while (
                        nums[j - 1] == nums[j] and j < k
                    ):  # skipping if we found the duplicate of j and we dont need to check
                        # the duplicate of k cause it will automatically skip the duplicate by the adjustment of i and j
                        j += 1

        return l
        """
        Voted #1, Naive implementation, 문제에서 얘기한 조건을 정확한 경우의 수를 파악하여 풀어낸 방법이다.
        이거는 실전에서 하기는 좀 어려울 듯; 뭐라도 잘못 구현하거나 빼먹는 경우에 디버깅 하는데 어버버 하게 되어서 시간을 많이 쓰게 된다.
        아이디어 #1: O(N^2) 가 가능한걸 그대로 활용하고, Set 을 사용하여 O(N^3) 이 안되도록 한다. 말그래도 공간 복잡도를 희생하여 시간 복잡도를 좀 살렸다.
        아이디어 #2: Edge case 인 000 이나 -3,0,3 을 잘 걸러냈다.
        """
        res = set()

        # 1) split nums into three lists: negative, positive, zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        # 2) create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        # 3) If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        # i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))

        # 4) If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0, 0, 0))

        # 5) For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        # exists in the positive number set
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        # 6) Same method buf different objective, positive numbers
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        return res
        """
        MY FAILED SOLUTION #2: time exceeded
        looping M, and iterating L, R 2 pointers
        """
        seen = []
        result = []
        nums.sort()

        for m in range(1, len(nums) - 1):
            l, r = m - 1, m + 1

            while l >= 0 and r < len(nums):
                temp = nums[l] + nums[m] + nums[r]
                if temp == 0:
                    temp_set = set([nums[l], nums[m], nums[r]])
                    if (
                        temp_set not in seen
                    ):  # maybe this is the reason of time exceeding
                        result.append([nums[l], nums[m], nums[r]])
                        seen.append(temp_set)
                    l -= 1
                    r += 1
                elif temp > 0:
                    l -= 1
                else:
                    r += 1

        return result
        """
        MY FAILED SOLUTION #1
        looping L, R, and iterating M
        """
        # l, m, r = 0, 0, len(nums)-1
        # result = set()

        # while l != r:
        #     temp = nums[l] + nums[r]
        #     if temp == 0:
        #         for x in range(l+1, r-1):
        #             if x == 0:
        #                 result.add([nums[l], nums[x], nums[r]])
        #     elif temp > 0:
        #         for x in range(l+1, r-1):
        #             if x >= 0:
        #                 break

        #             temp2 = temp + nums[x]
        #             if temp2 == 0:
        #                 result.add([nums[l], nums[x], nums[r]])
        #     elif temp < 0:
        #         for x in range(r-1, l+1, -1):
        #             if x <= 0:
        #                 break

        #             temp2 = temp + nums[x]
        #             if temp2 == 0:
        #                 result.add([nums[l], nums[x], nums[r]])
