class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#暴力
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
        return[]

  
        
        
        
   #双指针     
        temp=nums.copy()
        temp.sort()
        i=0
        j=len(nums)-1
        while i<j:
            if (temp[i]+temp[j])>target:
                j=j-1
            elif (temp[i]+temp[j])<target:
                i=i+1
            else:
                break
        p=nums.index(temp[i])
        nums.pop(p)
        k=nums.index(temp[j])
        if k>=p:
            k=k+1
        return[p,k]


