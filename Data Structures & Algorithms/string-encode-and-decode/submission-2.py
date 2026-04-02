class Solution:

    def encode(self, strs: List[str]) -> str:
        total_str = ""
        parts = []
        for string in strs:
            parts.append(f"{len(string)}#{string}")
        return "".join(parts)

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