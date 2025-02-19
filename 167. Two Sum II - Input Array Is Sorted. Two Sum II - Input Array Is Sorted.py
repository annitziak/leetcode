class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-indexed indices
            elif current_sum < target:
                left += 1  # Increase the sum by moving the left pointer
            else:
                right -= 1  # Decrease the sum by moving the right pointer

