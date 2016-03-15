class Reg(object):

    def __init__(self, num, isBusy=False):
        self.num = num
        self.isBusy = isBusy


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