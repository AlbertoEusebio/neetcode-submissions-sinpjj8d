class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        operations = operations[::-1]

        record = []
        while operations:

            o = operations.pop()

            if o not in ['C', 'D', '+']:
                n = int(o)
                record.append(n)
            else:
                if o == 'C':
                    record.pop()
                elif o == 'D':
                    record.append(2*record[-1])
                elif o == '+':
                    record.append(record[-1] + record[-2])
        return sum(record)
        