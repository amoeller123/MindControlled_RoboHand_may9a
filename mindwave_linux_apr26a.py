from NeuroPy import NeuroPy
import bluetooth
import time
import serial
import sys

time.sleep(5) #Timer for Bluetooth to become ready

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.bind(("00:00:00:00:00:00", 1))

object1=NeuroPy("/dev/rfcomm0", 57600)
ser = serial.Serial('/dev/ttyUSB0', 9600);

def attention_callback(attention_value):
    print "Attention is",attention_value
    return None

def meditation_callback(meditation_value):
    print "Meditation is",meditation_value
    return None

#Set call back:
object1.setCallBack("attention",attention_callback)
object1.setCallBack("meditation",meditation_callback)

#Call start method
object1.start()

while True:
    if(object1.attention > 70):
        ser.write(chr(1))
        time.sleep(1)
    if(object1.meditation > 70):
        ser.write(chr(2))
        time.sleep(1)

        
ser.close();
sock.close()
