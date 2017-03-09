# No. 15 - 3Sum

def threeSum(self, nums):
    res = [] #initial the list
    nums.sort() #sort the numbers first
    for i in xrange(len(nums)-2): # minus 2 because we need two more pointers
        if i > 0 and nums[i] == nums[i-1]: # from i = 1, check duplicates
            continue # skip it
        l, r = i+1, len(nums)-1 # only look forward, "i+1" next to i, "len(nums) - 1" is the last one
        while l < r: 
            s = nums[i] + nums[l] + nums[r] # check the sum
            if s < 0:
                l +=1  # because already sorted
            elif s > 0:
                r -= 1
            else: # 3 sums equal to 0
                res.append((nums[i], nums[l], nums[r])) # record this list
                while l < r and nums[l] == nums[l+1]: # two adjacent numbers are equal
                    l += 1 # move forward
                while l < r and nums[r] == nums[r-1]: # two adjacent numbers are equal
                    r -= 1 # move backward
                l += 1
                r -= 1 # then move to the next step
    return res