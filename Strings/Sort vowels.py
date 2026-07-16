class Solution:
    def sortVowels(self, s: str) -> str:
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        vowels2=[]

        for i in range(len(s)):
            if s[i] in vowels:
                vowels2.append(s[i])
        vowels2.sort()
        t=[]
        j=0
        for i in range(len(s)):
            if s[i] not in vowels:
                t.append(s[i])
            else:
                t.append(vowels2[j])
                j+=1
        return "".join(t)

           
            