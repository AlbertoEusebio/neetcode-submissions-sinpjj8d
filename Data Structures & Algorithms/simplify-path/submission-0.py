class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = [p for p in path.split('/') if p !='']

        print(folders)

        res = []

        for p in folders:
            if p == '.':
                continue
            elif p=="..":
                if res:
                    res.pop()
                continue
            res.append(p)

        path ="/" + '/'.join(res)
        return path
        