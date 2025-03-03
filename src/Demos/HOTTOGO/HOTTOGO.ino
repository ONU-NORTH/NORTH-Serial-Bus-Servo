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
    //H
    st.WritePosEx(5, 2152, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(6, 3696, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(7, 2761, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(8, 2760, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    delay(2100);

    //O
    st.WritePosEx(5, 2152, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(6, 3709, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(7, 2761, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(8, 2112, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    delay(1000);

    //T
    st.WritePosEx(5, 2152, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(6, 2969, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(7, 2761, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(8, 2913, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    delay(800);

    //T up
    st.WritePosEx(5, 2152, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(6, 3100, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(7, 2761, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(8, 2913, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    delay(400);

    //T
    st.WritePosEx(5, 2152, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(6, 2969, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(7, 2761, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(8, 2913, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    delay(1000);

    //O
    st.WritePosEx(5, 2152, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(6, 3709, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(7, 2761, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(8, 2112, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    delay(1500);

    //G
    st.WritePosEx(5, 2152, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(6, 3067, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(7, 2761, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(8, 1768, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    delay(700);

    //O
    st.WritePosEx(5, 2152, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(6, 3709, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(7, 2761, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    st.WritePosEx(8, 2112, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=.
    delay(3000);

    //lower arm
    st.WritePosEx(5, 2048, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=-30.
    st.WritePosEx(6, 2048, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=-30.
    st.WritePosEx(7, 2048, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=-30.
    st.WritePosEx(8, 2048, 1000, 40); // servo(ID1) speed=1000，acc=40，move to position=-30.
    delay(3000);
    

    
}
