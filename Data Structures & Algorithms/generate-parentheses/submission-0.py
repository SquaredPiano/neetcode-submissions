class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(start, path, stack):
            print(start, path, stack)
            if start == 0:
                dfs(start + 1, path + ["("], stack + 1)
            elif start == 2 * n - 1:
                dfs(start + 1, path + [")"], stack - 1)
            elif stack < 0:
                return
            elif start >= 2 * n:
                if stack == 0:
                    res.append("".join(path))
                return
            else:
                dfs(start + 1, path + ["("], stack + 1)
                dfs(start + 1, path + [")"], stack - 1)

        dfs(0, [], 0)
        return res