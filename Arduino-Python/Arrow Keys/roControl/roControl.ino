
#include <ArduinoRobot.h> // include the robot library
#include <Wire.h>

void setup() {
  Robot.begin();
  Robot.beginTFT();
  Robot.beginSD();
  Serial.begin(115200);

  Robot.displayLogos();

  Robot.clearScreen();

}

void loop() {
  if(Serial.available() > 1){
    if(Serial.read() == 48){           // if recieves 0
      Robot.motorsWrite(255, 255);   // move forward
    }
    else if(Serial.read() == 49){       // if recieves 1
      Robot.motorsWrite(-255, -255);   // move backward
    }
     else if(Serial.read() == 50){       // if recieves 2
      Robot.motorsWrite(-255, 255);    // turn left
    }
     else if(Serial.read() == 51){       // if recieves 3
      Robot.motorsWrite(255, -255);    // turn right
    }
  }
}
