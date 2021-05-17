'''
i2c_v1.py
Simple Python 3 script to test I2C
Tested on Raspberry Pi 4 B+ and Adafruit Feather M4 Express
'''
import smbus
import time
import sys
bus = smbus.SMBus(1)
address = 0x04              # Arduino I2C Address
def main():
    
    PWMpercent = 50         # PWM pin 11
    data6 = [0x00]          # Pin 6 GPIO 
    
    while 1:
      '''
      #1  Write DAC
      Voltage = 2
      ADC = int(Voltage / 3.3 * 1023)
      msb = ((ADC & 0xFF00)  >> 8)
      lsb = (ADC & 0xFF)
      offset = 1
      DACdata = [msb, lsb]
      bus.write_i2c_block_data(address, offset, DACdata)
      print ("%s %5.2f" % ("Write A0:", Voltage))
      time.sleep(5)
      '''
      
      #2 Read A1
      offset = 2
      numBytes = 2    
      block = bus.read_i2c_block_data(address, offset, numBytes)
      ADCvalue = (block[0]<<8) + block[1]
      Voltage = ADCvalue / 1023 * 3.3
      print("%s %7.3f" % ("Read A1:", Voltage))
        
      #3 Read A2
      offset = 3
      numBytes = 2    
      block = bus.read_i2c_block_data(address, offset, numBytes)
      ADCvalue = (block[0]<<8) + block[1]
      Voltage = ADCvalue / 1023 * 3.3
      print("%s %7.3f" % ("Read A2:", Voltage))
        
      #4 Read A3
      offset = 4
      numBytes = 2    
      block = bus.read_i2c_block_data(address, offset, numBytes)
      ADCvalue = (block[0]<<8) + block[1]
      Voltage = ADCvalue / 1023 * 3.3
      print("%s %7.3f" % ("Read A3:", Voltage))
      
      #5 Read A4
      offset = 5
      numBytes = 2    
      block = bus.read_i2c_block_data(address, offset, numBytes)
      ADCvalue = (block[0]<<8) + block[1]
      Voltage = ADCvalue / 1023 * 3.3
      print("%s %7.3f" % ("Read A4:", Voltage))
      
      #6 Read A5
      offset = 6
      numBytes = 2    
      block = bus.read_i2c_block_data(address, offset, numBytes)
      ADCvalue = (block[0]<<8) + block[1]
      Voltage = ADCvalue / 1023 * 3.3
      print("%s %7.3f" % ("Read A5:", Voltage))
      
      #7 Write O5
      offset = 7
      data = [0x01]
      bus.write_i2c_block_data(address, offset, data)
      print ("%s %d" % ("Write 5:  ",data[0]))
      
      #8 Write O6
      offset = 8
      bus.write_i2c_block_data(address, offset, data6)
      print ("%s %d" % ("Write 6:  ",data6[0]))
      
      #9 Read I9
      offset = 9
      numBytes = 1
      block = bus.read_i2c_block_data(address, offset, numBytes)
      print("%s %2d" % ("Read 9:  ", block[0]))
      
      #10 Write PWM
      PWM = int(PWMpercent / 100 * 255)
      msb = (PWM & 0xFF00)  >> 8
      lsb = PWM & 0xFF
      offset = 10
      data = [msb, lsb]
      bus.write_i2c_block_data(address, offset, data)
      print ("%s %2d" % ("Write PWM:", PWMpercent))
      # time.sleep(0.001)
      
      #11 Write LED
      offset = 11
      # turn LED on
      data = [0x01]
      bus.write_i2c_block_data(address, offset, data)
      print ("%s %d" % ("Write LED:",data[0]))
      time.sleep(.5)
      # turn LED off 
      data = [0x00]
      bus.write_i2c_block_data(address, offset, data)
      print ("%s %d" % ("Write LED:", data[0]))
      
      #12 Read ID
      offset = 12
      numBytes = 2
      block = bus.read_i2c_block_data(address, offset, numBytes)
      print("Address:  ", block[0])
      print("%s %d" % ("version:  ", block[1]))
      print ("")
      
      print("Enter p to change PWM")
      print("Enter 6 to change pin 6 state")
      doNext = input("Enter q to quit: ")
      if (doNext == "q"):
            break
      elif (doNext == "p"):
            PWMPercent = input("PWM, 0 to 100: ")
            try:
                val = int(PWMPercent)
                PWMpercent = val
                if (PWMpercent > 100):
                    PWMpercent = 100
                if (PWMpercent < 0):
                    PWMpercent = 0
            except ValueError:
                print ("*** qNot an integer")
      elif (doNext == "6"):
            if (data6 == [0x00]):
                data6 = [0x01]
            else:
                data6 = [0x00]
      print('\n\n')
      
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        gpio.cleanup()
        sys.exit(0)
