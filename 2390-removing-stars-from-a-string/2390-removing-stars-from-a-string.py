class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for letter in s:
            if letter =="*":
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)