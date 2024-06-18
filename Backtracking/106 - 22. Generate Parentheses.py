class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(opn, clse, seq, res):
            if opn < n:
                dfs(opn + 1, clse, seq + '(', res)
            
            if clse < opn:
                dfs(opn, clse + 1, seq + ')', res)
            
            if opn == n and clse == n:
                res += seq,
        
        res = []
        dfs(0, 0, '', res)
        return res