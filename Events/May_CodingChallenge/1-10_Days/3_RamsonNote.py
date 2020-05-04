class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for c in ransomNote:
            if not c in magazine: return False
            magazine.pop(magazine.index(c))
        return True
