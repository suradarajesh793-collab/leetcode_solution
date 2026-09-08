class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"
        v=[ch for ch in s if ch in vowels]
        j=len(v)-1
        result=""
        for ch in s:
            if ch in vowels:
                result+=v[j]
                j-=1
            else:
                result+=ch
        return result
                

    