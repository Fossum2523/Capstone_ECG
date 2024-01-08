from asyncore import write
import struct
import sys
import cv2
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QLabel, QPushButton
import pyqtgraph as pg
from random import randint
import serial
import serial.tools.list_ports
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import *
import requests as req
from urllib import parse
from PyQt5.QtGui import QIcon
import  PyQt5.QtGui
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

guta_list=list(range(0,100))

sample_num=40





class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()
        self.setWindowTitle("遠端健康檢測裝置")
        self.setWindowIcon(QIcon('C:/Users/USER/Desktop/Formal_Race_Code/python/fes.png'))
        #self.setWindowIcon(QIcon('C:/Users/USER/Desktop/race/python/Pyqt5_picture/bitbug_favicon.ico'))
        self.ser = serial.Serial()
        
        # self.port_check()

    def initUI(self):
         # Window size
        self.WIDTH = 1920
        self.HEIGHT = 1000
        self.resize(self.WIDTH, self.HEIGHT)

        # Widget
        self.centralwidget = QWidget(self)
        self.centralwidget.resize(self.WIDTH, self.HEIGHT)

        # Initial
        #self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.99)

        radius = 0
        self.centralwidget.setStyleSheet(
            """
            background:rgb(131, 176, 214);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )
        
        #pw1 start-------------------------------------------
        self.pw1 = pg.PlotWidget()
        '''self.pw.setYRange(min=300000, # 最小值
                          max=400000)  # 最大值
        self.pw.setXRange(min=0, # 最小值
                          max=100)  # 最大值'''
        self.pw1.setBackground('w')
        self.pw1.showGrid(x=True, y=True)
        self.curve_pw1 = self.pw1.plot(
            pen=pg.mkPen('r', width=1)
        )
        self.pw1.setTitle("PPG-IR",
                         color='008080',
                         size='12pt')
        #pw1 end---------------------------------------------

        #pw2 start-------------------------------------------
        self.pw2 = pg.PlotWidget()
        '''self.pw.setYRange(min=300000, # 最小值
                          max=400000)  # 最大值
        self.pw.setXRange(min=0, # 最小值
                          max=100)  # 最大值'''
        self.pw2.setBackground('w')
        self.pw2.showGrid(x=True, y=True)
        self.curve_pw2 = self.pw2.plot(
            pen=pg.mkPen('r', width=1)
        )
        self.pw2.setTitle("PPG-RED",
                         color='008080',
                         size='12pt')
        #pw2 end---------------------------------------------

        #pw3 start-------------------------------------------
        self.pw3 = pg.PlotWidget()
        '''self.pw3.setYRange(min=300000, # 最小值
                          max=400000)  # 最大值
        self.pw3.setXRange(min=0, # 最小值
                          max=100)  # 最大值'''
        self.pw3.setBackground('w')
        self.pw3.showGrid(x=True, y=True)
        self.curve_pw3 = self.pw3.plot(
            pen=pg.mkPen('r', width=1)
        )
        self.pw3.setTitle("ECG",
                         color='008080',
                         size='12pt')
        #pw3 end---------------------------------------------
        # self.test_R=np.loadtxt("1000.txt")
        # print(self.test_R)
        self.BP_slope=-0.24632823514346805
        self.BP_c=136.26511549847567
        self.traing_stop = 0
        self.ECG_mode = 5 # 0 => normal mode, 1 => traning mode, 2 => testing mode
        self.test1=0
        self.i = 0
        self.x = [] # x軸的值

        self.IR_DC_list = [] # y軸的值
        self.RD_DC_list = [] # y軸的值
        self.ECG_label_num=0
        self.ECG_label=[]
        self.ECG_traing_list =[]
        self.raw_heartbeat=[]
        self.ECG_list = [] # y軸的值

        self.fewef=0
        self.sample_time=0
        self.sample_times=1

        '''self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateData)
        self.timer.start(100)'''
        
        #self.pw.setMouseTracking(True)

        #normal mode buttom
        self.btn_normal = QPushButton('Normal Mode', self)
        self.btn_normal.setStyleSheet(''' 
                     QPushButton
                     {text-align : center;
                     background-color : white;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 17px;}
                     QPushButton:pressed
                     {text-align : center;
                     background-color : light gray;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 17px;}
                     ''')
        #traning mode buttom
        self.btn_traning = QPushButton('Traning Mode', self)
        self.btn_traning.setStyleSheet(''' 
                     QPushButton
                     {text-align : center;
                     background-color : white;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 17px;}
                     QPushButton:pressed
                     {text-align : center;
                     background-color : light gray;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 17px;}
                     ''')

        #testing mode buttom 
        self.btn_testing = QPushButton('Testing Mode', self)
        self.btn_testing.setStyleSheet(''' 
                     QPushButton
                     {text-align : center;
                     background-color : white;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 17px;}
                     QPushButton:pressed
                     {text-align : center;
                     background-color : light gray;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 17px;}
                     ''')

        self.btnOpen = QPushButton('Open Serial', self)
        self.btnOpen.setStyleSheet(''' 
                     QPushButton
                     {text-align : center;
                     background-color : white;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 17px;}
                     QPushButton:pressed
                     {text-align : center;
                     background-color : light gray;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 17px;}
                     ''')
        #self.btnOpen.setObjectName("radioButton_1")
        self.btnclose = QPushButton('Close Serial', self)
        self.btnclose.setStyleSheet(''' 
                     QPushButton
                     {text-align : center;
                     background-color : white;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 17px;}
                     QPushButton:pressed
                     {text-align : center;
                     background-color : light gray;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 17px;}
                     ''')
        #SPo2----------------------------------------
        self.SPo2_fnt = QLabel( self)
        self.SPo2_fnt.setText('SpO2 (%)')
        self.SPo2_fnt.setStyleSheet("font-size:20px;font-weight:bold;font-family:Roman times;color: #000000;")
        self.SPo2_fnt.move(15,0)
        self.SPo2_fnt.resize(500,100)
        # self.SPo2_fnt.setVisible(True)

        self.SPo2_box = QLineEdit(self)
        self.SPo2_box.move(10, 70)
        self.SPo2_box.setStyleSheet("font-size:20px")
        self.SPo2_box.setText('0')
        #SPo2----------------------------------------
        
        #heartbeat---------------------------------------
        self.heartbeat_fnt = QLabel(self)
        self.heartbeat_fnt.setText('HR (bpm)')
        self.heartbeat_fnt.setStyleSheet("font-size:20px;font-weight:bold;font-family:Roman times;color: #000000;")
        self.heartbeat_fnt.move(15,90)
        self.heartbeat_fnt.resize(500,100)
        # self.SPo2_fnt.setVisible(True)

        self.heatbeat_box = QLineEdit(self)
        self.heatbeat_box.move(10, 160)
        self.heatbeat_box.setStyleSheet("font-size:20px")
        self.heatbeat_box.setText('0')

        print(self.heatbeat_box.text())
        #heartbeat---------------------------------------


        layout = QGridLayout(self)
        layout.addWidget(self.pw3, 0, 2, 8, 8)
        layout.addWidget(self.btn_normal, 2, 0, 1, 1)
        layout.addWidget(self.btn_traning, 3, 0, 1, 1)
        layout.addWidget(self.btn_testing, 4, 0, 1, 1)
        layout.addWidget(self.btnOpen, 6, 0, 1, 1)
        layout.addWidget(self.btnclose, 7, 0, 1, 1)
    
    def init(self):

        # 打開串口按钮
        self.btnOpen.clicked.connect(self.port_open)

        # 關閉串口按钮
        self.btnclose.clicked.connect(self.port_close)

        #normal mode
        self.btn_normal.clicked.connect(self.normal_mode)

        #traing mode
        self.btn_traning.clicked.connect(self.traing_mode)

        #testing mode
        self.btn_testing.clicked.connect(self.testing_mode)
        # 定時器接收數據
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.data_receive)

    # 打開串口
    def port_open(self):
        
        self.test1=0
        self.ser.port = 'COM4'
        self.ser.baudrate = 38400
        self.ser.open()

        # 打開串口接收定器，周期為2ms
        self.timer.start(0.01)

        if self.ser.isOpen():
            print("串口已開啟")

    # 關閉串口
    def port_close(self):
        self.ser.write('E'.encode())
        self.traing_stop = 0
        self.test1=1
        self.timer.stop()
        self.i=0
        self.ECG_list=[]
        self.x=[]
        self.curve_pw3.setData(self.x,self.ECG_list)
        #self.timer_send.stop()
        try:
            self.ser.close()
        except:
            pass

    # 接收数据
    def data_receive(self):
        #ECG_mode = Normal start--------------------------------------------------------
        if self.ECG_mode == 0 :
            self.traing_stop = 0
            #Get ECG signal start-------------------------------------------------------
            data =  self.ser.read(1)
            if data == b'A':

                data_raw_1 = self.ser.read(4) 
                guta_1 = bytearray()

                guta_1.append(data_raw_1[3])				
                guta_1.append(data_raw_1[2])				
                guta_1.append(data_raw_1[1])				
                guta_1.append(data_raw_1[0])

                a,=struct.unpack('!f',guta_1)#ECG
                
                if   a<=10000000 and a >=0: 
                    print("ECG=",a)
                    self.x.append(self.i)
                    self.i += 1
                    self.ECG_list.append(a)
                    
            #Get ECG signal end---------------------------------------------------------

            #Get RD  signal start-------------------------------------------------------
            data =  self.ser.read(1)
            if data == b'B':

                data_raw_1 = self.ser.read(4) 
                guta_1 = bytearray()

                guta_1.append(data_raw_1[3])				
                guta_1.append(data_raw_1[2])				
                guta_1.append(data_raw_1[1])				
                guta_1.append(data_raw_1[0])

                a,=struct.unpack('!f',guta_1)#IR

                if   a<=10000000 and a >=0:
                    print("IR=",a)
                    self.IR_DC_list.append(a)
                    if len(self.x) <=200:
                        self.curve_pw3.setData(self.x,self.IR_DC_list)
                    else:
                        self.curve_pw3.setData(self.x[self.i-200:self.i],self.IR_DC_list[self.i-200:self.i])
            #Get RD  signal end-------------------------------------------------------

            #Get IR  signal start-----------------------------------------------------
            data =  self.ser.read(1)
            if data == b'C':
                
                data_raw_1 = self.ser.read(4) 
                guta_1 = bytearray()

                guta_1.append(data_raw_1[3])				
                guta_1.append(data_raw_1[2])				
                guta_1.append(data_raw_1[1])				
                guta_1.append(data_raw_1[0])

                a,=struct.unpack('!f',guta_1)#Red Light


                if   a<=10000000 and a >=0:
                    print("RD=",a)
                    self.RD_DC_list.append(a)

                    '''self.pw.setXRange(min=self.i-100, # 最小值
                        max=self.i)  # 最大值
                    if self.i>100:
                        self.pw.setYRange(min=(min(self.IR_DC_list[self.i-100:self.i])-2000), # 最小值
                            max=(max(self.IR_DC_list[self.i-100:self.i]))+2000)  # 最大值
                    else:
                        self.pw.setYRange(min=(min(self.IR_DC_list)-1500), # 最小值
                            max=(max(self.IR_DC_list))+1500)  # 最大值'''
                #Get IR  signal end-------------------------------------------------------

                    if self.i > sample_num-1:
                        self.IR_DC_num=sum(self.IR_DC_list[self.i-sample_num:self.i])/sample_num
                        self.RL_DC_num=sum(self.RD_DC_list[self.i-sample_num:self.i])/sample_num
                        self.IR_AC_maxnum=max(self.IR_DC_list[self.i-sample_num:self.i])
                        self.IR_AC_minnum=min(self.IR_DC_list[self.i-sample_num:self.i])
                        self.RL_AC_maxnum=max(self.RD_DC_list[self.i-sample_num:self.i])
                        self.RL_AC_minnum=min(self.RD_DC_list[self.i-sample_num:self.i])
                        R_num=((self.RL_AC_maxnum-self.RL_AC_minnum)/self.RL_DC_num)/((self.IR_AC_maxnum-self.IR_AC_minnum)/self.IR_DC_num)
                    else:
                        self.IR_DC_num=sum(self.IR_DC_list)/self.i
                        self.RL_DC_num=sum(self.RD_DC_list)/self.i
                        R_num=0

                    SPo2=-45.1*R_num*R_num+30.4*R_num+94.9#SPO2值

                    if SPo2 < 70:
                        SPo2 =70
                    
                    if SPo2 >100:
                        SPo2 =100
                    
                    self.SPo2_box.setText(str(int(SPo2)))

                self.ser.write('S'.encode())
            
            
        #ECG_mode = 0 end----------------------------------------------------------

        #ECG_mode = traning start--------------------------------------------------------
        if self.ECG_mode == 1 and self.traing_stop == 0:
            self.ser.write('U'.encode())
            while len(self.ECG_list) <2000:
                print(1)
                data =  self.ser.read(1)
                if data == b'C':
                    self.ECG_traing_list=[]
                    for i in range(200):
                        self.sample_time =0
                        data_raw_1 = self.ser.read(4) 
                        guta_1 = bytearray()

                        guta_1.append(data_raw_1[3])				
                        guta_1.append(data_raw_1[2])				
                        guta_1.append(data_raw_1[1])				
                        guta_1.append(data_raw_1[0])

                        c,=struct.unpack('!f',guta_1)#ECG
                        print(c)
                        c_num=float(c)

                        print(c_num)

                        

                        if   self.test1==0 and c_num<=10 and c_num >= -10: 
                            self.x.append(self.i)
                            self.i+= 1
                            self.ECG_traing_list.append(c_num)
                            self.ECG_list.append(c_num)
                            # self.curve_pw3.setData(self.x_3,self.ECG_list)
                    lp= np.loadtxt("Lyn_RP.txt")
                    lp_after =np.append(lp,self.ECG_traing_list)
                    if len(self.ECG_list) <= 200 and type(self.raw_heartbeat)==list:
                        np.savetxt("Lyn_RP.txt",lp_after)
                        self.raw_heartbeat=self.ECG_traing_list
                        # print(self.raw_heartbeat)
                    else :
                        np.savetxt("Lyn_RP.txt",lp_after)
                        self.raw_heartbeat =  np.vstack((self.raw_heartbeat,self.ECG_traing_list))
                        # print(self.raw_heartbeat)
            self.curve_pw3.setData(self.x,self.ECG_list) 

            if type(self.ECG_label)==list:
                self.ECG_label=[0]
                for i in range(4):
                    self.ECG_label= np.vstack((self.ECG_label, self.ECG_label_num)) 
            else:
                for i in range(5):
                    self.ECG_label= np.vstack((self.ECG_label, self.ECG_label_num)) 
            self.ECG_label_num=self.ECG_label_num+1
            sklda= LinearDiscriminantAnalysis()
            data_2 = sklda.fit_transform(self.raw_heartbeat, self.ECG_label)
            print(self.raw_heartbeat)
            print("traing succcess")
            self.traing_stop = 1   
        #ECG_mode = 1 start--------------------------------------------------------

        #ECG_mode = 2 start--------------------------------------------------------
        # if self.ECG_mode == 2:
            # print(1)
        #ECG_mode = 2 start--------------------------------------------------------
       
                   
        #-----------------------------------
    def normal_mode(self):
        self.ser.write('X'.encode())
        self.ECG_mode = 0
    
    def traing_mode(self):
        self.traing_stop = 0
        self.ECG_mode = 1
    
    def testing_mode(self):
        print(1)
        self.ser.write('I'.encode())
        print(1)
        data =  self.ser.read(1)
        if data == b'B':
            print(data)
            data_raw_1 = self.ser.read(4) 
            guta_1 = bytearray()

            guta_1.append(data_raw_1[3])				
            guta_1.append(data_raw_1[2])				
            guta_1.append(data_raw_1[1])				
            guta_1.append(data_raw_1[0])

            c,=struct.unpack('!f',guta_1)#ECG
            print(c)
            c_num=float(c)

            print(c_num)

    


if __name__ == '__main__':
    a = QApplication(sys.argv)
    dialog = MyDialog() 
    dialog.show()
    sys.exit(a.exec_())