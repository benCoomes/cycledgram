class Inst(object):
    def __init__(self, string):
        self.string = string

    def cycle(self):
        pass

    def canProceed(self):
        pass

    def __str__(self):
        return self.string

#todo: make subclasses for each instuction type

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
