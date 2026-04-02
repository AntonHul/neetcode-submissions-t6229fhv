class Solution:

    def encode(self, strs: List[str]) -> str:
        total_str = ""
        for string in strs:
            total_str += str(len(string))
            total_str += "#"
            total_str += string
        return total_str

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i < len(s):
            num = ""
            while s[i] != "#":
                num += s[i]
                i+=1
            lens = int(num) + 1
            strs.append(s[i+1:i+lens])
            i+=lens
        return strs