class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blks = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                char = board[r][c] 
                if char == ".":
                    continue

                if char in rows[r]:
                    return False
                else:
                    rows[r].add(char)

                if char in cols[c]:
                    return False
                else:
                    cols[c].add(char)

                blk = 3 * (c // 3) + (r // 3)
                if char in blks[blk]:
                    return False
                else:
                    blks[blk].add(char)
        
        return True