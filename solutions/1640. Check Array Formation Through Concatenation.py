class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        compareList = []
        for i in range(len(arr)):
            for sublist in pieces:
                if sublist[0] == arr[i]:     # match found with first element of a sublist
                    compareList.extend(sublist)
                    i += len(sublist)
                    break
        if compareList == arr:
            return True
        return False
