from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we must create a hashmap to store frequency of the str
        hashmap = defaultdict(list)

        #iterate through every string in list of strs

        for s in strs:
            #create a count frequency list
            count = [0] * 26
            
          #add the frequency of every character
            for c in s:
                count[ord(c) - ord('a')] += 1

            #convert the freq list to a tuple because python dictionary keys don't support list since they are mutable
            key = tuple(count)

            #add the converted freq tuple as a key and append the current string
            hashmap[key].append(s)
        
        return list(hashmap.values())


        