import Instruction
import Registers
import Processor


# main method start
# ----------------------------------------------


# make cpu 
"""
cpu object holds all instructions. 
cpu.addInst(Inst) adds an instruction to the instruction list
cpu.tick() runs one cpu clock cycle (described in my notes)
cpu.printPipeline() prints a history of executed instructions and 
the order that they were processed in the pipeline. (output required
for project). 
"""

# process input to generate instructions
# need to make a set of registers to give instructions as they are made
regs = Registers.RegisterSet(10)
# read in lines, parse as instructions
print("Enter commands below, enter an empty line when finished")
raw_inst = []
next_line = raw_input();

while(next_line != ''):
    print "You entered: %s" % next_line
    raw_inst.append(next_line)
    next_line = raw_input()

inst_list = []
for s in raw_inst:
    parts = s.split()
    if(len(parts) == 2):
        parts[1] = parts[1].split(',')
    else:
        print "Error: bad string format for instruction input"

    print parts

    if(parts[0] == 'add'):
    #make add
        inst_regs = []
        # uncheked assumption
        for r in parts[1]:
            r_num = int(r[1])
            inst_regs.append(regs.get(r_num))
        inst_list.append(Instruction.Add_inst(inst_regs))
        #cpu.addInst(Add_inst(inst_regs))

    elif(parts[0] == 'sub'):
        #make sub
        inst_regs = []
        # uncheked assumption
        for r in parts[1]:
            print r
            r_num = int(r[1])
            inst_regs.append(regs.get(r_num))
        inst_list.append(Instruction.Sub_inst(inst_regs))
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
        inst_list.append(Instruction.Load_inst(inst_regs))
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
        inst_list.append(Instruction.Store_inst(inst_regs))
        #cpu.addInst(Store_inst(inst_regs))

    else:
        print "ERROR! Unrecognized instruction"



#create instance of a subclass of instruction (add, lw, sub, sw)
#add the created inst to the cpu list
cpu = Processor.CPU()
cpu.addInst(inst_list)
while cpu.tick():
    pass
cpu.printPipeline()


#run the cpu while there are still unexecuted instructions
# cpu.unex_inst keeps track of this

#when all inst have executed, print pipeline








