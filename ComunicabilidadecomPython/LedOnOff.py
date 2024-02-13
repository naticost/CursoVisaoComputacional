import serial
import time 

conexao = serial.Serial('COM5', baudrate=9600)

time.sleep(2)

def arduino ():
    msg = input('EScolha uma opção (On/Off) : ')
    conexao.write(msg.encode('ascii'))

    arduino()
 
arduino()