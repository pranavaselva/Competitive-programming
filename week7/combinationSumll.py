class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(index, curr_target, arr):
            if curr_target == 0:
                result.append(list(arr))
                return
            elif curr_target < 0:
                return

            for i in range(index, len(candidates)):
                if candidates[i] > curr_target:
                    break
                elif i > index and candidates[i] == candidates[i-1]:
                    continue

                arr.append(candidates[i])
                backtrack(i+1, curr_target - candidates[i], arr)
                arr.pop()

        backtrack(0, target, [])
        return result