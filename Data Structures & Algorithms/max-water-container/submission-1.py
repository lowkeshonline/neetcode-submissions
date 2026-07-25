class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1,7,2,5,4,7,3,6 - Heights
        # 0 1 2 3 4 5 6 7 - [r - l] = width of a container

        res = 0
        left = 0
        right = len(heights) - 1

        while left < right:

            area = (right - left) * min(heights[left],heights[right])

            res = max(res,area)

            if heights[left] > heights[right]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            else:
                left += 1

        return res










        