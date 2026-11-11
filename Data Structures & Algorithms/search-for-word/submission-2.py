class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def search(r, c, match):
            if match == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if board[r][c] != word[match]:
                return False

            tmp = board[r][c]
            board[r][c] = "#"
            res = search(r + 1, c, match + 1) or search(r - 1, c, match + 1) or search(r, c + 1, match + 1) or search(r, c - 1, match + 1)

            board[r][c] = tmp


            return res

        for r in range(rows):
            for c in range(cols):
                if search(r, c, 0):
                    return True

        return False
            