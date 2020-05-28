class Solution:
    def arrangeWords(self, text: str) -> str:
        s = text.split()
        s.sort(key = lambda x: len(x))
        return " ".join(s).capitalize()
        
