class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a hashmap to store the freq

        #{num : freq}

        freq = {}

        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        #create a list of lists and store the freq first and then nums so the sort works out on freq
        #[[freq : nums]]

        arr = []
        for num,cnt in freq.items():
            arr.append([cnt,num])

        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])

        return res
            