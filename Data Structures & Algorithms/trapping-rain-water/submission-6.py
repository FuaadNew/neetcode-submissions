class Solution:
    def trap(self, height: List[int]) -> int:
        left_walls = [0] * len(height)
        right_walls = [0] * len(height)

        for i in range(len(height)):
            if i == 0:
                left_walls[i] = height[i]
            else:
                left_walls[i] = max(left_walls[i-1], height[i])
        
        for i in range(len(height)-1,-1,-1):
            if i == len(height)-1:
                right_walls[i] = height[i]
            else:
                right_walls[i] = max(right_walls[i+1], height[i])
        res = 0
        for i in range(len(height)):
            limiting_wall = min(left_walls[i], right_walls[i])
            water_trapped = max(limiting_wall - height[i], 0)
            res+=water_trapped
        return res