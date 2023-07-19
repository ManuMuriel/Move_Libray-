import pyfirmata2
import time 
delay = 0.1 
pin = 6 

port = pyfirmata2.Arduino.AUTODETECT 
board = pyfirmata2.Arduino(port)
board. samplingOn(100)
board.analog[0].enable_reporting()

while True:
    x = board.analog[0].read()
    if x is None:
        continue
    else:
        data = x * 5 
        print(data)
        if data > 3.0:
            board.digital[pin].write(1)
        else:
            board.digital[pin].write(0)
    
    time.sleep(delay)



