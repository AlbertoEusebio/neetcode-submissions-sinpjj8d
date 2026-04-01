class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        hand = sorted(hand)

        freq = defaultdict(int)

        for n in hand:
            freq[n] += 1

        while freq:
            k = min(freq.keys())
            print(k, freq)
            # try to form group
            for i in range(k, k+groupSize):
                if i not in freq:
                    return False
                freq[i] -= 1
                if freq[i] == 0:
                    del freq[i]
        
        return True