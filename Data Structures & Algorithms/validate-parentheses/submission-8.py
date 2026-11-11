class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_pair = {']':'[', ')': '(', '}': '{'}

        for c in s:
            if c in valid_pair:
                if not stack:
                    return False

                if stack[-1] == valid_pair[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False
