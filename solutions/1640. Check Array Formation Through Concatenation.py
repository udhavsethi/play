class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        compareList = []
        for i in range(len(arr)):
            for sublist in pieces:
                if sublist[0] == arr[i]:     # match found with first element of a sublist
                    compareList.append(sublist)
                    i += len(sublist)
                    break
        flat_list = [item for sublist in compareList for item in sublist]
        if flat_list == arr:
            return True
        return False
