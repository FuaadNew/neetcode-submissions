class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #create set to hold values
        good = set()
        # iterate through all triplets
        for t in triplets:
            # if the triplet being iterated has a value greater than it's corresponding target value
            # go past it 
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            # for every index and value in curent triplet
            for i,v in enumerate(t):
                # if the value at the index equals the target at that index
                if v == target[i]:
                    # we add that index to the good set
                    good.add(i)
            # if the length of good is equal to three 
            # we return True
        return len(good) == 3