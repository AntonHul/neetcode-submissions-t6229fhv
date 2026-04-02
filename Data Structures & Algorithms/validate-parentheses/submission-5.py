class Solution:
    def isValid(self, s: str) -> bool:
        dicts = {
            '(': 1,
            ')': -1,
            '{': 2, 
            '}': -2, 
            '[': 3, 
            ']': -3
        }     
        stack = []
        for char in s:
            val = dicts[char]
            if len(stack) == 0:
                stack.append(char)
            elif dicts[stack[-1]] == - val:
                if val > 0:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False