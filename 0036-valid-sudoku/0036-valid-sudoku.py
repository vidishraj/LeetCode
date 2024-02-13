class Solution(object):
    def isValidSudoku(self, board):
        checkMap = {}
        column = 0
        row = 0
        
        # Checking individual 3x3 boxes 
        while row < len(board):
            while column < len(board[row]):
                # print(row, column, board[row][column], checkMap)
                if board[row][column] != ".":
                    if checkMap.get(board[row][column]) is not None:
                        return False
                    checkMap[board[row][column]] = 1              
                if row!=0 and column!=0 and (column+1) % 3 == 0 and (row+1) % 3 == 0:
                    row -= 2
                    column+=1
                    checkMap.clear()
                elif column!= 0 and (column+1) % 3 == 0:
                    row += 1
                    column-=2
                else:
                    column+=1
            checkMap={}
            row += 3
            column = 0
        checkMap.clear()
        
        #Checking all the row
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if checkMap.get(board[i][j]) is not None:
                        return False
                    checkMap[board[i][j]] = True
            checkMap.clear()
        checkMap.clear()
        
        # Checking all the columns
        for i in range(len(board[0])):
            for j in range(len(board)):
                if board[j][i] != ".":
                    if checkMap.get(board[j][i]) is not None:
                        return False
                    checkMap[board[j][i]] = True
            checkMap.clear()
        
        return True
