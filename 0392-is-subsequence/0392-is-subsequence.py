from queue import Queue

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        q = Queue()
        if len(s)==0:
            return True
        for letter in s:
            q.put(letter)
        current = q.get()
        for letter in t:
            if letter == current:
                if q.qsize()==0:
                    return True
                current = q.get()
        return False