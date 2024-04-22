class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        
        for element in path:
            if element == '..' and len(stack) != 0:
                stack.pop()
            elif element not in ['.', '', '..']:
                stack.append(element)
                
        return '/' + '/'.join(stack)