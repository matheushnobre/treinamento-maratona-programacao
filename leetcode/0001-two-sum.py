class Solution:
    def twoSum(self, nums, target):
        '''
        type nums: List[int]
        type target: int
        rtype: List[int]
        '''
        map = {}
        for index, value in enumerate(nums):
            if target - value in map:
                return map[target-value], index
            else:
                map[value] = index