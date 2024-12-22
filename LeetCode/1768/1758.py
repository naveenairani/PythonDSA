class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
    	res = []
    	value = max(len(str1), len(str2))
    	for i in range(value):
    		if i < len(word1):
    			res.append(word1[i])
    		if i < len(word2):
    			res.append(word2[i])
    	result = "".join(res)
    	return result