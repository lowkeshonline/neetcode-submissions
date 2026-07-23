class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #create a hashmap to count frequencies
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i,0)

        for num,cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            if (len(res) == k):
                return res
            for n in freq[i]:
                res.append(n)
            

        