

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