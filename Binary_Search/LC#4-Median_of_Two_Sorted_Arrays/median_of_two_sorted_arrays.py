# 4. Median of Two Sorted Arrays
# Difficulty: Hard
# Topics: Array, Binary Search, Divide and Conquer
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # # Brute force
        # Time Complexity: O(m + n)
        # Space Complexity: O(m + n)

        # p1 = 0
        # p2 = 0
        # m = len(nums1)
        # n = len(nums2)
        # merged_arr = []
        # for i in range(m+n):
        #     if p1 < len(nums1) and p2 < len(nums2):
        #         if nums1[p1] <= nums2[p2]:
        #             merged_arr.append(nums1[p1])
        #             p1 += 1
        #         else:
        #             merged_arr.append(nums2[p2])
        #             p2 += 1
        #     elif p1 < len(nums1):
        #         merged_arr.extend(nums1[p1:])
        #         break
        #     else:
        #         merged_arr.extend(nums2[p2:])
        #         break
        # print(merged_arr)
        
        # if len(merged_arr) == 0:
        #     return 0.0
        # # even length
        # if len(merged_arr) % 2 == 0:
        #     mid2 = merged_arr[len(merged_arr) // 2]
        #     mid1 = merged_arr[len(merged_arr) // 2 - 1]
        #     return (mid2 + mid1) / 2.0
        # else:
        #     return merged_arr[len(merged_arr) // 2]

        # Optimal (binary search)
        
        if len(nums1) <= len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2

        # for smaller array where we do binary search
        l, r = 0, len(A) - 1

        # for bigger array
        while True:
            mid = (l + r) // 2
            # pointer for bigger array. Need "- 2" because it's the index
            j = half - mid - 2
            leftA = A[mid] if mid >= 0 else float("-infinity")
            rightA = A[mid+1] if (mid+1) < len(A) else float("infinity")
            leftB = B[j] if j >= 0 else float("-infinity")
            rightB = B[j+1] if (j+1) < len(B) else float("infinity")
            
            # binary search conditions
            if leftA <= rightB and leftB <= rightA:
                # then we know we partioned correctly and can find median
                # even total array, so median is average of middle two values
                if total % 2 == 0:
                    first_num = max(leftA, leftB)
                    second_num = min(rightA, rightB)
                    median = (first_num + second_num) / 2.0
                    return median
                else:
                    median = min(rightA, rightB)
                    return median
            elif leftA <= rightB:
                # leftB > rightA so we need to take more elements from A array
                l = mid + 1
            else:
                # leftA > rightB so we need to take less elements from A array
                r = mid - 1

solution_instance = Solution()

case_1_nums_1 = [1, 3]
case_1_nums_2 = [2]
case_1_output = 2.0

case_2_nums_1 = [1, 2]
case_2_nums_2 = [3, 4]
case_2_output = 2.5

assert solution_instance.findMedianSortedArrays(case_1_nums_1, case_1_nums_2) == case_1_output
assert solution_instance.findMedianSortedArrays(case_2_nums_1, case_2_nums_2) == case_2_output

print("All tests passed successfully!")