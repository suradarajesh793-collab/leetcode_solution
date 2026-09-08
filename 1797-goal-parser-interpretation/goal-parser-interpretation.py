class Solution:
    def interpret(self, command: str) -> str:
        s=command
        for ch in command:
            s=s.replace("()","o")
            s=s.replace("(","")
            s=s.replace(")","")
        return s

        