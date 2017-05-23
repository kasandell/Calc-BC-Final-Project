bool buttonPressed = false;
int analogPin = A3;
int val = 0;
int buttonPin = 3;
int buttonState = 0;
int sv3 = 0;
int t = 0;
float acceleration = 0;
float unitsToMs = (.0049) * (3/1.5) * (9.81/1.000342); // volts/unit * g's/volts * m/s^2/g's

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
  buttonPressed = false;
  t = 0;

}

void loop() {
  analogReference(EXTERNAL);
  // put your main code here, to run repeatedly:
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH)
  {
    buttonPressed = true;
  }
  if (buttonPressed == true)
  {
    sv3 = analogRead(analogPin);
    t = millis();
    val = map(sv3, 0, 1023, -511, 512); 
    acceleration = (val * 1.0) * unitsToMs;
    Serial.println(String(t) + "," + String(acceleration));
  }
  delay(2);
}