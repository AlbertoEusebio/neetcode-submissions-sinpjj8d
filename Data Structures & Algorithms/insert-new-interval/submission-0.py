class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #      t
        # [    ] [   ]
        #    [  ]
        # [          ]

        # [    ]      [   ]
        #        [  ] 
        # [    ] [  ] [   ]

        ns, ne = newInterval
        res = []
        appended = False

        for t in intervals:
            s, e = t

            # not touched -- before
            if e < ns:
                res.append(t)
                continue
            # not touched -- after
            elif s > ne:
                if not appended:
                    res.append([ns, ne])
                    appended = True
                res.append(t.copy())
                continue

            # touched insert start
            else:
                ns = min(s, ns)
                ne = max(e, ne)
            
            
        if not appended:
            res.append([ns, ne])

        return res