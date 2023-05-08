class Triple:
    def __init__(self, op, arg1=None, arg2=None):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2

    def __str__(self):
        if self.arg2 is None:
            return f'({self.op}, {self.arg1})'
        else:
            return f'({self.op}, {self.arg1}, {self.arg2})'

class IntermediateCodeGenerator:
    def __init__(self):
        self.code = []
        self.temp_count = 0
        self.label_count = 0

    def new_temp(self):
        temp = f't{self.temp_count}'
        self.temp_count += 1
        return temp

    def new_label(self):
        label = f'L{self.label_count}'
        self.label_count += 1
        return label

    def gen(self, op, arg1=None, arg2=None):
        result = self.new_temp()
        self.code.append(Triple(op, arg1, arg2))
        return result

    def assign(self, arg):
        return self.gen('=', arg)

    def conditional_jump(self, op, arg1, arg2, label):
        self.code.append(Triple(op, arg1, arg2))
        self.code.append(Triple('goto', label))

    def unconditional_jump(self, label):
        self.code.append(Triple('goto', label))

    def label(self, label):
        self.code.append(Triple('label', label))

    def print_code(self):
        for triple in self.code:
            print(triple)

if __name__ == '__main__':
    icg = IntermediateCodeGenerator()
    a = icg.assign(5)
    b = icg.assign(6)
    c = icg.gen('+', a, b)
    icg.conditional_jump('<', c, 10, 'L1')
    icg.assign(0)
    icg.unconditional_jump('L2')
    icg.label('L1')
    icg.assign(1)
    icg.label('L2')
    icg.print_code()
