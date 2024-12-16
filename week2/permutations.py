class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(arr):
            if len(arr) == len(nums):
                result.append(arr)
                return
            else:
                for i in nums:
                    if i not in arr:
                        backtrack(arr+[i])

        backtrack([])
        return result