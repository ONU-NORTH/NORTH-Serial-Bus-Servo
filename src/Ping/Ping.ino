

/*
Ping the servo to check if it is ready.
*/

#include <SCServo.h>
#include <SoftwareSerial.h>

SMS_STS sms_sts;
// the uart used to control servos.
// GPIO 18 - S_RXD, GPIO 19 - S_TXD, as default.
#define S_RXD 2
#define S_TXD 3

int TEST_ID = 1;

SoftwareSerial mySerial(2, 3); // RX, TX pins for your external device

void setup()
{
  Serial.begin(115200);
  mySerial.begin(1000000);
  sms_sts.pSerial = &mySerial;
  delay(1000);
}

void loop()
{
  int ID = sms_sts.Ping(TEST_ID);
  if(ID!=-1){
    Serial.print("Servo ID:");
    Serial.println(ID, DEC);
    delay(100);
  }else{
    Serial.println("Ping servo ID error!");
    delay(2000);
  }
}
