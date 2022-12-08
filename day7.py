testing = False
from queue import Queue
import pprint

if testing:
    infile = "./input/day7test.txt"
else:
    infile = "./input/day7.txt"

indata = Queue()
with open(infile) as f:
    for line in f.readlines():
        indata.put(line.strip())

class Directory(dict):
    def __init__(self, parent, name):
        self.parent = parent
        self._size = 0
        self._flat = {}
        self.name = name

    def path(self):
        self._path = self.name
        if self.parent != None:
            return self.parent.path() + self.name + "/"
        else:
            return "/"
    
    def add(self, object, size:int):
        self[object] = size
        
    @property    
    def size(self):
        return self._size
    
    def dir(self):
        dirListing = {}
        for key, val in self.items():
            if type(val) == Directory:
                dirListing[key] = val.dir()
            else:
                dirListing[key] = val
        return dirListing
    def subFolders(self):
        subFolders = {}
        for key, val in self.items():
            if type(val) == Directory:
                subFolders[key] = val
        return subFolders
                
    def getSize(self):
        self._size = 0
        for subObj in self.values():
            if type(subObj) == Directory:
                self._size += subObj.getSize()
            else:
                self._size += subObj
        return self._size
    
    def findDirAbove(self, minSize:int):
        folders = {}
        if self.getSize() >= minSize:
            folders[self.name] = self.getSize()
            for key, val in self.subFolders().items():
                folders = folders | val.findDirAbove(minSize)
        return folders
    
    def findDirBelow(self, maxSize:int):
        folders = {}
        if self.getSize() <= maxSize:
            folders[self.name] = self.getSize()
        for key, val in self.subFolders().items():
            folders = folders | val.findDirBelow(maxSize)
        return folders
                 
class Device():
    def __init__(self, commands:Queue):
        self.disk = Directory(None, "/")
        self.wd = self.disk
        self.commands = commands
        self.expectedOutput = None
        
    def nextCommand(self) -> str:
        return self.commands.get()
                
    def inputCommand(self, cmd, arg=None):
        if cmd == "cd":
            self.cd(arg)
        elif cmd == "ls":
            self.ls()          
         
    def cd(self, directory:str):
        if directory == "..":
            self.wd = self.wd.parent
        elif directory == "/":
            self.wd = self.disk
        else:
            try:
                self.wd = self.wd[directory]
            except KeyError:
                self.disk[directory] = Directory(self.wd)
            
    def ls(self):
        self.expectedOutput = "ls"
               
    def parseOutput(self, output:list):
        if self.expectedOutput == "ls":
            if output[0] == "dir":
                self.wd[output[1]] = Directory(self.wd, output[1])
            else:
                self.wd.add(output[1], int(output[0]))
        else:
            print(f"Unexpected output {output}")
                                   
    def run(self):
        while not self.commands.empty():
            command = self.nextCommand()
            command = command.split(" ")
            if command[0] == "$":
                self.expectedOutput = None
                self.inputCommand(*command[1:])
            else:
                self.parseOutput(command)
                             
        
elfDevice = Device(indata)
elfDevice.run()

p1total = 0
p1Folders = elfDevice.disk.findDirBelow(100000)
p1total = sum(p1Folders.values())
print(f"Part 1: {p1total}")
TOTALSIZE = 70000000
REQFREE = 30000000
requiredsize = elfDevice.disk.getSize() - (TOTALSIZE - REQFREE)
p2Folders =elfDevice.disk.findDirAbove(requiredsize)
p2total = min(p2Folders.values())
print(f"Part 2: {p2total}")



    
            