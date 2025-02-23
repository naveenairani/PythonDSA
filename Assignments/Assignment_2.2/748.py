class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        f=collections.Counter()
        for c in licensePlate.lower():
            if c.isalpha():
                f[c]+=1
        shortest="z"*20
        for word in words:
            wf=collections.Counter(word)

            if (f&wf)==f:
                if len(word)<len(shortest):
                    shortest=word
        return shortest