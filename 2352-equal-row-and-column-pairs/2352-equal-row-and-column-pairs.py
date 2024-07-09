class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        We want to store the chars in each row and column in dicts
        or can directly do the check cause python lol?
        """
        
        columnList = []
        for i in range(len(grid[0])):
            curr = []
            for j in range(len(grid)):
                curr.append(grid[j][i])
            columnList.append(curr)
        count = 0
        for row in grid:
            for col in columnList:
                if row==col:
                    count+=1
        return count
            