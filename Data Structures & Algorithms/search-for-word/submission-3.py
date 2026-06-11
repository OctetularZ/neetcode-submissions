class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        rows = len(board)
        cols = len(board[0])

        def backtrack(r, c, index):
            if index == len(word):
                return True
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if board[r][c] == '#' or word[index] != board[r][c]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            found = False

            for dr, dc in directions:
                if backtrack(r + dr, c + dc, index + 1):
                    found = True
            
            board[r][c] = temp
            
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True
        
        return False
        
