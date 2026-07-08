class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        l = []
        s = sorted(h.keys(), key = h.get , reverse = True)
        for i in range(k):
            l.append(s[i])
            
        return l
        
        
        
                
        


