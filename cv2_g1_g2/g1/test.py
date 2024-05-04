import serial


ser = serial.Serial('COM15', 9600)
ser.write(b'1')


ser.close()