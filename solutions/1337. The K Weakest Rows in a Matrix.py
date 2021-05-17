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
