#!/usr/bin/python3

import time
import requests, json
from influxdb import InfluxDBClient as influxdb
import serial

seri = serial.Serial('/dev/ttyACM0', baudrate = 9600, timeout = None)


while(True):
    time.sleep(1)
    if seri.in_waiting !=0:
      content = seri.readline()
      a = float(content.decode())
      data = [{
          'measurement' : 'dust',        
          'tags':{
              'InhaUni' : '2222',
          },
          'fields':{
              'dust' : a,
          }
      }]
      client = None
      try:
          client = influxdb('localhost',8086,'root','root','dust')
      except Exception as e:
        print ("Exception" + str(e))
      if client is not None:
          try:
              client.write_points(data)
          except Exception as e:
              print("Exception write " + str(e))
        finally:
            client.close()
      print("running influxdb OK")
      
      
      
      
      ## !pir_influxdb

import time
import RPi.GPIO as GPIO
import requests, json
from influxdb import InfluxDBClient as influxdb

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)

def interrupt_fired(channel):
    print("interrupt Fired")
    a = 5
    data = [{
        'measurement' : 'pir',        
        'tags':{
            'VisionUni' : '2410',
        },
        'fields':{
            'pir' : a,
        }
    }]
    client = None
    try:
        client = influxdb('localhost',8086,'root','root','pir')
    except Exception as e:
        print("Exception" + str(e))
    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print("Exception write " + str(e))
        finally:
            client.close()
    print(a)
GPIO.add_event_detect(14, GPIO.FALLING, callback=interrupt_fired)

while(True):
    time.sleep(1)
    a = 1
    data = [{
        'measurement' : 'pir',        
        'tags':{
            'VisionUni' : '2410',
        },
        'fields':{
            'pir' : a,
        }
    }]
    client = None
    try:
        client = influxdb('localhost',8086,'root','root','pir')
    except Exception as e:
        print ("Exception" + str(e))
    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print("Exception write " + str(e))
        finally:
            client.close()
    print("running influxdb OK")##


## !dust_influxdb
import time
import requests, json
from influxdb import InfluxDBClient as influxdb
import serial
##