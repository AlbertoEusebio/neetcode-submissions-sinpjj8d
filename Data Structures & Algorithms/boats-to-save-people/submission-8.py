class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # freq = defaultdict(int)
        # for p in people:
        #     freq[p] += 1

        # boats = 0
        # for p in people:
        #     c = limit - p
        #     # print(c, freq, boats)
        #     if c == 0:
        #         freq[p] -= 1
        #         boats += 1
            
        #     if c in freq and freq[c] > 0:
        #         freq[c] -= 1
        #         freq[p] -= 1

        #         boats += 1
        # # print(c, freq, boats)
        
        # s = 0
        # for p in people:
        #     if freq[p] <= 0:
        #         continue
        #     # print(p)
        #     if s + p > limit:
        #         s = p
        #         freq[p] -=1
        #         boats += 1
        #     else:
        #         s += p
        #         freq[p] -=1

        # return boats + 1 * int(s > 0)

        boats = 0

        people = sorted(people)
        taken = [0]*len(people)

        i, j = 0, len(people)-1
        s = people[j]
        while i < j:
            c = s + people[i]
            if c <= limit:
                boats +=1
                taken[i] = 1
                taken[j] = 1
                i +=1
                j -= 1
                if i <= j:
                    s = people[j]
                else:
                    s = 0
            elif c > limit:
                boats +=1
                j-=1
                taken[j] = 1
                s = people[j]

        print(i, j, sum(taken), len(taken))
        return boats + int(s>0)
