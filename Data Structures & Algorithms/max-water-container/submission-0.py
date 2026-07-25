class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1,7,2,5,4,7,3,6 - Heights
        # 0 1 2 3 4 5 6 7 - [r - l] = width of a container

        res = 0

        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):

                area_of_container = (r - l) * min(heights[l] , heights[r])
                res = max(res, area_of_container)

        return res








        