class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            if (target-i in nums):
                try:
                    if nums.index((target-i),nums.index(i)+1):
                        return [nums.index((target-i), nums.index(i)+1), nums.index(i)]
                
                    if nums.index((target-i), 0, nums.index(i)):
                        return [nums.index((target-i), 0, nums.index(i)), nums.index(i)]
                except:
                    continue

                