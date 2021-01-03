class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    #方法1：将不为0的元素向前移，0元素向后移，时间复杂度为O(n),空间复杂度为O(1)
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            elif count != 0:
                nums[i - count], nums[i] = nums[i], 0
        return nums
    
    #方法2：快慢指针，快指针不断往后遍历，找到不为0的数，一旦找到，就把该值赋予给慢指针所在的位置，然后慢指针往后走一格，这样就保证慢指针前面的全是非0，等快指针遍历完了，那么直接把慢指针之后的都赋为0即可。


        slow = 0;

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

        for i in range(slow,len(nums)):
            nums[i] = 0




