#include <Wire.h>//Capa MAC usa protocolo I2C manda paquetes de 8 bits-
#include<stdio.h>

struct Frame {
  int blinks;
  int data;
}frame;

struct Frame *back;

uint8_t *p=(uint8_t *)&frame;

int i=0;

void setup(){

  Wire.begin(8);//nombre
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  Wire.onReceive(receiveEvent);

}

void receiveEvent(int){//Espera evento
  if (Wire.available()){//Si hay algo disponible en el buffer.
    p[i]=Wire.read();
    delay(100);
    i++;
  }
}

void loop(){
    back=(struct Frame*)p;
    if(back->data==5){
      Serial.println("########################");
      for(int i=0;i<sizeof(struct Frame);i++){
      Serial.println(p[i]);
    }

    Serial.println("$$$$$$$$$$$$");
    Serial.println(back->data);
    Serial.println(back->blinks);
    back->data=0;
    delay(100);
  }
}
