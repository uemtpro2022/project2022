import serial
import time

ser=serial.Serial('COM7', 9600, timeout=1)
#ser.readline()
#not_used = ser.readline()
time.sleep(1)
print(ser)
print("START")
"""
line = ser.readline()   # 行終端まで読み込む
line = line.rstrip()
print("START")
print(line)
ser.close()
exit()
"""

while True:
    #count_arduino = ser.readline()
    # val_decoded = float(repr(val_arduino.decode())[1:-5])
    #count_decoded = count_arduino
    line = ser.readline()   # 行終端まで読み込む
    line = line.rstrip()
    #print(count_decoded)
    print(line)


#ser.close()