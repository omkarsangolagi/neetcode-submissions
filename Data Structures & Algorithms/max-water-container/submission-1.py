class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water=[]
        i=0
        j=len(heights)-1
        while(i<j):
            current = (min(heights[i],heights[j]))*(j-i)
            water.append(current)
            if heights[i]>heights[j]:
                j -= 1
            else:
                i += 1
        return max(water)
        