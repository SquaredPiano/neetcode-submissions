class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(start, path, stack):
            if stack < 0:
                return
            elif start >= 2 * n:
                if stack == 0:
                    res.append("".join(path.copy()))
                return
            else:
                path.append("(")
                dfs(start + 1, path, stack + 1)
                path.pop()
                path.append(")")
                dfs(start + 1, path, stack - 1)
                path.pop()

        dfs(0, [], 0)
        return res