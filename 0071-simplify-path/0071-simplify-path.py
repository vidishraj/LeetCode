class Solution:
    def simplifyPath(self, path: str) -> str:
        start = 1
        result = ""
        currentBox = ""
        path = re.sub('[/]{2,}','/', path)
        while start < len(path):
            while path[start] != "/":
                currentBox += path[start]
                start += 1
                if start == len(path):
                    break
            start += 1
            if currentBox == ".":
                start = start
            elif currentBox == "..":
                lastIndex = len(result) - 1
                while len(result)>0 and result[-1]!='/':
                    result = result[:-1]
                result = result[:-1]
            else:
                result += f"/{currentBox}"
            # print(result, currentBox, start)
            currentBox = ""
        if result=="":
            return "/"
        return result.replace("//","/")