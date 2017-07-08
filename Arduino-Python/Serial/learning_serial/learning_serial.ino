/*
 * Hello World!
 *
 * This is the Hello World! for Arduino. 
 * It shows how to send data to the computer
 */

int a = 0;

void setup()                    // run once, when the sketch starts
{
  Serial.begin(9600);           // set up Serial library at 9600 bps
  // Serial.println("Hello world!");  // prints hello with ending line break 
}

void loop()                       // run over and over again
{
  // Serial.println("Hello world!");  // prints hello with ending line break
  a = a + 10;
  Serial.println(a);
  delay(1000); 
}
