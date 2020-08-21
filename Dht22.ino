#include <dht.h>
#define DHT_PIN 4 //Pin de lectura 4
dht DHT; // Objeto del sensor

void setup(){
  Serial.begin(9600); 
}
void loop(){
  int dato= DHT.read22(DHT_PIN);

  Serial.print("{\"temperature\":");
  Serial.print(DHT.temperature);
  Serial.print(",");
  Serial.print("\"humidity\":");
  Serial.print(DHT.humidity);
  Serial.print("}\n");

  delay(30000);
}
