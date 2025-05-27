class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #swicth = False
        #t = 1
        #for i in range(0, l):
            #if 0 not in nums and len(nums) > 1:
            #    if t not in nums and t == i:
            #        t = i+1
            #        continue
            #    return 0
            #elif i not in nums:
            #    return i   
        #return i+1
        
        for i in range(len(nums)):
            if i not in nums:
                return i   
        return i+1