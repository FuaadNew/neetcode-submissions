class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted([(posit, (target - posit)/ spd) for posit,spd in zip(position,speed)])
        stack = []
        for car in reversed(cars):
            position,time = car
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)
