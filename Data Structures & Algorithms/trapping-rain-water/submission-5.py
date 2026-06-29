class Solution:
    def trap(self, height: List[int]) -> int:

        def find_highest_wall(l,r):
            res = 0
            while l < r:
                res = max(res, height[l])
                l+=1
            return res

        res = 0
        
        for i in range(len(height)):
            left_wall = find_highest_wall(0,i+1)
            right_wall = find_highest_wall(i,len(height))

            limiting_wall = min(left_wall, right_wall)

            water_trapped = max(limiting_wall - height[i],0)
            res+=water_trapped
        return res
                