class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
  
        if len(s) == 0:
            return 0

        first_el = 0
        max_len = 1
        lens = []
        for j in range(0, len(s)):
            i = 0
            while first_el + i < j:
                if s[first_el + i] == s[j]:
                    max_len = max(max_len, i+1)
                    first_el += i + 1
                    break
                i+=1
                max_len = max(max_len, i+1)

            max_len = max(max_len, i)
        return max_len

