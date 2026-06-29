class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        highest_left_wall_so_far = 0
        highest_right_wall_so_far = 0
        res = 0
        while l<=r:
            highest_left_wall_so_far = max(highest_left_wall_so_far, height[l])
            highest_right_wall_so_far = max(highest_right_wall_so_far, height[r])

            if highest_left_wall_so_far < highest_right_wall_so_far:
                res+= max(highest_left_wall_so_far - height[l], 0)
                l+=1
            
            elif highest_right_wall_so_far <= highest_left_wall_so_far:
                res+= max(highest_right_wall_so_far - height[r], 0)
                r-=1
        return res

