class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for i in strs:
            k = "".join(sorted(i))
            if k in h:
                h[k].append(i)
            else:
                h[k] = [i]
        return list(h.values())
        