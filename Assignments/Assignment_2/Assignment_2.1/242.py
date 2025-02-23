class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        fre1 = {}
        fre2 = {}
        for ch in s:
            if ch in fre1:
                fre1[ch] += 1
            else:
                fre1[ch] = 1
        for ch in t:
            if ch in fre2:
                fre2[ch] += 1
            else:
                fre2[ch] = 1
        for key in fre1:
            if key not in fre2 or fre1[key] != fre2[key]:
                return False
        return True