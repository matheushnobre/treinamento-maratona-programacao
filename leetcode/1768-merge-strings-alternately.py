class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = '' 
        for i in range(min(len(word1), len(word2))):
            word3 += word1[i]
            word3 += word2[i]
        if len(word1) > len(word2):
            word3 += word1[i+1:]
        else:
            word3 += word2[i+1:]
        return word3