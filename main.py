class Reg(object):

    def __init__(self, num, isBusy=False):
        self.num = num
        self.isBusy = isBusy


# main method start
# ----------------------------------------------

registers = []

for i in range(0, 13):
    nextreg = Reg(i, False)
    registers.append(nextreg)

for r in registers:
    print "R%d busy? : %d" % (r.num, r.isBusy)


print("Enter commands below, enter an empty line when finished")
raw_inst = []
next_line = raw_input();

while(next_line != ''):
    print "You entered: %s" % next_line
    raw_inst.append(next_line)
    next_line = raw_input()

for s in raw_inst:
    print s

inst = []
for s in raw_inst:
    i = getInstruction(s)




