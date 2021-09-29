class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        kweakest = []
        rowIndices = list(range(len(mat)))
        for col in range(len(mat[0])):
            for rowIndex in rowIndices[:]:
                if mat[rowIndex][col] == 0:
                    kweakest.append(rowIndex)
                    rowIndices.remove(rowIndex)
                    if len(kweakest) == k:
                        return kweakest
        kweakest.extend(rowIndices)
        return kweakest[:k]
​
    
#############################################
​
#  revisit
​
# Used `for rowIndex in rowIndices[:]` and not `for rowIndex in rowIndices`
# because otherwise the iteration fails
# ref: https://stackoverflow.com/a/1207427/8743880
​
# Alternate Solution
​
# Add content of each row; create tuple (rowIndex, rowSum) 
# sort on rowSum; sort on rowIndex, return top k rowIndex
