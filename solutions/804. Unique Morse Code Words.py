class Solution:
    morseSym = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
​
    def morseForChar(self, ch):
        index = ord(ch) - ord('a')
        return self.morseSym[index]
​
    def morseForStr(self, str):
        code = ""
        for ch in str:
            code += self.morseForChar(ch)
        return code
        
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = 0
        morseList = []
        for word in words:
            code = self.morseForStr(word)
            if code not in morseList:
                morseList.append(code)
                res += 1
        return res
​
