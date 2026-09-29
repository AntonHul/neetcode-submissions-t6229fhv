class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        nums = [int(tokens[0]), int(tokens[1])]
        i = 2
        while i < len(tokens):
            if tokens[i] == "+":
                nums[-2] += nums[-1]
                nums.pop()
            elif tokens[i] == "*":
                nums[-2] *= nums[-1]
                nums.pop()
            elif tokens[i] == "-":
                nums[-2] -= nums[-1] 
                nums.pop()
            elif tokens[i] == "/":
                nums[-2] /= nums[-1] 
                nums[-2] = int(nums[-2])
                nums.pop()
            else:
                nums.append(int(tokens[i]))
            i+=1
        return nums[0]
            
        