class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if target in triplets:
            return True

        maxima = [0]*3
        for t in triplets:
            larger = False
            for i in range(3):
                if t[i] > target[i]:
                    larger = True
                    break
            if larger:
                continue
            for i in range(3):
                maxima[i] = max(maxima[i], t[i])
            if maxima == target:
                return True
            print(maxima)

        return False