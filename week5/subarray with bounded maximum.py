class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count_subarray(limit):
            current = 0
            count = 0

            for i in nums:
                if i <= limit:
                    current += 1
                else:
                    current = 0
                count += current
            return count

        return count_subarray(right) - count_subarray(left - 1)