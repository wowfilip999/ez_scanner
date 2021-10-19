a = 0
import time
import socket
s = socket.socket()
ip = input("ip: ")
portstart = input("from : ")
portend = input("to : ")
delay = input("delay y/n/custom : " )
if delay == "custom":
  custm = input("custom delay : ")

for a in range(int(portstart), int(portend)):
   try:
       s.connect((ip, int(a)))
       s.close()
       status = "open"
   except:
       status = "closed"

   print("port " + str(a)  + "" +  status)
   if delay == "y":
     time.sleep(0.7)
   if delay == "n":
     pass
   if delay == "custom":
     time.sleep(int(custm))
