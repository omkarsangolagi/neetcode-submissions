class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i=0
        h=set()
        nums.sort()

        for i in range(0,len(nums)-1):
            j=i+1
            k=len(nums)-1
            while(j<k):
                if (nums[i]+nums[j]+nums[k]==0):
                    a=[]
                    a.append(nums[i])
                    a.append(nums[j])
                    a.append(nums[k])
                    h.add(tuple(a))
                    j += 1
                    k -= 1
                elif (nums[i]+nums[j]+nums[k]>0):
                    k -= 1
                else:
                    j += 1
        return [list(t) for t in h]
        
        