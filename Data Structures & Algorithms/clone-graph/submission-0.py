"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # edge case
        if node is None:
            return None

        old_to_new = {}

        def dfs(cur):
            # check if it is cloned
            if cur in old_to_new:
                return old_to_new[cur]

            copy = Node(cur.val)
            old_to_new[cur] = copy

            for n in cur.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        return dfs(node)
