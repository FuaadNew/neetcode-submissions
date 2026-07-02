class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temps)

        for i,x in enumerate(temps):
            while stack and temps[stack[-1]] < x:
                last_indx = stack.pop()
                res[last_indx] = i - last_indx
            stack.append(i)
        return res



