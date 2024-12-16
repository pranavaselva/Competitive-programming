class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, combo):
            if len(combo) == k:
                result.append(combo[:])
                return
            
            for i in range(start, n+1):
                combo.append(i)
                backtrack(i+1, combo)
                combo.pop()
        
        result = []
        backtrack(1, [])
        return result