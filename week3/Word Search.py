class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        listt = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
                
            if r<0 or c<0 or r>=row or c>=col or board[r][c] != word[i] or (r,c) in listt:
                return False

            listt.add((r, c))
            true = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            listt.remove((r,c))
            return true

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        return False
