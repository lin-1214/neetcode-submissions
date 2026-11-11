class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False

        table = dict()
        for c in s:
            if c not in table:
                table[c] = 0
            table[c] += 1
        
        for c in t:

            if c not in table:
                return False
            table[c] -= 1
            
        
        if any(v > 0 for v in table.values()):
            return False

        return True