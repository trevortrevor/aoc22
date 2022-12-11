testing = False
if testing:
    infile = "./input/day10test.txt"
else:
    infile = "./input/day10.txt"
import curses
import asyncio
from curses import wrapper

class SystemClock():
    def __init__(self, system):
        self.totalCycles = 0
        self.system = system
        
    def tick(self):
        self.totalCycles += 1

class CPU():
    def __init__(self, system):
        self.system = system
        self.registers = {"x": 1,
                          "instruction": 0}
        self.interruptFlags = {
            "clockMultiple": False
        }
        self.code = []
        self.instSet = {
            "noop": self.noop,
            "addx": self.addx   
        }
        self.clockInterruptFreq = None
        self.outputBuffer = None
        
    def tick(self, ticks:int=1):
        for tick in range(ticks):
            self.system.tick()
            #print(self.clock.totalCycles)
            self.checkRegInterrupt()
            if True in self.interruptFlags.values():
                self.outputBuffer = self.handleInterrupt()
        return self.registers
        
    def setRegInterrupt(self, start, interval):
        if self.code == []:
            print(f"Error: Load code first")
        else:
            stop = len(self.code) * 2 #Maximum instruction length
        self.clockInterruptFreq = range(start, stop, interval)
        
    def checkRegInterrupt(self):
        if self.clockInterruptFreq:
            if self.system.clock.totalCycles in self.clockInterruptFreq:
                self.interruptFlags['clockMultiple'] = True
                print(f"Clock: {self.system.clock.totalCycles} - X: {self.registers['x']}")
            else:
                self.interruptFlags['clockMultiple'] = False
                
    def handleInterrupt(self):
        if self.interruptFlags['clockMultiple']:
            return self.system.clock.totalCycles * self.registers['x'] 
                    
    def readCode(self, infile):
        with open(infile) as f:
            self.code = [x.strip() for x in f.readlines()]
            
    def reset(self):
        self.__init__()
        
    def parseInst(self, instruction:str):
        instruction = instruction.split()
        try:
            inst = self.instSet[instruction[0]]
        except KeyError:
            print(f"Instruction {instruction} not known")
            inst = None
        try:
            args = instruction[1:]
        except IndexError:
            args = None
        return inst, args
        
    def noop(self, *args):
        self.tick()
        return 1
        
    def addx(self, *args):
        self.tick(2)
        self.registers["x"] += int(args[0])
        return 1
    
    def run(self):
        while self.registers["instruction"] < len(self.code):
            inst, args = self.parseInst(self.code[self.registers['instruction']])
            self.registers['instruction'] += inst(*args)
            if self.outputBuffer is not None:
                yield self.outputBuffer
                self.outputBuffer = None
            
      
class CRT():
    def __init__(self, v:int, h:int, system):
        self.h = h
        self.v = v
        self.lines = [['.' for x in range(h)] for y in range(v)]
        self.totalCycles = 0
        self.system = system
        
    def drawPixel(self, xpos):
        xpos = self.system.clock.totalCycles % self.h
        #print(xpos)
        ypos = self.system.clock.totalCycles // self.h
        #print(ypos)
        sprite = [x + self.system.cpu.registers['x'] for x in range(-1,2)]
        #print(sprite)
        if xpos in sprite:
            self.lines[ypos][xpos] = '#'
            
        
    def drawScreen(self):
        print(" "*self.h+"\n")
        for line in self.lines:
            print(''.join(line))
        print(""*self.h+"\n"*3)
        
            
class ElfComputer():
    def __init__(self):
        self.clock = SystemClock(self)
        self.cpu = CPU(self)
        self.crt = CRT(6, 40, self)
        self.stdout = None
        
    def doCRT(self, xpos):
        self.crt.drawPixel(xpos)
        self.crt.drawScreen()
        
        
    def tick(self):
        self.doCRT(self.cpu.registers['x'])
        self.clock.tick()
        
    
     
    

elfComputer = ElfComputer()
elfComputer.cpu.readCode(infile)   
elfComputer.cpu.setRegInterrupt(20, 40)
outputArr = [x for x in elfComputer.cpu.run()]
print(outputArr)
print(f"Part 1: {sum(outputArr)}")

#print(elfComputer.crt.lines)
    

        
        
        
    
        

        
        