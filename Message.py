"""-----------------------------------------------------------------------------
----------------------------------class Message---------------------------------
--------------------------------------------------------------------------------
1.- Init function.
-----------------------------------------------------------------------------"""
from struct import*
import binascii
class Message:
    def __init__(self,ID):
        self.MyID=ID
        self.Type='2'
        self.IDdst=''
        self.Temperature=0
        self.steps=0
        self.crc=0
        self.msj_coded=''
        self.msj_out=b''

    def Message_pack(self,IDdst,T):
        self.IDdst=IDdst
        self.Temperature=T
        self.C_WEP()
        self.msj_out=self.Type.encode('utf-8')+self.MyID.encode('utf-8')
        self.msj_out+=self.IDdst.encode('utf-8')+pack('!B',self.steps)
        self.msj_out+=self.msj_coded.encode('utf-8')
        self.crc=binascii.crc32(self.msj_out)
        self.msj_out+=pack('!I',self.crc)
        return self.msj_out

    def Message_unpack(self,msj,Tp):
        pass

    def C_WEP(self):
        pass

    def D_WEP(self,code):
        pass
