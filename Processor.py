class Cpu(object):
    def __init__():
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
        self.win_end = 4

    def addInst(self, instruction_list):
        for i in instruction_list
            self.instuctions.append(i)
            self.output.append(str(i))

    def tick(self):
        # go throguh all inst
        #if inst is in window, call cycle on inst and get the output
        #if inst is before window, set output to ""
        #if inst is after window, set output to appropriate spacing
        #write output for inst to coor. entry in self.output
