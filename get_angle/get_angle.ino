#include "Wire.h"
#include <MPU6050_light.h>

MPU6050 mpu(Wire);
unsigned long timer = 0;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu.begin();
//  Serial.println(F("Calculating gyro offset, do not move MPU6050"));x
  delay(1000);
  mpu.calcGyroOffsets();
  pinMode(8,OUTPUT);
//  Serial.println("Done!\n");
}

void loop() {
  mpu.update();
  int x,y,z;
  
  if ((millis() - timer) > 10) { // print data every 10ms
    Serial.print("X:");
    Serial.print(mpu.getAngleX());
//    Serial.write(x);
    Serial.print(",Y:");
    Serial.print(mpu.getAngleY());
    Serial.print(",Z:");
    Serial.println(mpu.getAngleZ());
    if(mpu.getAngleX()>50){
      digitalWrite(8,HIGH);
      }
     else{
      digitalWrite(8,LOW);
      }
    timer = millis(); 
     
//    delay(1000);
  }
}
