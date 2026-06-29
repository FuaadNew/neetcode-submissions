class Solution:
    def trap(self, height: List[int]) -> int:
        left_walls = [0] * len(height)
        highest_right_wall_so_far = 0

        for i in range(len(height)):
            if i == 0:
                left_walls[i] = height[i]
            else:
                left_walls[i] = max(left_walls[i-1], height[i])
        print(left_walls)
        res = 0
        for i in range(len(height)-1,-1,-1):
            highest_right_wall_so_far = max(highest_right_wall_so_far, height[i])
            limiting_wall = min(left_walls[i], highest_right_wall_so_far)
            water_trapped = max(limiting_wall - height[i], 0)
            res+=water_trapped
        return res