#include <Wire.h>//Capa MAC usa protocolo I2C manda paquetes de 8 bits-
#include<stdio.h>

struct Frame {
  int blinks;
  int data;
};

struct Frame frame;

uint8_t *p;

void setup () {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  Wire.begin();//Habilita la capa MAC es el transmisor maestro.
}

void loop (){
  char rx_byte[]="Israel no es un estado legitimo";
  ParteMensaje(rx_byte);

  /*if (Serial.available()>0){//Que exista un buffer
    rx_byte = Serial.parseInt();
  }
  if (rx_byte==5){
    digitalWrite(13,HIGH);
    delay(100);
    digitalWrite(13,LOW);
    delay(100);
    frame.blinks=549;
    frame.data=rx_byte;

    p=(uint8_t *)&frame;

    for (int i=0; i<sizeof(frame);i++)
    {
      Wire.beginTransmission(8);
      Serial.println(p[i]);
      Wire.write(p[i]);
      Wire.endTransmission();

    }
  }*/
}

void ParteMensaje(char msg)
{
  int tam=0;
  tam=sizeof(msg);
  
}
