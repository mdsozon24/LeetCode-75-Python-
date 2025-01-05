class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for c in s:
            if stk and c == "]":
                x = ""
                while stk and stk[-1] != "[":
                    x = stk.pop() + x
                stk.pop()
                y = ""
                while stk and stk[-1].isdigit():
                    y = stk.pop() + y
                n = int(y)
                stk.append(x * n)
            else:
                stk.append(c)
        return "".join(stk)
