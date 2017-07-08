int a = 0;
int incomingByte = 0;   // for incoming serial data


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);           // set up Serial library at 9600 bps

}

void loop() {
  // put your main code here, to run repeatedly:


  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

     // say what you got:
     Serial.print("I received: ");
     Serial.println(incomingByte, DEC);
   }
  
  a = a + 10;
  Serial.println(a);
  delay(1000); 
}
