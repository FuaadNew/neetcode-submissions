class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = [(x,i) for i,x in enumerate(temperatures)]
        #[(38, 1), (30, 2), (36, 3), (35, 4), (40, 5), (28, 6)]
        #stack = [(30,0)]
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temps)):
            temp, index = temps[i]
            if not stack:
                stack.append((temp,index))
                continue
            while stack and temp > stack[-1][0]:
                last_temp, last_index = stack.pop()
                res[last_index] = index - last_index
            stack.append((temp,index))
        return res




        




        
