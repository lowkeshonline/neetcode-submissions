class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        longest = 1
        num_set = set(nums)

        #check the elements one by one
        for i in range(len(nums)):
            #keep track of current element
            streak = 1
            current = nums[i]
            # check if the current element has it's previous element in numset
            if current - 1 not in num_set:
                while current + 1 in num_set:
                    current += 1
                    streak += 1
                
                longest = max(longest, streak)

        return longest

        