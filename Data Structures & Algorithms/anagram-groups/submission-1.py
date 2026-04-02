class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)
            if key not in anagrams.keys():
                anagrams[key] = []
            anagrams[key].append(string) 

        return list(anagrams.values())
    


        