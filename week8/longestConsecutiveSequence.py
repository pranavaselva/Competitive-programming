class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        length = 0
        for i in nums:
            if i-1 not in setNums:
                curr = 0
                while curr+i in setNums:
                    curr += 1
                length = max(length, curr)
        return length