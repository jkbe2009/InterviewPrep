
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = nums[0]
        count = 1

        for num in nums[1:]:
            if num == candidate:
                count += 1
            else:
                if count == 0:
                    candidate = num
                    count = 1
                else:
                    count -= 1
        
        return candidate