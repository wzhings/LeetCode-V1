class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        min_gap = 1000000
        nums.sort()

        for i in xrange(len(nums) - 2):
          if i > 0 and nums[i] == nums[i-1]:
            continue
          l, r = i+1, len(nums)-1
          while l < r:
            sums = nums[i] + nums[l] + nums[r]
            gap = abs(sums - target)
            if gap < min_gap:
              result = sums
              min_gap = gap
            if sums < target:
              l += 1
            else:
              r -= 1

        return result



