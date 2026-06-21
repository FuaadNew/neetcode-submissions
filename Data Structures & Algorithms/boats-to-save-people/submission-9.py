class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        res = []
        level = []
        people = sorted(people)

        while people:
            if len(level) == 2:
                res.append(level)
                level = []
            if people[-1] + sum(level) <= limit:
                level.append(people.pop())
            elif people[0] + sum(level) <= limit:
                level.append(people.pop(0))
            else:
                if level:
                    res.append(level)
                level = []

        if level:
            res.append(level)
        return len(res)

