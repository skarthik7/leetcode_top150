class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrows = 1
        curr = points[0][1]

        for start, end in points:
            if start > curr:
                arrows += 1
                curr = end

        return arrows