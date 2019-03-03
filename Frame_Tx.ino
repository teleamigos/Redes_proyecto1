#include <Wire.h>//Capa MAC usa protocolo I2C manda paquetes de 8 bits-
#include<stdio.h>

/*
   creamos una estructura Frame, que contendrà la informaciòn del mensaje
   dividido, de modo que cada Frame serà contenedor de un solo caracter
   del mensaje. Tambien portarà un indice que sirve como etiqueta para
   que el receptor pueda ordenar. Y la direccion de memoria de un head y
   tail para saber el inicio y fin de la fila dinamica. La direcion del
   siguiente nodo es next
*/
struct Frame {
  struct Dato *dato;
  struct  Frame *next;
};

/*
   La estructura Dato es el contenido de cada Frame, de modo que contenga
   la informacion del mensaje y el indice
*/
struct Dato {
  char mensaje;
  int blinks;
  int index;

};

/*
   El arregloFrame es una estructura que cocntiene estructuras tipo
   Frame, compuesta de un head y tail. Podemos obtener la cantidad
   de estructuras a partir de tam
*/
struct ArregloFrame {
  struct Frame *head;
  struct Frame *tail;
  int tam;

};

typedef struct ArregloFrame queu;

void Init(queu *serie) {
  serie->head = NULL;
  serie->tail = NULL;
  serie->tam = 0;
}

int insertar(queu *serie, Frame  *actual, Dato *dato) {
  Frame *nuevo_frame;

  if ((nuevo_frame = (Frame*)malloc(sizeof(Frame))) == NULL) {
    return -1;
  }
  if ((nuevo_frame->dato = (Dato*)malloc(sizeof(Dato))) == NULL) {
    return -1;
  }
  //strcpy (nuevo_frame->dato,dato);
  nuevo_frame->dato->mensaje = dato->mensaje;
  nuevo_frame->dato->blinks = dato->blinks;
  nuevo_frame->dato->index = dato->index;
  ///////////////////////////////////////
  if (actual == NULL)
  {
    if (serie->tam == 0) // Si está vaciío llena el primer espacio
    {
      serie->tail = nuevo_frame;
      nuevo_frame->next = serie->head;
      serie->head = nuevo_frame;
      return 0;
    }
  }
  else {
    if (actual->next == NULL)
    {
      serie->tail = nuevo_frame;

    }
    nuevo_frame->next = actual->next;
    actual->next = nuevo_frame;
  }
  serie->tam++;
  return 0;
}

boolean isItVoid(queu *contenedor) {
  if (contenedor->head == NULL) {
    return true;
  } else {
    return false;
  }
}

void enviar(queu *contenedor) {
  struct Frame *temporal;
  uint8_t *p;
  int i = 0;
  temporal = contenedor->head;
  while (temporal->next == NULL) {
    if (isItVoid(contenedor) == false) {
      //Envia mensaje
      digitalWrite(13, HIGH);
      delay(100);
      digitalWrite(13, LOW);
      delay(100);
      p = (uint8_t *)&temporal;
      temporal = temporal->next;

      for (int i = 0; i < sizeof(temporal); i++)
      {
        Wire.beginTransmission(8);
        Serial.println(p[i]);
        Wire.write(p[i]);
        Wire.endTransmission();
      }
    }
    else {
      //Manda error
    }
  }
}

//uint8_t *p;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  Wire.begin();
}

void loop() {
  queu contenedor;
  struct Frame temporal;
  // put your main code here, to run repeatedly:
  String mensaje;
  //char mensaje[] = "Israel no es un estado";
  struct Dato msn;
  int i = 0;
  int a;
  if (Serial.available()>=0)
    {
    mensaje=Serial.read();
    }

  Init(&contenedor);
  for (i = 0; i < sizeof(mensaje); i++) {
    msn.mensaje = mensaje[i];
    msn.blinks = 549;
    msn.index = i + 1;
    a = insertar(&contenedor, &temporal, &msn);
    //Serial.println(a);
  }
  muestra(&contenedor);
  //Serial.print(contenedor.tam);
  enviar(&contenedor);
}



void muestra(queu *serie) {
  struct Frame *actual;
  int i;
  actual = serie -> head;
  for (i=0; i < serie->tam; ++i) {
    Serial.print(actual->dato->mensaje);
    actual = actual -> next;
  }
}
