
#### Register.py ####
class Reg(object):

    def __init__(self, num, isBusy=False):
        self.num = num
        self.isBusy = isBusy

    def __str__(self):
        return "r%d" % self.num


class RegisterSet(object):

    def __init__(self, regCount):
        self.regCount = regCount
        self.__registers = []
        for i in range(0,regCount):
            self.__registers.append(Reg(i, False))

    def get(self, index):
        if(index < 0 or index >= self.regCount):
            print "Error: index of %d out of range in RegisterSet.get(index)" % index
            return None
        return self.__registers[index]



#### Instruction.py ####

class Inst(object):
    def __init__(self, string):
        self.string = string

    def cycle(self):
        pass

    def canProceed(self):
        pass

    def __str__(self):
        return self.string

class Add_inst(Inst):
    def __init__(self, reg_list, string):
        super(Add_inst, self).__init__(string)
        self.source_regs = reg_list[1:3]
        self.product_reg = reg_list[0]
        self.stages = {
            -1: '  ', # wait or unstarted
            0 : 'IF', 
            1 : 'ID',
            2 : 'EX',
            3 : 'MD',
            4 : 'WB',
            5 : '' # finished
        }
        self.currentStage = -1

    def cycle(self):
        if self.currentStage == 0:
            if self.canProceed():
                self.currentStage += 1
                self.product_reg.isBusy = True
            else:
                return self.stages[-1]

        elif self.currentStage == 3:
            self.currentStage += 1
            self.product_reg.isBusy = False
            
        elif self.currentStage == 5:
            pass

        else:
            self.currentStage += 1

        return self.stages[self.currentStage]

    def canProceed(self):
        idle_sregs = True
        for r in self.source_regs:
            if r.isBusy:
                idle_sregs = False
        return idle_sregs


class Sub_inst(Inst):
    def __init__(self, reg_list, string):
        super(Sub_inst, self).__init__(string)
        self.source_regs = reg_list[1:3]
        self.product_reg = reg_list[0]
        self.stages = {
            -1: '  ', # wait or unstarted
            0 : 'IF', 
            1 : 'ID',
            2 : 'EX',
            3 : 'MD',
            4 : 'WB',
            5 : '' # finished
        }
        self.currentStage = -1

    def cycle(self):
        if self.currentStage == 0:
            if self.canProceed():
                self.currentStage += 1
                self.product_reg.isBusy = True
            else:
                return self.stages[-1]

        elif self.currentStage == 3:
            self.currentStage += 1
            self.product_reg.isBusy = False
            
        elif self.currentStage == 5:
            pass

        else:
            self.currentStage += 1

        return self.stages[self.currentStage]

    def canProceed(self):
        idle_sregs = True
        for r in self.source_regs:
            if r.isBusy:
                idle_sregs = False
        return idle_sregs


class Load_inst(Inst):
    def __init__(self, reg_list, string):
        super(Load_inst, self).__init__(string)
        self.source_regs = reg_list[1]
        self.product_reg = reg_list[0]
        self.stages = {
            -1: '  ', # wait or unstarted
            0 : 'IF', 
            1 : 'ID',
            2 : 'EX',
            3 : 'MD',
            4 : 'WB',
            5 : '' # finished
        }
        self.currentStage = -1

    def cycle(self):
        if self.currentStage == 0:
            if self.canProceed():
                self.currentStage += 1
                self.product_reg.isBusy = True
            else:
                return self.stages[-1]

        elif self.currentStage == 3:
            self.currentStage += 1
            self.product_reg.isBusy = False
            
        elif self.currentStage == 5:
            pass

        else:
            self.currentStage += 1

        return self.stages[self.currentStage]

    def canProceed(self):
        return not self.source_regs.isBusy and not self.product_reg.isBusy


class Store_inst(Inst):
    def __init__(self, reg_list, string):
        super(Store_inst, self).__init__(string)
        self.source_regs = reg_list[0:2]
        self.product_reg = None
        self.stages = {
            -1: '  ', # wait or unstarted
            0 : 'IF', 
            1 : 'ID',
            2 : 'EX',
            3 : 'MD',
            4 : 'WB',
            5 : '' # finished
        }
        self.currentStage = -1

    def cycle(self):
        if self.currentStage == 0:
            if self.canProceed():
                self.currentStage += 1
            else:
                return self.stages[-1]
            
        elif self.currentStage == 5:
            pass

        else:
            self.currentStage += 1

        return self.stages[self.currentStage]

    def canProceed(self):
        idle_sregs = True
        for r in self.source_regs:
            if r.isBusy:
                idle_sregs = False
        return idle_sregs


#### Processor.py ####

class CPU(object):
    def __init__(self):
        self.instructions = []
        self.output = []
        # lists should only ever hold a single instruction object
        self.stages = {
            0 : 'IF', 
            1 : 'ID',
            2 : 'EX',
            3 : 'MD',
            4 : 'WB'
        }
        self.win_start = 0
        self.win_end = 1
        self.win_max = 5

    def addInst(self, instruction_list):
        for i in instruction_list:
            self.instructions.append(i)
            self.output.append(str(i) + "  ")
    
    def tick(self):
        # go throguh all inst
        inst_finished = False
        if_open = True
        for inst in self.instructions:
            # default value for inst before window
            inst_out = ""
            #if inst is in window, call cycle on inst and get the output
            if(inst in self.instructions[self.win_start:self.win_end]):
                if if_open:
                    inst_out = inst.cycle()
                else:
                    inst_out = '  '
                if(inst_out == 'WB'):
                    inst_finished = True
                if(inst_out == '  '):
                    if_open = False

            #if inst is after window, set output to appropriate spacing
            elif(inst in self.instructions[self.win_end:]):
                inst_out = "  "
            #write output for inst to coor. entry in self.output
            self.output[self.instructions.index(inst)] += inst_out + " "
        #update window values for next tick
        if inst_finished:
            self.win_start += 1

        if (self.win_end - self.win_start) < self.win_max and if_open:
            self.win_end += 1

        return self.win_start != len(self.instructions)


    def printPipeline(self):
        for line in self.output:
            print line

regs = RegisterSet(10)
# read in lines, parse as instructions
raw_inst = []
next_line = raw_input();

while(next_line != ''):
    raw_inst.append(next_line)
    next_line = raw_input()

inst_list = []
for s in raw_inst:
    parts = s.split()
    if(len(parts) == 2):
        parts[1] = parts[1].split(',')
    else:
        print "Error: bad string format for instruction input"


    if(parts[0] == 'add'):
    #make add
        inst_regs = []
        # uncheked assumption
        for r in parts[1]:
            r_num = int(r[1])
            inst_regs.append(regs.get(r_num))
        inst_list.append(Add_inst(inst_regs, s))
        #cpu.addInst(Add_inst(inst_regs))

    elif(parts[0] == 'sub'):
        #make sub
        inst_regs = []
        # uncheked assumption
        for r in parts[1]:
            r_num = int(r[1])
            inst_regs.append(regs.get(r_num))
        inst_list.append(Sub_inst(inst_regs, s))
        #cpu.addInst(Sub_inst(inst_regs))

    elif(parts[0] == 'lw'):
        #make lw
        inst_regs = []
        r = parts[1]
        inst_regs.append(regs.get(int(r[0][1])))
        #assumption about how offset works: 
        # offset + regnum = actual reg num
        # probably wrong, CHECK THIS
        inst_regs.append(regs.get(int(r[1][0]) + int(r[1][3])))
        inst_list.append(Load_inst(inst_regs, s))
        #cpu.addInst(Load_inst(inst_regs))   

    elif(parts[0] == 'sw'):
        #make sw
        inst_regs = []
        r = parts[1]
        inst_regs.append(regs.get(int(r[0][1])))
        #assumption about how offset works: 
        # offset + regnum = actual reg num
        # probably wrong, CHECK THIS
        inst_regs.append(regs.get(int(r[1][0]) + int(r[1][3])))
        inst_list.append(Store_inst(inst_regs, s))
        #cpu.addInst(Store_inst(inst_regs))

    else:
        print "ERROR! Unrecognized instruction"


cpu = CPU()
cpu.addInst(inst_list)
while cpu.tick():
    pass
cpu.printPipeline()