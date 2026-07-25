class Solution:
    def trap(self, height: List[int]) -> int:

        #create a prefix sums for left max and right max

        n = len(height)
        sum = 0

        leftmax = [0] * n
        rightmax = [0] * n

        leftmax[0] = 0
        for i in range(1,n):
            leftmax[i] = max(leftmax[i - 1], height[i - 1])

        rightmax[n - 1] = 0
        for i in range(n - 2, -1, -1):
            rightmax[i] = max(rightmax[i + 1], height[i + 1])

        print(leftmax, rightmax)

        for i in range(n):
            res = min(leftmax[i],rightmax[i]) - height[i]
            if res <= 0:
                sum += 0
            else: 
                sum += res

        return sum

        