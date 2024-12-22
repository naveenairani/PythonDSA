class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        def gcd(str1, str2):
            minval = min(len(str1), len(str2))
            for i in range(minval, 0, -1):
                if len(str1) % i == 0 and len(str2) % i ==0:
                    return i
            return 1
        return str1[:gcd(str1, str2)]