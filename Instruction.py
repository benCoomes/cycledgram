class Inst(object):
    def __init__(self):
        pass

    def cycle():
        pass

    def __str__(self):
        pass

#todo: make subclasses for each instuction type

class Add_inst(Inst):
    def __init__(self, reg_list):
        self.source_regs = reg_list[1:3]
        self.product_regs = reg_list[0]

    # what is the difference between __srt__ and __repr__ ?
    def __str__(self):
        return "add r%r r%r r%r" % (self.product_regs, self.source_regs[0], self.source_regs[1])

    def __repr__(self):
        return "add r%r r%r r%r" % (self.product_regs, self.source_regs[0], self.source_regs[1])


class Sub_inst(Inst):
    def __init__(self, reg_list):
        self.source_regs = reg_list[1:3]
        self.product_regs = reg_list[0]

    def __str__(self):
        return "sub r%r r%r r%r" % (self.product_regs, self.source_regs[0], self.source_regs[1])

    def __repr__(self):
        return "sub r%r r%r r%r" % (self.product_regs, self.source_regs[0], self.source_regs[1])

class Load_inst(Inst):
    def __init__(self, reg_list):
        self.source_regs = reg_list[1]
        self.product_regs = reg_list[0]

    def __str__(self):
        return "lw  r%r r%r" % (self.product_regs, self.source_regs)

    def __repr__(self):
        return "lw  r%r r%r" % (self.product_regs, self.source_regs)


class Store_inst(Inst):
    def __init__(self, reg_list):
        self.source_regs = reg_list[1]
        self.product_regs = reg_list[0]

    def __str__(self):
        return "sw  r%r r%r" % (self.product_regs, self.source_regs)

    def __repr__(self):
        return "sw  r%r r%r" % (self.product_regs, self.source_regs)
