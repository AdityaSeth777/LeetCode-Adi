class Solution:
    def interpret(self, command: str) -> str:
        interpreted_str = ""
        i = 0

        while i < len(command):
            if command[i] == "G":
                interpreted_str += "G"
                i += 1
            elif command[i] == "(" and command[i+1] == ")":
                interpreted_str += "o"
                i += 2
            elif command[i] == "(" and command[i+1] == "a":
                interpreted_str += "al"
                i += 4

        return interpreted_str
