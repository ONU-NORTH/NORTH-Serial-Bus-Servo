/*
The normal write example passed the test in ST3215 Servo, 
and if testing other models of ST series servos
please change the appropriate position, speed and delay parameters.
*/

#include <SCServo.h>

SMS_STS st;

// the UART used to control servos.
// GPIO 18 - S_RXD, GPIO 19 - S_TXD, as default.
#define S_RXD 18
#define S_TXD 19

void setup()
{
  Serial.begin(115200);
  Serial1.begin(1000000, SERIAL_8N1, S_RXD, S_TXD);
  st.pSerial = &Serial1;
  delay(1000);
  
  //for (int i = 0; i <= 3; i++) {
    
    //commands to run 3 times at startup
    
  //}
    
}

void loop()
{
    //raise arm
    st.WritePosEx(1, 1024, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=700.
    st.WritePosEx(2, 1024, 700, 40); // servo(ID2) speed=700，acc=40，move to position=700.
    delay(1500);
    //wave twice
    st.WritePosEx(4, 2400, 1000, 50); // servo(ID4) speed=500，acc=40，move to position=1536.
    delay(700);
    st.WritePosEx(4, 1536, 1000, 50); // servo(ID4) speed=500，acc=40，move to position=2560.
    delay(700);
    st.WritePosEx(4, 2400, 1000, 50); // servo(ID4) speed=500，acc=40，move to position=1536.
    delay(700);
    st.WritePosEx(4, 1536, 1000, 50); // servo(ID4) speed=500，acc=40，move to position=2560.
    delay(700);

    //lower arm
    st.WritePosEx(1, 2048, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=-30.
    st.WritePosEx(2, 2048, 700, 40); // servo(ID2) speed=700，acc=40，move to position=-30.
    delay(3000);
    

    
}
