import asyncio
from collections import deque
import queue
testing = False

if testing:
    infile = "./input/day6test.txt"
else:
    infile = "./input/day6.txt"
 
def inputData(filename):
    with open(infile) as f:
        for line in f.readlines():
            yield line
   
class Communicator():
    def __init__(self):
        self.inBuffer = queue.Queue()
        self.pos = 0
        self.packetdata = deque(maxlen = 4)
        self.messagedata = deque(maxlen = 14)
        self.packetPos = None
        self.messagePos = None
        
    def recieve(self, stream:str) -> None:
        for char in list(stream.strip()):
            self.inBuffer.put(char)
       
    def testPacket(self) -> bool:
        return len(set(list(self.packetdata))) == 4
    
    def testMessage(self) -> bool:
        return len(set(list(self.messagedata))) == 14
            
    def advance(self):
        self.packetdata.append(self.inBuffer.get())
        self.messagedata.append(self.packetdata[-1])
        self.pos += 1
        
    def decode(self):
        while (self.packetPos == None and self.messagePos == None) or not self.inBuffer.empty():
            if self.testPacket() and self.packetPos == None:
                self.packetPos = self.pos
                print(f"Packet header at position: {self.packetPos}")
            if self.testMessage() and self.messagePos == None:
                self.messagePos = self.pos
                print(f"Message header at position: {self.messagePos}")
            self.advance()
        return self.packetPos, self.messagePos
        
    

            

for line in inputData(infile):
    elfComms = Communicator()
    elfComms.recieve(line)
    elfComms.decode()

    
        
        
