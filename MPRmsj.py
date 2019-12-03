"""-----------------------------------------------------------------------------
----------------------------------class MPRmsj----------------------------------
--------------------------------------------------------------------------------
1.- Init function.
2.- MPRmsj_pack :
    * Type message : 1 byte
    * ID source : 1 byte
    * Lenght of the MPRs list : 2 bytes
    * List of MPRs : varible size
    * CRC : 4 bytes
3.- MPRmsj_unpack :
    * If my node is in the list of MPR, My node will be recognised as MPR.
-----------------------------------------------------------------------------"""
from struct import*
import binascii
#import zlib

class MPRmsj:
    def __init__(self,ID):
        self.MyID=ID
        self.Type='1'
        self.MyMPR=[]
        self.crc=0
        self.msj_out=b''

    def MPRmsj_pack(self,tp):
        self.MyMPR=tp.MyMPR
        self.msj_out=self.Type.encode('utf-8')
        self.msj_out+=self.MyID.encode('utf-8')
        l=len(self.MyMPR)
        self.msj_out+=pack('!H',l)
        for n in self.MyMPR:
            self.msj_out+=n.encode('utf-8')
        #self.crc=zlib.crc32(self.msj_out)
        self.crc=binascii.crc32(self.msj_out)
        self.msj_out+=pack('!I',self.crc)
        return self.msj_out

    def MPRmsj_unpack(self,msj_MPR,Tp):
        lista=[]
        num_MPR=unpack('!H',msj_MPR[2:4])[0]
        MPRs=msj_MPR[4:4+num_MPR]
        print(MPRs)
        for i in range(0,num_MPR):
            m=MPRs[i:i+1]
            m=m.decode('utf-8')
            lista.append(m)
        print(lista)
        if Tp.MyID in lista:
            Tp.SOYMPR=1
