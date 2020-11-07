
import socket 
from threading import Thread 
from socketserver import ThreadingMixIn 

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print ("[+] New server socket thread started for " + ip + ":" + str(port) )
    def run(self): 
      #  while True :
            self.flag=True
            self.data = conn.recv(2048) 
            print( "Server received data:", self.data)
           # if  data== b'hh':
            self.check_code()
            if self.flag==True:
          #  img1 = open('filtred.jpg', 'rb')
                self.data = self.img .read(1024)
        
                # add "done" at the end of our data to make the server stop waiting for more bytes
                while (self.data != b''):
                    conn.send(self.data)
                    self.data = self.img .read(1024)
                  #  print(data)
                    print("done")
                conn.send(str.encode('done'))
        
                self.img .close()
#                self.data = conn.recv(2048)
#                self.send_information()
            
            else:    
                with conn:
                    with open('VIDEO1.MP4', 'rb') as file:
                      sendfile = file.read()
                    conn.sendall(sendfile)
                    print('file sent')
            self.data = conn.recv(2048)
            self.send_information()
#        else:   
#            img1 = open('2.jpg', 'rb')
#            data = img1.read(1024)
#    
#            # add "done" at the end of our data to make the server stop waiting for more bytes
#            while (data != b''):
#                conn.send(data)
#                data = img1.read(1024)
#             #   print(data)
#                print("done")
#            conn.send(str.encode('done'))
#    
#            img1.close()
            
    def check_code(self):

       if self.data ==b'1' :
            self.flag=True
            self.img = open('1.jpg', 'rb')
       elif self.data ==b'2' :
            self.img = open('2.jpg', 'rb')
            self.flag=True
       elif self.data == b'3':
            self.img = open('3.jpg', 'rb')
            self.flag=True
       elif self.data == b'4':
            self.img = open('4.jpg', 'rb')
            self.flag=True
       elif self.data== b'5 v': 
            self.flag=False
       elif self.data== b'5':
            self.img = open('5.jpg', 'rb')
            self.flag=True     
       else:
            self.img = open('6.jpg', 'rb')
            self.flag=True
          #  data = conn.recv(2048) 
          #  print( "Server received data:", data)
          #  MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
          #  if MESSAGE == 'exit':
          #      break
          #  conn.send(str.encode(MESSAGE))  # echo 
    def send_information(self):
           if self.data ==b'1' :
               conn.send(str.encode('Ahmed Ashraf Male 32 23/12/2019 Brain MRI'))
           elif self.data ==b'2' :
               conn.send(str.encode('Salma Mohamed Female 29 23/12/2019 Lung MRI'))
           elif self.data == b'3':
                conn.send(str.encode('Mohamed Sayed Male 44 23/12/2019 leg X-Ray'))
           elif self.data == b'4':
                 conn.send(str.encode('Noha Mohamed Female 23 23/12/2019 Eye COT'))
           elif self.data== b'5': 
                conn.send(str.encode('shery Ahmed Female 35 23/12/2019 fetus US'))
              #  print("kk")
           elif self.data== b'5 v': 
           #     conn.send(str.encode('shery Ahmed Female 35 23/12/2019 fetus US'))
                print("kk")     
           else:
                conn.send(str.encode('Notfound  .  Notfound Notfound Notfound Notfound Notfound'))
# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0' 
TCP_PORT = 2004 
BUFFER_SIZE = 20  # Usually 1024, but we need quick response 

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
while True: 
    tcpServer.listen(4) 
    print( "Multithreaded Python server : Waiting for connections from TCP clients..." )
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 