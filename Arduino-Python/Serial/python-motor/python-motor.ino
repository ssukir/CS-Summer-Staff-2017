#include <Servo.h>

Servo myservo;

int pos = 0;

void setup() {
  Serial.begin(115200); // use the same baud-rate as the python side
  myservo.attach(9);
}

void loop() {
  if(Serial.available() > 1){
    for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
      if(Serial.read() == 49){ 
        myservo.write(pos);              // tell servo to go to position in variable 'pos'
        delay(1000);                       // waits 1s for the servo to reach the position
      }
    }
    for (pos = 180; pos >= 180; pos -= 1) { // goes from 0 degrees to 180 degrees
      if(Serial.read() == 49){ 
        myservo.write(pos);              // tell servo to go to position in variable 'pos'
        delay(1000);                       // waits 1s for the servo to reach the position
      }
    }
  }
}
