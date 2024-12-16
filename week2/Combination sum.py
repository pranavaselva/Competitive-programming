class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(index, curr_target, arr):
            if curr_target == 0:
                result.append(list(arr))
                return
            elif curr_target < 0:
                return

            for i in range(index, len(candidates)):
                arr.append(candidates[i])
                backtrack(i, curr_target - candidates[i], arr)
                arr.pop()
        
        result = []
        backtrack(0, target, [])
        return result