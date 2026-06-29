class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        for i in range(len(height)):
            left_max = max(height[0:i+1])
            right_max = max(height[i:len(height)])
            limiting_wall = min(left_max, right_max)
            water_trapped = max(limiting_wall - height[i], 0)
            res+= water_trapped
        return res
