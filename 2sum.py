
class Solution(object):
    def twoSum(self, nums, target):
        seen = {} 
        for i, num in enumerate(nums):
            complement = target - num 
            if complement in seen:  # Nếu giá trị còn thiếu đã xuất hiện
                return [seen[complement], i]  # Trả về cặp chỉ số
            seen[num] = i  # Lưu giá trị hiện tại vào dictionary
        
