class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums) - 1
        res = set()
        nums.sort()

        for i in range(n - 1):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1 
            right = n

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:

                    triplets  = tuple([nums[i], nums[left], nums[right]])
                    res.add(triplets)
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                
        return list(res)



        