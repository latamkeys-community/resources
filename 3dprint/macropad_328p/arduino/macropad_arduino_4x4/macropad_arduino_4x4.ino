#include <Keypad.h>

const byte ROWS = 4; //three rows
const byte COLS = 4; //three columns
//define the cymbols on the buttons of the keypads
//Your Keypad distribution
const char hexaKeys[ROWS][COLS] = {
  {'1', '2', '3', '4'},
  {'5', '6', '7', '8'},
  {'9', '10', '11', '12'},
  {'13', '14', '15', '16'}
 };

//Digital pins for Rows and Cols
byte rowPins[ROWS] = {9, 8, 7, 6};//connect to the row pinouts of the keypad
byte colPins[COLS] = {5, 4, 3, 2};//connect to the column pinouts of the keypad

//Creates keypad object
Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);

void setup() {
  Serial.begin(9600);
}

void loop() {
  char customKey = customKeypad.getKey();
  if (customKey) {
    //Print de key char from hexaKeys matrix
    Serial.println(customKey);
  }
}