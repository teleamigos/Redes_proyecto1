#import numpy as np
# =============================================================================
# funcion to_bytes : El valor binario lo asigna a un arreglo de un byte
# =============================================================================
def to_bytes(n):
    Arraybyte=[0,0,0,0,0,0,0,0]#Generamos un vector de 8 bits
    numero=int(n)
    i=0
    while(i!=8):
        Arraybyte[7-i]=int(numero%10)
        numero=numero/10
        i=i+1
    return Arraybyte
# =============================================================================
# to_decimal : Pasamos de un arreglo de un byte a un valor decimal
# =============================================================================
def to_decimal(Byte):
    decimal=0
    for i in range(0,7):
        decimal=Byte[i]*(2**(7-i))+decimal
    return decimal
# =============================================================================
# Principal
# =============================================================================
##Apertura y lectura de la imagen en formato .txt
archivo=open("/home/georky/Escritorio/proyectoredes_2-master/imagen.txt","rb")
BytesFrame=0
buffer=archivo.read(1)#Lee el primer byte
while(buffer):
    n=int.from_bytes(buffer,'big')#Convierte a tipo entero
    print (n)
    n=format(n,'b')
    BytesFrame=to_bytes(n)
#    print(buffer)
#    print(n)
#    print(BytesFrame)
    buffer=archivo.read(1)# Aumenta el buffer al siguiente byte.
print("final byte")
arregloprueba=[1,1,1,1,1,1,1,1]
decimal=to_decimal(arregloprueba)+1
print(decimal)
a=decimal.to_bytes(1,byteorder='little')
print(a)



