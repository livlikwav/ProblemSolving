package Docs.Algorithms.searching;

import java.util.Arrays;

public class BinarySearch {
}

class Example {
    static void main(String[] args) {
        int[] nums = { 1, 3, 5, 7, 9, 11 };
        int target = 7;

        int result = bSearch(nums, target);
        System.out.println("result idx: " + result);
    }

    static int bSearch(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }
}

// ParametricSearch
class BudgetAllocation {
    static void main(String[] args) {
        int[] requests = { 120, 140, 110, 150 };
        int totalBudget = 485;

        int result = findMaxCap(requests, totalBudget);
        System.out.println("최대 상환액: " + result);
    }

    static int findMaxCap(int[] requests, int totalBudget) {
        int left = 0;
        int right = Arrays.stream(requests).max().getAsInt();

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int allocated = calculateAllocated(requests, mid); // 상한액 후보

            if (allocated <= totalBudget) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return right;
    }

    static int calculateAllocated(int[] requests, int cap) {
        int total = 0;
        for (int request : requests) {
            total += Math.min(request, cap); // 상한액 만큼만 배정
        }
        return total;
    }
}