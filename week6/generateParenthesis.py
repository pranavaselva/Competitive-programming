class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, openn, close):
            if len(current) == n*2:
                result.append(current)
                return

            if openn < n:
                backtrack(current + "(", openn + 1, close)

            if close < openn:
                backtrack(current + ")", openn, close+1)

        backtrack("", 0, 0)
        return result