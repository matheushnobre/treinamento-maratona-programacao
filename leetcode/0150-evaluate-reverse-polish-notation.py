class Solution:
    def evalRPN(self, tokens):
        '''
        type tokens: List[str]
        rtype: int
        '''
        stack = []
        operators = ['+', '-', '*', '/']
        
        for element in tokens:
            if element in operators:
                b, a = int(stack.pop()), int(stack.pop())
                match(element):
                    case '+': element = a + b
                    case '-': element = a - b
                    case '*': element = a * b
                    case '/': element = int(a / b)
            else:
                element = int(element)
            stack.append(element)
        return stack[0]
    