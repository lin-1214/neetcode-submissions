class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # construct graph to detect whether a path form a loop
        graph = [[] for _ in range(numCourses)]
        states = [0 for _ in range(numCourses)] # 0: unvisited, 1: visited, 2: safe

        for x,y in prerequisites:
            graph[y].append(x)

        def dfs(node):
            if states[node] == 1:
                return False    # forms a loop
            if states[node] == 2:
                return True

            states[node] = 1

            # check if the current node forms a loop with it neighbor
            for nxt in graph[node]:
                if not dfs(nxt):
                    return False
            states[node] = 2
            return True

        return all([dfs(i) for i in range(numCourses)])



