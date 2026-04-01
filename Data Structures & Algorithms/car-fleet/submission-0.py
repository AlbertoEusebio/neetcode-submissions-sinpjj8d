class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # time #######################
        #0# /   /
        #1#/|  /
        #2# | /
        #3#/ /
        #4# /
        #5#/ 
        #N# 

        print(sorted(zip(position, speed),key = lambda ps: ps[0]))

        time_arrivals = [(target - p)/v for p,v in sorted(zip(position, speed),key = lambda ps: ps[0], reverse=True)]

        i = 0
        fleets = 0
        
        min_t = 0

        while i < len(time_arrivals):

            if time_arrivals[i] > min_t:
                fleets += 1
                min_t = time_arrivals[i]

            i += 1
        return fleets
