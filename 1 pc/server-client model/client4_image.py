
import socket 
import numpy as np
from PyQt5 import QtWidgets, QtCore ,Qt
from PyQt5.QtWidgets import  QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from TCPClient2 import Ui_MainWindow
from PIL import Image
import PIL
import scipy.misc
from PIL.ImageQt import ImageQt 
import sys
import os  
import time
import cv2
from PIL import Image
import random


#Using the socket connect to a server...in this case localhost
class runClient(QtWidgets.QMainWindow):
  def __init__(self):
        super(runClient, self).__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Send.clicked.connect(self. send)
        
  def send(self):      
        while True:
          
            MESSAGE = (self.ui.PatientCode.text())
            n = random.random()
            print(MESSAGE)
            if MESSAGE != 'exit' or MESSAGE == "0":
            # Receive the data
              socketObject = socket.socket()
              #_____________________________________FOR WIRED ON 2 PC________________________________________________________
              #socketObject.connect(("192.168.1.20", 2004))
              #___________________________________FOR WIRLESS ON 2 PC_________________________________________________________
              #socketObject.connect(("192.168.173.1", 2004))
             #___________________________________FOR SAME PC _________________________________________________________
              socketObject.connect((socket.gethostname(), 2004))
              print("Connected to localhost")
              socketObject.send(str.encode(MESSAGE))
      
            while MESSAGE != 'exit' or MESSAGE == "no" :
                
                split1=MESSAGE.split(" ")
                print(split1)
                try:
                 split2=split1[1]
                 print(split2)
                except:
                   print("not video") 
                   split2="p"
                if split2=="v":
                    with socketObject,open(""+str(n)+".MP4",'wb') as file:
                        while True:
                            recvfile = socketObject.recv(4096)
                            if not recvfile: break
                            file.write(recvfile)
                    print("File has been received.")
                else:
      
                    img_filtered = open(""+str(n)+".jpg", 'ab')
                    print("1")
                    returned_data = socketObject.recv(1024)
                    while True:
                        if returned_data.endswith(str.encode('done')):
                            img_filtered.write(returned_data[:-4])
                            break
               
                        img_filtered.write(returned_data)
                        returned_data = socketObject.recv(1024)
                    print("3")
                    img_filtered.close()
                    print("4")
          
                MESSAGE = 'exit'
        
                if split2 !="v":
                    pixmap = QPixmap(""+str(n)+".jpg")
                    pixmap = pixmap.scaled(1024, 1024, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                    self.ui.label_3.setPixmap(pixmap)
                if split2=="v":
                    cap = cv2.VideoCapture(""+str(n)+".MP4")
                    
                    while True:
                        ret, frame = cap.read(500)
                        if not ret:
                            break
                    
                        time.sleep(.1)
                        cv2.imshow('ImageWindow',frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
  
                    cap.release()

            socketObject.close()
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = runClient()
    application.show()

  
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()