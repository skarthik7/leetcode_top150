class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        
        def dfs(i):
            if visited[i] == -1:
                return True
            if visited[i] == 1:
                return False
            visited[i] = -1
            for j in graph[i]:
                if dfs(j):
                    return True
            visited[i] = 1
            return False
        
        order = []
        for i in range(numCourses):
            if dfs(i):
                return []
            if visited[i] == 0:
                visited[i] = 1
                order.append(i)
        return order