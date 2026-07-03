class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [(posit, (target - posit) / sped) for posit,sped in zip(position, speed)]
        cars.sort()

        stack = []
        print(cars)
        for car in reversed(cars):
            posit, time = car
            if stack and stack[-1][1] >= time:
                pass
            else:
                stack.append(car)
        return len(stack)

        [(0, 5.0), 
        (2, 2.6666666666666665), 
        (4, 6.0)]

