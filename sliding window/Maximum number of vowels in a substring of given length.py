class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=0
        vowels={'a','e','i','o','u'}
        vowel_count=0
        res=0
        for ch in s[:k]:
            if ch in vowels:
                vowel_count+=1
        res=vowel_count
        for r in range(k,len(s)):
            if s[r] in vowels:
                vowel_count+=1       
            if s[l] in vowels:        
                vowel_count-=1
            l+=1
            res=max(res,vowel_count)
        return res