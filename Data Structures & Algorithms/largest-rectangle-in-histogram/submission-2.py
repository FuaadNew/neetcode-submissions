class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        res = 0
        for i,h in enumerate(heights):
            start = i
            while stack and h <stack[-1][1]:
                last_index, last_height = stack.pop()
                res = max(res, (i - last_index) * last_height)
                start = last_index
            stack.append((start,h))
        while stack:
            last_index, last_height = stack.pop()
            res = max(res, (len(heights) - last_index) * last_height)
        return res