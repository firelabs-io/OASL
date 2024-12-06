import sys

#virtual machine for asm
class vm:
    def __init__(self):
        self.reg = {'AX': 0}
        self.op = 0
    
    def runline(self, line):
        command = line.split(' ')
        if command[0] == 'adax':
            self.reg['AX'] += int(command[1])
        print(self.reg)
    def runProgram(self, program):
        while self.op < len(program):
            self.runline(program[self.op])
            self.op += 1

if __name__ == '__main__':
    filename = sys.argv[1]
    program = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            program.append(line)
    
    myvm = vm()
    myvm.runProgram(program)
