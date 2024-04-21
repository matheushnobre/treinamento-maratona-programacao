class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = '([{'
        close_brackets = ')]}'
        opens = list()
        for b in s:
            if b in open_brackets:
                opens.append(b)
            else:
                if len(opens) == 0: return False
                if open_brackets.index(opens.pop()) != close_brackets.index(b): return False
        return True if len(opens) == 0 else False