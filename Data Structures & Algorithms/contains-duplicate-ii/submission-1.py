class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Better solution - Let's implement it using the hashmap

        #Create a hashmap to store the numbers and the index

        last_seen = {}

        #check all the nums from left to right
        for i, num in enumerate(nums):
            #check if the num exists in the hashmap
            if num in last_seen:
                #get it's index and check if distance is within k
                if abs(last_seen[num] - i) <= k:
                    return True
            
            #add the index to the hashmap if not seen already
            last_seen[num] = i
        
        return False


        
        


        