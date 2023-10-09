class BrainfuckCompiler:
    def __init__(self, tape_size=30000):
        self.memory = [0] * tape_size
        self.pointer = 0
        self.output = ''

    def compile(self, code):
        self.pointer = 0
        self.output = ''
        stack = []
        input_index = 0

        for char in code:
            if char == '>':
                self.pointer += 1
                if self.pointer == len(self.memory):
                    self.memory.append(0)
            elif char == '<':
                self.pointer -= 1
                if self.pointer < 0:
                    raise ValueError("Pointer moved beyond tape boundaries.")
            elif char == '+':
                self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
            elif char == '-':
                self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
            elif char == '.':
                self.output += chr(self.memory[self.pointer])
            elif char == ',':
                if input_index < len(input_data):
                    self.memory[self.pointer] = ord(input_data[input_index])
                    input_index += 1
                else:
                    raise ValueError("Not enough input data.")
            elif char == '[':
                stack.append(len(self.output))
            elif char == ']':
                if self.memory[self.pointer] == 0:
                    stack.pop()
                else:
                    position = stack[-1]
                    code_to_repeat = code[position:]
                    self.compile(code_to_repeat)

        return self.output


if __name__ == "__main__":
    bf_compiler = BrainfuckCompiler()
    bf_code = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++.>++++.------.--------.>+.>."
    input_data = ""
    result = bf_compiler.compile(bf_code)
    print(result)