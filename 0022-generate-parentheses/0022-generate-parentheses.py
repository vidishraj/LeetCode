class Solution:
    res:list
    def rec(self, n , openP, closeP, currentString):
        if openP>n or closeP>n:
            return 
        if openP==n and closeP==n:
            self.res.append(currentString)
            return 
        if openP<n:
            # Add open parentheses
            self.rec(n, openP+1, closeP, currentString+"(")
        if closeP<n and openP>closeP:
            self.rec(n, openP, closeP+1, currentString+")")
        
    def generateParenthesis(self, n: int) -> List[str]:
        # We can add an open parenthese at any time, we can add closing parentheses only when opening paraenthese used>closing parenthese used
        self.res = []
        self.rec(n, 0, 0, "")
        return self.res
        