
/**
 * Finch RGB Cube.
 * 
 * This Finch example is based heavily on the classic RGB cube Processing example.
 * The example uses most of the RGB cube code, but replaces the mouse input to rotate
 * the cube with a filtered version of the Finch's Accelerometer. It also changes the
 * color of the Finch's beak in rough correlation with the color of the visible cube face.
 */

/* Imports the Finch library. Ensure that you have installed the Finch library package 
as per the directions at: http://wiki.processing.org/w/How_to_Install_a_Contributed_Library */
import edu.cmu.ri.createlab.terk.robot.finch.*;

// Creates a new instantiation of the Finch object called "tweety" 
Finch tweety = new Finch();


float xmag, ymag = 0;
float newXmag, newYmag = 0; 

// Holds a filter version of the X and Y accelerometer values
float xAccel, yAccel = 0; 

// Holds scaled versions of xAccel and yAccel
float xScale, yScale = 0;

// Used to store the 0-255 values of the red, green, and blue color intensities for the Finch's beak.
int redLED, greenLED, blueLED = 0;
 
void setup() 
{ 
  size(640, 360, P3D); 
  noStroke(); 
  colorMode(RGB, 1); 
  // Gratuitous test of the Finch's text to speech (ensure computer speakers are on)
  tweety.saySomething("Hello!");
} 
 
void draw() 
{ 
  background(0.5);
  
  pushMatrix(); 
 
  translate(width/2, height/2, -30); 
  
  // reads in the x and y accelerometer values. Note that we run these through a filter that is 10% new value and 90% old value
  // this is done to reduce apparent noise (without the filter, the cube looks kind of jittery).
  xAccel = 0.1*(float)tweety.getXAcceleration()+0.9*xAccel;
  yAccel = 0.1*(float)tweety.getYAcceleration()+0.9*yAccel;
  
  // Scale these filtered values to the width and height of the window
  xScale = xAccel*height/2;
  yScale = yAccel*width/2;
  
  // RGB Cube used MouseX and MouseY in place of yScale and xScale
  // The rest of the code to popMatrix is identical  
  newXmag = yScale/float(width) * TWO_PI;
  newYmag = xScale/float(height) * TWO_PI;
  
  float diff = xmag-newXmag;
  if (abs(diff) >  0.01) { xmag -= diff/4.0; }
  
  diff = ymag-newYmag;
  if (abs(diff) >  0.01) { ymag -= diff/4.0; }
  
  rotateX(-ymag); 
  rotateY(-xmag); 
  
  scale(90);
  beginShape(QUADS);

  fill(0, 1, 1); vertex(-1,  1,  1);
  fill(1, 1, 1); vertex( 1,  1,  1);
  fill(1, 0, 1); vertex( 1, -1,  1);
  fill(0, 0, 1); vertex(-1, -1,  1);

  fill(1, 1, 1); vertex( 1,  1,  1);
  fill(1, 1, 0); vertex( 1,  1, -1);
  fill(1, 0, 0); vertex( 1, -1, -1);
  fill(1, 0, 1); vertex( 1, -1,  1);

  fill(1, 1, 0); vertex( 1,  1, -1);
  fill(0, 1, 0); vertex(-1,  1, -1);
  fill(0, 0, 0); vertex(-1, -1, -1);
  fill(1, 0, 0); vertex( 1, -1, -1);

  fill(0, 1, 0); vertex(-1,  1, -1);
  fill(0, 1, 1); vertex(-1,  1,  1);
  fill(0, 0, 1); vertex(-1, -1,  1);
  fill(0, 0, 0); vertex(-1, -1, -1);

  fill(0, 1, 0); vertex(-1,  1, -1);
  fill(1, 1, 0); vertex( 1,  1, -1);
  fill(1, 1, 1); vertex( 1,  1,  1);
  fill(0, 1, 1); vertex(-1,  1,  1);

  fill(0, 0, 0); vertex(-1, -1, -1);
  fill(1, 0, 0); vertex( 1, -1, -1);
  fill(1, 0, 1); vertex( 1, -1,  1);
  fill(0, 0, 1); vertex(-1, -1,  1);

  endShape();
  
  popMatrix(); 
  
/* Use the x accelerometer reading to set the RGB LED based roughly on the visible face
   We leave setting the y accelerometer reading to LED color as an exercise for the reader. */
   
   
  // If the x acceleration is greater than 0, the beak is pointing upward 
  if(xAccel > 0)
  {
    // If it's more than a half, turn off blue
    // Make it so green increases as the beak goes higher
    if(xAccel > 0.5) 
    {
      redLED = (int)((1-xAccel)*510);
      greenLED = (int)((xAccel-0.5)*510);
      blueLED = 0;
    }
    // Blue should decrease and red should increase
    // as the beak goes higher.
    else
    {
      redLED = (int)(xAccel * 510);
      greenLED = 0;
      blueLED = (int)((0.5-xAccel)*510);
    }
  }
  // This are different as we point the beak further down
  // Here the colors go from blue->green->red
  else
  {
    // Red increases as the beak points further down
    if(xAccel < -0.5) 
    {
      greenLED = (int)((1+xAccel)*510);
      redLED = (int)((-xAccel-0.5)*510);
      blueLED = 0;
    }
    // Green increases until 0.5, blue decreases
    else
    {
      greenLED = (int)(-xAccel * 510);
      redLED = 0;
      blueLED = (int)((xAccel+0.5)*510);
    }
  }
  
  // The following code just keeps the values in line with what's expected
  // Though we don't expect more than 1 gees from any accelerometer, it is
  // possible due to sudden movements or noise.
  if(redLED < 0)
    redLED = 0;
  if(blueLED < 0)
    blueLED = 0;
  if(greenLED < 0)
    greenLED = 0;
    
  if(redLED > 255)
    redLED = 255;
  if(blueLED > 255)
    blueLED = 255;
  if(greenLED > 255)
    greenLED = 255;
  // Set the LED to the RGB color we determined
  tweety.setLED(redLED, greenLED, blueLED);

}

// Close down communication with Finch so it doesn't go driving off a table
void stop() {
  tweety.quit();
}
