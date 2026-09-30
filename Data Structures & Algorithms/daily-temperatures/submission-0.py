class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [0]
        i = 1 
        while i < len(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
            i+=1

        return result


        

            

            

        