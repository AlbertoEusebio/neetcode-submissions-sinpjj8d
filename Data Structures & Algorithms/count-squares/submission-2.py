class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        # search diag element
        copy_d = self.points


        a, b = point

        count = 0
        for p in copy_d.keys():
            if p == point:
                continue
            x, y = p

            lx = a-x
            ly = b-y

            # not diagonal point
            if lx == 0 or ly == 0 or abs(lx) != abs(ly):
                continue

            print(p, point, (x+lx, y), (x+lx, y+ly))

            if (x+lx, y) in copy_d and (x, y+ly) in copy_d:
                count += copy_d[p] * copy_d[(x+lx, y)] * copy_d[(x, y+ly)]
        
        return count

