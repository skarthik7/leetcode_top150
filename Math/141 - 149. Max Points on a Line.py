class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)

        max_points = 0
        for i, p1 in enumerate(points):
            same = 1
            count = {}
            for j in range(i + 1, len(points)):
                p2 = points[j]
                if p1 == p2:
                    same += 1
                else:
                    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
                    g = gcd(dx, dy)
                    slope = (dx // g, dy // g)
                    count[slope] = count.get(slope, 0) + 1
                    max_points = max(max_points, count[slope])
            max_points = max(max_points, same)
        return max_points