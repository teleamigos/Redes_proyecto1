"""-----------------------------------------------------------------------------
----------------------------------class packed----------------------------------
--------------------------------------------------------------------------------
1.- Init function
2.- Pack :
    * MAC address destination : 6 bytes
    * MAC address source : 6 bytes
    * Payload : It depends on the message type, either Hello (0), MPR (1) or
                Temperature (2).
3.- Unpack :
    * This function unpack the message received depending its type.
-----------------------------------------------------------------------------"""
from struct import*
from Hello import*
from MPRmsj import*
from Message import*
from Topology import*

class Packed(Hello,MPRmsj,Message,Topology):
    def __init__(self,MyMacAdd,ID):
        self.myMACadd=MyMacAdd
        self.broadcast=b'\xff\xff\xff\xff\xff\xff'
        self.protocol=b'\x08\x01'
        self.payload=''
        self.Type_message={
        'Hello':'0',
        'MPR_message':'1',
        'Message':'2'
        }
        self.tp=Topology(ID)
        self.msj_out=''
        self.message_Hello=Hello(ID)
        self.message_MPR=MPRmsj(ID)
        self.message=Message(ID)
        self.temperature=0

    def Pack(self,type,IDdst,**temp):
        self.msj_out=self.broadcast+self.myMACadd+self.protocol
        self.temperature=temp
        if type==self.Type_message['Hello']:
            self.payload=self.message_Hello.Hello_pack(self.tp)
        elif type==self.Type_message['MPR_message']:
            self.payload=self.message_MPR.MPRmsj_pack(self.tp)
        elif type==Type_message['Message']:
            self.payload=self.message.Message_pack(IDdst,self.temperature)
        else:
            print('Error, invalid type of message...')
        self.msj_out+=self.payload
        return self.msj_out

    def Unpack(self,msj):
        payload=msj[14:]
        type=payload[0:1].decode('utf-8')
        if type==self.Type_message['Hello']:
            self.message_Hello.Hello_unpack(payload,self.tp)
        elif type==self.Type_message['MPR_message']:
            self.message_MPR.MPRmsj_unpack(payload,self.tp)
        elif type==self.Type_message['Message']:
            self.message.Message_unpack(payload,self.tp)
        else:
            print('Error, message type incorrect...')
