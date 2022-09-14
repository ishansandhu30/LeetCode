class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val = 0
        if len(tokens) <= 1:
            return int(tokens[0])
        for i in tokens:
            stack.append(i)
            if i == "+":
                index = stack.index(i)
                val = int(stack[index-2])+int(stack[index-1])
                stack[index-2] = val
                stack.pop()
                stack.pop()
                
            elif i == "-":
                index = stack.index(i)
                val = int(stack[index-2])-int(stack[index-1])
                stack[index-2] = val
                stack.pop()
                stack.pop()
            elif i == "*":
                index = stack.index(i)
                val = int(stack[index-2])*int(stack[index-1])
                stack[index-2] = val
                stack.pop()
                stack.pop()
            elif i == "/":
                index = stack.index(i)
                val = int(int(stack[index-2])/int(stack[index-1]))
                stack[index-2] = val
                stack.pop()
                stack.pop()
        return val
                
                