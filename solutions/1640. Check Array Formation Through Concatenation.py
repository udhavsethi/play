class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        compareList = []
        i=0
        while i<len(arr):
            found = False
            for sublist in pieces:
                if sublist[0] == arr[i]:     # match found with first element of a sublist
                    found = True
                    compareList.extend(sublist)
                    i += len(sublist)
                    pieces.remove(sublist)
                    break
            if not found:
                return False
        if compareList == arr:
            return True
        return False
