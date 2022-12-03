testing = False
if testing:
    ifile = "./input/day2test.txt"
else:
    ifile = "./input/day2.txt"
    
idata = [] 
with open(ifile) as f:
    for line in f.readlines():
        idata.append([x.strip("\n") for x in line.split(" ")])
        


class Hand():
    def play(self, opponent):
        if opponent.type == self.type:
            return 3 + self.value
        elif self.winsAgainst == opponent.type:
            return 6 + self.value
        elif self.losesTo == opponent.type:
            return 0 + self.value
    def x(self):
        return self.winsAgainst
    def y(self):
        return self.type
    def z(self):
        return self.losesTo  

class Rock(Hand):
    winsAgainst = 'scissors'
    losesTo = 'paper'
    def __init__(self):
        self.value = 1
        self.type = 'rock'
        
class Paper(Hand):
    winsAgainst = 'rock'
    losesTo = 'scissors'
    def __init__(self):
        self.value = 2
        self.type = 'paper'
        
class Scissors(Hand):
    winsAgainst = 'paper'
    losesTo = 'rock'
    def __init__(self):
        self.value = 3
        self.type = 'scissors'
        
classLookup = {
    "rock": Rock(),
    "paper": Paper(),
    "scissors": Scissors()
}
        
c1Lookup = {
    "A": Rock(),
    "B": Paper(),
    "C": Scissors()
}

c2Lookup = {
    "X": Rock(),
    "Y": Paper(),
    "Z": Scissors()
}


totalscore = 0
for p1, p2 in idata:
    p1h = c1Lookup[p1]
    p2h = c2Lookup[p2]
    #print(f"{p1h.type} plays {p2h.type}, scoring {p2h.play(p1h)}")
    totalscore += p2h.play(p1h)

print(f"Part 1 - Total Score: {totalscore}")

totalscore = 0
for p1, result in idata:
    p1h = c1Lookup[p1]
    if result == "X":
        p2h = classLookup[p1h.x()]
    elif result == "Y":
        p2h = classLookup[p1h.y()]
    elif result == "Z":
        p2h = classLookup[p1h.z()]
    print(f"{p1h.type} plays {p2h.type}, scoring {p2h.play(p1h)}")
    totalscore += p2h.play(p1h)

print(f"Part 2 - Total Score: {totalscore}")
    
    
    
