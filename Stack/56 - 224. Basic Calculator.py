# 224. Basic Calculator
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num, sign, result = 0, 1, 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-':
                result += num * sign
                num = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                result, sign = 0, 1
            elif c == ')':
                result += num * sign
                result *= stack.pop()  # sign before '('
                result += stack.pop()  # result before '('
                num = 0
        result += num * sign
        return result