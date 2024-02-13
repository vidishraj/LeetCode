class Solution(object):

    def countNeighbours(self, i, j, board):
        count = 0
        if j + 1 < len(board[0]) and (board[i][j + 1] == 1 or board[i][j + 1] == -2):
            count += 1
        if j - 1 >= 0 and (board[i][j - 1] == 1 or board[i][j-1]==-2):
            count += 1
        if i - 1 >= 0 and j - 1 >= 0 and (board[i - 1][j - 1] == 1 or board[i - 1][j - 1] == -2):
            count += 1
        if i - 1 >= 0 and j + 1 < len(board[0]) and (
                board[i - 1][j + 1] == 1 or board[i - 1][j + 1] == -2):
            count += 1
        if i + 1 < len(board) and j + 1 < len(board[0]) and (
                board[i + 1][j + 1] == 1 or board[i + 1][j + 1] == -2):
            count += 1
        if j - 1 >= 0 and i + 1 < len(board) and (
                board[i + 1][j - 1] == 1 or board[i + 1][j - 1] == -2):
            count += 1
        if i + 1 < len(board) and (board[i + 1][j] == 1 or board[i + 1][j] == -2):
            count += 1
        if i - 1 >= 0 and (board[i - 1][j] == 1 or board[i - 1][j] == -2):
            count += 1
        return count

    def gameOfLife(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    # dead case
                    count = self.countNeighbours(i, j, board)
                    if count == 3:
                        board[i][j] = -1
                elif board[i][j]==1:
                    # live case
                    count = self.countNeighbours(i, j, board)
                    if count < 2 or count > 3:
                        board[i][j] = -2 
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==-2:
                    board[i][j]=0
                if board[i][j]==-1:
                    board[i][j]=1