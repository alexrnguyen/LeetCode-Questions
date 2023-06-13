class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums) - 1
        minimum = nums[0]

	# Set up binary search
        while left <= right:
	    # Numbers between pointers are sorted
            if nums[left] < nums[right]:
                minimum = min(minimum, nums[left])
                break

            mid = (left + right)//2
            minimum = min(minimum, nums[mid])

	    # Update pointers
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return minimum