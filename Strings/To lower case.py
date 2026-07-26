class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=""
        for ch in s:
            if ch.isupper():
                ch=ord(ch)+32
                ans+=chr(ch)
            else:
                ans+=ch
        return ans