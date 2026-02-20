
class Solution(object):
    def twoSum(self, nums, target):
        seen = {} 
        for i, num in enumerate(nums):
            complement = target - num 
            if complement in seen:  
                return [seen[complement], i]  # Trả về cặp chỉ số
            seen[num] = i  
