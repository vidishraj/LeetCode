class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        We need a stack to keep track of when we encounter an opening bracket
        When opening bracked, pop from other stack till we encounter closing bracket. Reverse the string attained
        The closing bracket and the opening bracket should be dropped. 
        REPEAT
        """

        stack = [char for char in s]
        stack2= []
        openingBracketCount = 0
        for char in s:
            if char == "(":
                openingBracketCount+=1
        bracketsEncountered=0
        while bracketsEncountered!=openingBracketCount:
            currentChar = stack.pop()
            if currentChar == "(":
                otherStackChar = stack2.pop()
                middleStr= ""
                while otherStackChar!=")":
                    middleStr+=otherStackChar
                    otherStackChar = stack2.pop()
                middleStrRev = middleStr[::-1]
                for char in middleStrRev:
                    stack.append(char)
                while len(stack2)>0:
                    char = stack2.pop()
                    stack.append(char)
                stack2 = []
                bracketsEncountered+=1
            else:
                stack2.append(currentChar)
        if len(stack2)>0:
            return "".join(stack)+"".join(stack2)
        return "".join(stack)