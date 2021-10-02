import numpy as np
​
class Solution:
    
    def getMap(self):
        valid = {}
        for i in range(1,10):
            valid[str(i)] = False
        return valid
    
    def isValidList(self, lst: List[str]) -> bool:
        valid = self.getMap()
        for num in lst:
            if num == ".":
                continue
            elif num in valid and not valid[num]:
                    valid[num] = True
            else:
                return False
        return True
​
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        board = np.array(board)
        # check cols
        for m in range(rows):
            col = board[:,m]
            if not self.isValidList(col):
                return False
​
        # check rows
        for n in range(cols):
            row = board[n]
            if not self.isValidList(row):
                return False
        
        # check sub-boxes
        for i in range(0, rows, 3):
            for j in range(0, cols, 3):
                subbox = board[i:i+3,j:j+3]
                if not self.isValidList(subbox.flatten()):
                    return False
​
        return True
        
        
