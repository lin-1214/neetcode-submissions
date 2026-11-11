class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        table = dict()
        ans = []

        for string in strs:
            counts = [0]*26
            for c in string:
                counts[ord(c) - ord('a')] += 1

            counts = tuple(counts)

            if counts not in table:
                table[counts] = []
            
            table[counts].append(string)

        
        for v in table.values():
            ans.append(v)

        return ans