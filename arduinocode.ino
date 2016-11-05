#include <SoftwareSerial.h>  
#include <LiquidCrystal.h>
// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(1, 0, 13, 12, 11, 10);

int bluetoothTx = 2;  // TX-O pin of bluetooth mate, Arduino D2
int bluetoothRx = 3;  // RX-I pin of bluetooth mate, Arduino D3
#define EN  4
#define MS1 5
#define MS2 6
#define MS3 7
#define stp 8
#define dir 9



SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);
void setup()
{
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.setCursor(0,0);
  lcd.print("Initializing...");

  
  pinMode(13, OUTPUT);
  pinMode(stp, OUTPUT);
  pinMode(dir, OUTPUT);
  pinMode(MS1, OUTPUT);
  pinMode(MS2, OUTPUT);
  pinMode(MS3, OUTPUT);
  pinMode(EN, OUTPUT);
  resetBEDPins(); //Set step, direction, microstep and enable pins to default states
  
  Serial.begin(9600);  // Begin the serial monitor at 9600bps

  bluetooth.begin(115200);  // The Bluetooth Mate defaults to 115200bps
  bluetooth.print("$");  // Print three times individually
  bluetooth.print("$");
  bluetooth.print("$");  // Enter command mode
  delay(100);  // Short delay, wait for the Mate to send back CMD
  bluetooth.println("U,9600,N");  // Temporarily Change the baudrate to 9600, no parity
  // 115200 can be too fast at times for NewSoftSerial to relay the data reliably
  bluetooth.begin(9600);  // Start bluetooth serial at 9600
}

void loop()
{
  if(bluetooth.available())  // If the bluetooth sent any characters
  {
    lcd.setCursor(0,0);
    lcd.print("Idle...");
    // Send any characters the bluetooth prints to the serial monitor
    char character = (char)bluetooth.read();
    Serial.print(character);
    if (character == 'G') {
      lcd.setCursor(0, 0);
      lcd.print("Running...");
      digitalWrite(EN, LOW);
      SmallStepMode();
      digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(500);              // wait for a half second
      digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
      resetBEDPins();
    }    
  }
  if(Serial.available())  // If stuff was typed in the serial monitor
  {
    // Send any characters the Serial monitor prints to the bluetooth
    char character = (char)Serial.read();
    bluetooth.print(character);
  }
  // and loop forever and ever!
}

void resetBEDPins()
{
  digitalWrite(stp, LOW);
  digitalWrite(dir, LOW);
  digitalWrite(MS1, LOW);
  digitalWrite(MS2, LOW);
  digitalWrite(MS3, LOW);
  digitalWrite(EN, HIGH);
}

// 1/16th microstep foward mode function
void SmallStepMode()
{
  digitalWrite(dir, LOW); //Pull direction pin low to move "forward"
  digitalWrite(MS1, HIGH); //Pull MS1,MS2, and MS3 high to set logic to 1/16th microstep resolution
  digitalWrite(MS2, HIGH);
  digitalWrite(MS3, HIGH);
  int x;
  for(x=0; x<3200; x++)  //Loop the forward stepping enough times for motion to be visible
  {
    digitalWrite(stp,HIGH); //Trigger one step forward
    delay(1);
    digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
    lcd.setCursor(0, 1);
    lcd.print("Msteps");
    delay(1);
  }
}

