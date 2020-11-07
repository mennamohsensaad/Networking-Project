#
import socket 
import numpy as np
from PyQt5 import QtWidgets, QtCore ,Qt
from PyQt5.QtWidgets import  QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from Doctor2 import Ui_MainWindow
import sys
import os  
import time
import cv2
#from PIL import Image
import random

#Create a socket instance
#socketObject = socket.socket()
#Using the socket connect to a server...in this case localhost
class runClient(QtWidgets.QMainWindow):
  def __init__(self):
        super(runClient, self).__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Send.clicked.connect(self. send)
        self.ui.saveButton.clicked.connect(self. save_img)
        
  def send(self):      
        while True:
        
            MESSAGE = (self.ui.PatientCode.text())
            n = random.random()
            print(MESSAGE)
            if MESSAGE != 'exit' or MESSAGE == "0":
            
              socketObject = socket.socket()
              socketObject.connect((socket.gethostname(), 2004))
              print("client1_Connected to localhost")
              socketObject.send(str.encode(MESSAGE))
    
            while MESSAGE != 'exit' or MESSAGE == "no" :
                
            
                split1=MESSAGE.split()
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
                    print("File has been received_client1.")
                    file.close()
                else:
    
                    img_filtered = open(""+str(n)+".jpg", 'ab')
                    print("1")
                    returned_data = socketObject.recv(1024)
                    while True:
                        if returned_data.endswith(str.encode('done')):
                            img_filtered.write(returned_data[:-4])
                            break
                 #       print("2")
                        img_filtered.write(returned_data)
                        returned_data = socketObject.recv(1024)
                    print("3")
                    img_filtered.close()
                    print("4")
       
          #      MESSAGE = 'exit'
                
                if split2 !="v":
                    pixmap = QPixmap(""+str(n)+".jpg")
                    pixmap = pixmap.scaled(1024, 1024, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
                    self.ui.label_4.setPixmap(pixmap)
                if split2=="v":
                    cap = cv2.VideoCapture(""+str(n)+".MP4")
                    
                    while True:
                        ret, frame = cap.read(500)
                        if not ret:
                            break
                    
                     
                        time.sleep(.1)
                        cv2.imshow('ImageWindow',frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                              break
 
                    cap.release()
                    
              #  code = (self.ui.PatientCode.text())
             #   print(code)
                try:
                    socketObject.send(str.encode(MESSAGE))
               
          #      socketObject.send(str.encode(code))
            ##  print(code)
                    NAME = socketObject.recv(1024)
                    NAME=str(NAME.decode("utf-8"))
                    pieces= NAME.split()
                   
                    print(pieces[0],pieces[1])
                    self.ui.lineEdit.setText(""+pieces[0]+" "+pieces[1]+"")
                    self.ui.lineEdit_2.setText(""+pieces[2]+"")
                    self.ui.lineEdit_3.setText(""+pieces[3]+"")
                    self.ui.lineEdit_4.setText(""+pieces[4]+"")
                    self.ui.lineEdit_5.setText(""+pieces[5]+"")
                    self.ui.lineEdit_6.setText(""+pieces[6]+"")
                except:
                    print("video")
                self.ui.PatientCode.textchanged("0")
                MESSAGE = 'exit'
            socketObject.close()
  def save_img(self):
        code = (self.ui.PatientCode.text()) 
        self.im =self.im.save("patient code"+str(code)+".jpg")
        os.remove(self.MM)
        
        
 
      
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = runClient()
    application.show()

  
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()