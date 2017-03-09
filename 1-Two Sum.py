class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        buff_dict = {} #initial a blank dictionary
        for i in range(len(nums)): # get the length
            if nums[i] in buff_dict: # if found the element, then we can get the index
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i #save the element needed with index - i
