"""-----------------------------------------------------------------------------
----------------------------------Class Topology--------------------------------
--------------------------------------------------------------------------------
1.- Init:
    * Define class variables as MyId, Topology, MyMPR, etc...
2.- MPR :
    * Compute a list of MPRs from a Topology given.
-----------------------------------------------------------------------------"""
import time
class Topology:
    def __init__(self,ID):
        self.MyID=ID
        self.Neighbors=[]
        self.Topology={}
        self.MyMPR=[]
        self.SOYMPR=0
        self.around=[]

    def MPR(self):
        nei=[]
        for i in self.Topology:
            nei.append(i)
            for j in self.Topology[i]:
                try:
                    self.around.index(j)
                except:
                    self.around.append(j)
        self.around.sort()
        if self.MyID in self.around:
            self.around.remove(self.MyID)
        for i in nei:
            try:
                self.around.remove(i)
            except:
                time.sleep(0.05)
        aux=0
        for k in self.around:
            for i in self.Topology:
                for j in self.Topology[i]:
                    if k == j and aux == 0:
                        try:
                            self.MyMPR.index(i)
                        except:
                            self.MyMPR.append(i)
                            aux = 1
        aux = 0
