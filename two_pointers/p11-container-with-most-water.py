class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxContainer = 0
        leftHeight = 0
        rightHeight = len(height) - 1

        while leftHeight < rightHeight:
            area = (rightHeight-leftHeight) * min(height[leftHeight], height[rightHeight])
            maxContainer = max(maxContainer, area)

            if height[leftHeight] < height[rightHeight]:
                leftHeight += 1
            else:
                rightHeight -= 1

        return maxContainer