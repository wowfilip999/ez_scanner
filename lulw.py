a = 0
import time
import socket
s = socket.socket()


def single():
 ip = input("ip : ")
 port = input("port : ")

 try:
     s.connect((ip, int(port)))
     status = "open"
 except:
     status = "closed"

 print(str(port)  +  status + " on " +  str(ip))
def multi():
 ip = input("ip : ")
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

    print("port " +  str(a)   +  status + " on " + str(ip))
    if delay == "y":
      time.sleep(0.7)
    if delay == "n":
      time.sleep(0)
    if delay == "custom":
      time.sleep(int(custm))



while True:
  mode = input("multi/single : ")
  if mode == "multi":
    multi()
  if mode == "single":
    single()
