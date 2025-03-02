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
}

void loop()
{
    //raise arm
    st.WritePosEx(1, 1024, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=700.
    delay(800);
    
    //wave twice
    st.WritePosEx(3, 2400, 3000, 50); // servo(ID3) speed=2000，acc=50，move to position=2400.
    delay(600);
    st.WritePosEx(3, 1672, 3000, 50); // servo(ID3) speed=2000，acc=50，move to position=1672.
    delay(600);
    st.WritePosEx(3, 2400, 3000, 50); // servo(ID3) speed=500，acc=50，move to position=2800.
    delay(600);
    st.WritePosEx(3, 1672, 3000, 50); // servo(ID3) speed=500，acc=50，move to position=1330.
    delay(600);
    st.WritePosEx(3, 2048, 3000, 50); // servo(ID3) speed=500，acc=50，move to position=2048.
    delay(600);

    //lower arm
    st.WritePosEx(1, 2048, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=-30.
    delay(3000);
    

    
}
