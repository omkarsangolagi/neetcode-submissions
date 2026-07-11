class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        ans=[]
        i=0
        j= len(a)-1
        while(i<j):
            if(a[i]+a[j]==target):
                return [i+1,j+1]
            elif(a[i]+a[j]>target):
                j=j-1
            else:
                i=i+1
        return ans
        