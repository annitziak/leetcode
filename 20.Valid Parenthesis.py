class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Map of matching brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        opening = []  
        for char in s:
            if char in bracket_map.values():  #if its opening
                opening.append(char)
            elif char in bracket_map:  #if in closing
            ## Check if the stack is empty or the top of the stack doesn't match
            #opening.pop() is used to remove the most recent unmatched opening bracket
                if not opening or opening.pop() != bracket_map[char]:
                    return False
            else:
                return False  #wrong char

        return not opening