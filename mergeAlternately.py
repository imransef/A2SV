

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = []
        for i in zip_longest(word1, word2, fillvalue ='' ):
            out += list(i)
        return ''.join(out)
