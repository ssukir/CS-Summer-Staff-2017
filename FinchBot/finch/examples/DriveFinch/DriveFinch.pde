/** 
//
//  The purpose of this program is to demonstrate some of the basic
//  ways to use the Finch and how to interface it with the Processing
//  language. This program reads accelerometer data from the Finch
//  and uses the data to control a circle that draws on the screen. It also
//  uses the mouse position to drive the Finch around.
*/

 /* Imports the Finch library. Ensure that you have installed the Finch library package 
as per the directions at: http://wiki.processing.org/w/How_to_Install_a_Contributed_Library */
import edu.cmu.ri.createlab.terk.robot.finch.*;

//Start by creating some variables, including a new finch
Finch myFinch = new Finch();

//These store the x and y position of the circle we're going to draw
float turtleX = 320;
float turtleY = 640;

//This is the font we'll use to put text on the screen
PFont font;

//Typical Processing programs start with a setup function
//This initializes everything you're only going to set once
void setup() {
  //First we choose how big our window is going to be
  //This is in pixels
  size(640,640);
  //This sets the background to a medium gray
  color(128);
  //This is to make the code more readable
  int half = 640/2;

  //The next thing we draw will be filled in with red
  fill(255,0,0,255);
  //Draw a rectangle with upper-left corner at 0,0 with a length
  //of half the window size
  rect(0, 0, half, half);

  //Next color is yellow
  fill(255,255,0,255);
  //Put this one at the top right
  rect(half, 0, half, half);

  //Now purple
  fill(255,0,255,255);
  //in the bottom left
  rect(0, half, half, half);

  //And turquoise
  fill(0,255,255,255);
  //in the bottom right
  rect(half, half, half, half);

  //Set up a font
  font = loadFont("ComicSansMS-Bold-60.vlw");
  textFont(font);
  fill(0,0,0,255);
  //Write the direction each area of the screen will make the finch
  //drive
  text("Forward",half*3/2.5,half*3/2);
  text("Backward",half/8,half/2);
  text("Right",half*3/2.5,half/2);
  text("Left",half/3,half*3/2);
}

//The draw function loops infinitely until the main window is closed
void draw()
{
  //First, get the accelerometer data from the finch
  //We are only looking at the X and Y accelerations, but we could
  //also look at the Z acceleration.
  double myY = (myFinch.getXAcceleration());
  double myX = (myFinch.getYAcceleration());
  
  //The accelerations are in the range -1.5 to 1.5 g (1g is
  //standard gravity). We want to move a circle around a little
  //faster than that, so we multiply it by 6. Also, X acceleration
  //is positive when the finch is tilted left, but x coordinates on
  //the screen increase to the right, so use -6 for myX.
  turtleX += -6*myX;
  turtleY += 6*myY;
  
  //Make sure we don't try to draw the circle off the screen
  if(turtleX < 0) turtleX = 0;
  if(turtleY < 0) turtleY = 0;
  if(turtleX > 640) turtleX = 640;
  if(turtleY > 640) turtleY = 640;

  //Set the speed of the finch based off where the mouse is
  //The velocity for each wheel can be set between -255 and 255
  int leftSpeed = (int)(2*255.0/640.0*mouseX)-255;
  int rightSpeed = (int)(2*255.0/640.0*mouseY)-255;

  //Set the wheel velocities on the Finch
  myFinch.setWheelVelocities(leftSpeed,rightSpeed);

  //Set the LED color of the finch based on the location of the mouse
  //to match the color of the background.
  if(mouseX > 320 && mouseY > 320) {
   myFinch.setLED(0,255,255);
  }
  else if(mouseX <= 320 && mouseY > 320) {
   myFinch.setLED(255,0,255);
  }
  else if(mouseX > 320 && mouseY <= 320) {
   myFinch.setLED(255,255,0);
  }
  else {
   myFinch.setLED(255, 0, 0);
  }
  // draw the circle representing accelerometer position
  ellipse(turtleX,turtleY, 10,10);
}

// Close down communication with Finch so it doesn't go driving off a table
void stop() {
  myFinch.quit();
}
