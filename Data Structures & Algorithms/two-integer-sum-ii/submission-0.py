class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        left = 0
        right = n - 1
        while(left < right):
            if target < numbers[left] + numbers[right]:
                right -= 1
            elif target > numbers[left] + numbers[right]:
                left += 1
            else:
                return [left + 1, right + 1]

        return [0, 0]

       
            
        