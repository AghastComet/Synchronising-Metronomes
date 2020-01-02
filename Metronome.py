from matplotlib import pyplot as plt
import math

StepPerTick = .05
KConstant = .002

class Metronome:
    def __init__(self, offset):
        self.time = 0
        self.links = []
        self.syncValue = offset
        self.output = math.sin(offset)
        self.history = []
    def update(self):
        newSync = 0
        syncOffset = 0
        for i in self.links:
            #Minimizes phase differance
            syncOffset += math.sin(i.syncValue-self.syncValue)
            #Maximizes phase differance            
            #syncOffset += math.sin(self.syncValue-i.syncValue)

        newSync += KConstant*syncOffset
        self.syncValue += newSync
        self.time+=1
        self.output = math.sin(self.time*StepPerTick+self.syncValue)
        self.history+=[self.output]
    def addLink(self, metronome):
        if metronome not in self.links and metronome != self:
            self.links+=[metronome]
            metronome.addLink(self)

metronomes = []
metronomes+=[Metronome(0), Metronome(2), Metronome(6)]
metronomes[0].addLink(metronomes[1])
metronomes[0].addLink(metronomes[2])
metronomes[1].addLink(metronomes[2])

#for i in range(1500):
for i in range(1500):
    for j in metronomes:
        j.update()

for i in metronomes:
    plt.plot(i.history)
plt.show()
