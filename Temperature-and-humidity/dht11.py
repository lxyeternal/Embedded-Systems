import time
import RPi.GPIO as GPIO
from mysql_insert import *

channel =21
data_time = 20190400
while(True):

    for k in range(30):
        data_time = data_time + 1
        tem_list = []
        hum_list = []
        for i in range(12):
            data = []
            j = 0
            time.sleep(1)
            GPIO.setmode(GPIO.BCM)
            time.sleep(1)
            GPIO.setup(channel, GPIO.OUT)
            GPIO.output(channel, GPIO.LOW)
            time.sleep(0.02)

            GPIO.output(channel, GPIO.HIGH)
            GPIO.setup(channel, GPIO.IN)

            while GPIO.input(channel) == GPIO.LOW:
              continue
            while GPIO.input(channel) == GPIO.HIGH:
              continue

            while j < 40:
              k = 0
              while GPIO.input(channel) == GPIO.LOW:
                continue
              while GPIO.input(channel) == GPIO.HIGH:
                k += 1
                if k > 100:
                  break
              if k < 8:
                data.append(0)
              else:
                data.append(1)

              j += 1

            humidity_bit = data[0:8]
            humidity_point_bit = data[8:16]
            temperature_bit = data[16:24]
            temperature_point_bit = data[24:32]
            check_bit = data[32:40]
            humidity = 0
            humidity_point = 0
            temperature = 0
            temperature_point = 0
            check = 0

            for i in range(8):
              humidity += humidity_bit[i] * 2 ** (7-i)
              humidity_point += humidity_point_bit[i] * 2 ** (7-i)
              temperature += temperature_bit[i] * 2 ** (7-i)
              temperature_point += temperature_point_bit[i] * 2 ** (7-i)
              check += check_bit[i] * 2 ** (7-i)

            tmp = humidity + humidity_point + temperature + temperature_point

            if check == tmp:
                tem_list.append(temperature)
                hum_list.append(humidity)
                print("temperature : ", temperature, " C humidity:", humidity, "%")
                vul_list = vul_data(temperature,humidity)
                insert_vul(vul_list)
            else:
                temperature = 25
                humidity = 50
                tem_list.append(temperature)
                hum_list.append(humidity)
                print("temperature : ", temperature, " C humidity:", humidity, "%")
            GPIO.cleanup()
            GPIO.cleanup()
            GPIO.cleanup()
        tem_list = deal_data(tem_list)
        hum_list = deal_data(hum_list)
        unite_list = unite_data(data_time,tem_list,hum_list)
        # insert_data(unite_list)
        print(unite_list)