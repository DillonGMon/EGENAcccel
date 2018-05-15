#include <Wire.h>
#include <Adafruit_MMA8451.h>
#include <Adafruit_Sensor.h>

Adafruit_MMA8451 mma = Adafruit_MMA8451(); //setting up the accelerometer

void setup(void) {
  Serial.begin(9600); //begins a serial connection to talk to the other software
  if (! mma.begin()) {
    Serial.println("Couldnt start");
    while (1);
  }
  Serial.println("MMA8451 found!");
  
  mma.setRange(MMA8451_RANGE_2_G);
  
  Serial.print("Range = "); Serial.print(2 << mma.getRange());  
  Serial.println("G");
  
}

void loop() {
  
  mma.read();
  Serial.print("X: "); Serial.println(mma.x); //sends the facing/rotational data to the serial port with an identifier for which piece, like x axis
  Serial.print("Y: "); Serial.println(mma.y); 
  Serial.print("Z: "); Serial.println(mma.z); 
  


  sensors_event_t event; 
  mma.getEvent(&event);

  Serial.print("S: "); Serial.println(event.acceleration.x); //send the acceleration data for each axis to the serial port
  Serial.print("D: "); Serial.println(event.acceleration.y);
  Serial.print("F: "); Serial.println(event.acceleration.z);
  
  
  /* Get the orientation of the sensor */
  uint8_t o = mma.getOrientation(); //built in orientation function to more clearly visualize which way the accel is facing
  
  switch (o) {
    case MMA8451_PL_PUF: 
      Serial.println("Portrait Up Front");
      break;
    case MMA8451_PL_PUB: 
      Serial.println("Portrait Up Back");
      break;    
    case MMA8451_PL_PDF: 
      Serial.println("Portrait Down Front");
      break;
    case MMA8451_PL_PDB: 
      Serial.println("Portrait Down Back");
      break;
    case MMA8451_PL_LRF: 
      Serial.println("Landscape Right Front");
      break;
    case MMA8451_PL_LRB: 
      Serial.println("Landscape Right Back");
      break;
    case MMA8451_PL_LLF: 
      Serial.println("Landscape Left Front");
      break;
    case MMA8451_PL_LLB: 
      Serial.println("Landscape Left Back");
      break;
    }
  Serial.println();
  delay(1000);
  
}
