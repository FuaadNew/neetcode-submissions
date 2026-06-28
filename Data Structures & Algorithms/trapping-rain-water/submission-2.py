class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        max_l = max_r = 0
        res = 0
        while l < r:
            max_l = max(max_l, height[l])
            max_r = max(max_r, height[r])
            if max_l < max_r:
                cur_height= max(min(max_l, max_r) - height[l], 0)
                res+=cur_height
                l+=1
            else:
                cur_height= max(min(max_l, max_r) - height[r], 0)
                res+=cur_height
                r-=1
        return res


