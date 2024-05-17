class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        stack = [i for i in range(numCourses) if indegree[i] == 0]
        order = []
        while stack:
            node = stack.pop()
            order.append(node)
            for i in graph[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    stack.append(i)
        return order if len(order) == numCourses else []