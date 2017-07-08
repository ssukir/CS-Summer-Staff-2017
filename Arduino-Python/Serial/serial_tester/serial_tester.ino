void setup() {
  Serial.begin(115200); // use the same baud-rate as the python side
  pinMode(LED_BUILTIN, OUTPUT); // initialize digital pin LED_BUILTIN as an output.
  digitalWrite(LED_BUILTIN, LOW); 
}

void loop() {
    Serial.println("Hello world from Arduino!"); // write a string
    delay(500);                         // wait for half a second
  if(Serial.available() > 1){
    if(Serial.read() == 49){           // if recieves 1
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    }
    else if(Serial.read() == 48){       // if recieves 0
      digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    }
  }
}
