/**
 * Sensor Visualizer
 *
 * This program visualizes the Finch's obstacle, light, temperature, and accelerometer sensors
 * It uses three cubes which rotate based on the accelerometers, a circle that grows lighter
 * for each of the light sensors, a circle that changes color with temperature, and two 
 * objects to represent the state of the obstacle sensors.
 */
 
 /* Imports the Finch library. Ensure that you have installed the Finch library package 
as per the directions at: http://wiki.processing.org/w/How_to_Install_a_Contributed_Library */
import edu.cmu.ri.createlab.terk.robot.finch.*;

// Creates a new instantiation of the Finch object called "visualize" 
Finch visualize = new Finch();

int leftLight;
int rightLight;
double temperature;

int rColor, gColor, bColor;

float xAccel, yAccel, zAccel;

void setup() 
{ 
  size(640, 360, P3D); 
  noStroke(); 

  // Gratuitous test of the Finch's text to speech (ensure computer speakers are on)
  visualize.saySomething("Welcome to the visualizer!");
} 

void draw() 
{ 
  background(0);

 // Store current coordinates for use with 3D objects
  pushMatrix();

  // Visualize the left and right light sensors as circles that 
  // become whiter with more light
  
  // Read in the sensor values from the Finch
  leftLight = visualize.getLeftLightSensor();
  rightLight = visualize.getRightLightSensor();

  // Set up two circles
  fill(leftLight,leftLight,leftLight);
  ellipse(220, 80, 90, 90);
  fill(rightLight,rightLight,rightLight);
  ellipse(420, 80, 90, 90);
  
  // Visualize the left and right obstacle sensors
  // Circles that are green with no obstacle, red with an obstacle
  if(visualize.isObstacleLeftSide())
    fill(255,0,0);
  else
    fill(0,255,0);
  ellipse(106, 80, 60, 60);
  
  if(visualize.isObstacleRightSide())
    fill(255,0,0);
  else
    fill(0,255,0);
  ellipse(534, 80, 60, 60); 

  // Visualize temperature as a circle
  // Green = 22 C, red = 30, blue is 14
  // Colors should fade smoothly between these vals
  temperature = visualize.getTemperature();
  
  // If less than 22, fade from green to blue
  if(temperature < 22.0) 
  {
    bColor = (int)((22-temperature)*32);
    gColor = (int)((temperature-14)*32);
    rColor = 0;
  }
  else
  {
    bColor = 0;
    gColor = (int)((30-temperature)*32);
    rColor = (int)(temperature-22)*32;   
  }
  // Keep values within a 0-255 range
  if(bColor < 0)
    bColor = 0;
  if(bColor > 255)
    bColor = 255;
  if(gColor < 0)
    gColor = 0;
  if(gColor > 255)
    gColor = 255;
  if(rColor < 0)
    rColor = 0;
  if(rColor > 255)
    rColor = 255;
  
  fill(rColor, gColor, bColor);
  ellipse(319, 80, 60, 60);
  // For good measure, set the Finch's beak to represent temperature
  visualize.setLED(rColor, gColor, bColor);
  
  /* Create three cubes that rotate based on the Finch's X, Y, and Z accelerometers.
   * For fun, the cubes also change color with orientation. */
  translate(106, 220, 0);
  // Read in accelerometry and use a filter to make the data less noisy
  xAccel = 0.1*(float)visualize.getXAcceleration()*PI + 0.9*xAccel;
  rColor = 128 - (int)(xAccel*90);
  gColor = 0;
  bColor = 128 + (int)(xAccel*90);
  fill(rColor, gColor, bColor);
  rotateX(xAccel);
  box(80);

  popMatrix();
  pushMatrix();
  translate(319, 220, 0);
  yAccel = 0.1*(float)visualize.getYAcceleration()*PI + 0.9*yAccel;
  rColor = 128 - (int)(yAccel*90);
  bColor = 0;
  gColor = 128 + (int)(yAccel*90);
  fill(rColor, gColor, bColor);
  rotateZ(yAccel);
  box(80);
  
  popMatrix();
  translate(534, 220, 0);
  zAccel = 0.1*(float)visualize.getZAcceleration()*PI + 0.9*zAccel;
  rColor = 0;
  gColor = 128 - (int)(zAccel*90);
  bColor = 128 + (int)(zAccel*90);
  fill(rColor, gColor, bColor);
  rotateY(zAccel);
  box(80);
 
}

// Close down communication with Finch
void stop() {
  visualize.quit();
}

