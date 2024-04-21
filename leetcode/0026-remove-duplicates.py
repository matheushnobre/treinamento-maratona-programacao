class Solution:
    def removeDuplicates(self, nums):
        '''
        type nums: List[int]
        rtype: int
        '''
        last = nums[0]
        for n in nums[1:]:
            if n == last: nums.remove(n)
            else: last = n
        return len(nums)
    
# Best solution, by users of LeetCode:
#class Solution:
#    def removeDuplicates(self, nums: List[int]) -> int:
#        j = 1
#        for i in range(1, len(nums)):
#            if nums[i] != nums[i - 1]:
#                nums[j] = nums[i]
#                j += 1
#        return j