class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        res.append([1])
        for i in range(numRows-1):
            arr = [1]
            for j in range(len(res[i+1-1])-1):
                arr.append(res[i+1-1][j] + res[i+1-1][j+1])
            arr.append(1)
            res.append(arr)
        return res
