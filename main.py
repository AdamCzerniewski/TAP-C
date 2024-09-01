#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:44:45 2024

@author: coco
"""
import os
import math
from ui import Ui_MainWindow
import pyqtgraph as pg
from PyQt5.QtGui import QColor
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets  as qtw
from PyQt5.QtWidgets import QMessageBox
#from LoginEntry import LoginEntry
#from LoginWindow import LoginWindow
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
QLineEdit, QInputDialog)


class Main(qtw.QMainWindow):
    
    def __init__(self):
        super(Main,self).__init__()
        self.port="none"
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)    
        print ("show GUI")
        
        print("tapc1")
        self.text = ""
        self.H = 0
        self.C1 = 0
        self.C2 = 0
        self.L = 0
        self.X = 0
        #self.ui.graphicsView.setBackground('light grey') 
        self.curve_color = QColor('yellow')  # Orange
                        
        self.ui.btn_enterParams.clicked.connect(self.fn100)    
        self.ui.btn_enterSweep.clicked.connect(self.fn920)    

        
    def fn100(self):
        print("fn100 RUNNING")
        
        # TAPC1 100
        # 120 CLS
        print("     RESISTANCE MATCHING - TAPPED CAPACITOR") # 140
        print("") #160
        
        
        print("          PASSBAND CENTER FRQ (MHz) = ")
        F = self.ui.tf_passbandCenterFrq.text();self.F = float(F)
        
        print("") #200
        W = self.F * float(6280000) #220
        
        print("          INSERTION LOSS = ")
        IL = self.ui.tf_insertionLoss.text();self.IL = int(IL) #240
        if self.IL == 0:         self.IL = .00001 #260
        print("") #280
        self.IL = 10 ** (-self.IL/10) #300

        print("          R1 in ohm = ")        
        RS = self.ui.tf_r1Ohms.text() ;self.RS = int(RS) #320
        labelRS = RS + "Ω"
        #self.ui.label_r1Ohms.setText(labelRS)
        self.ui.label_r1Ohms.setText(f"<html><head/><body><p><span style=\" font-weight:600; color:#3d8886;\">{labelRS}</span></p></body></html>") # color:#267a7a or color:#3d8886
        print("          Rt in ohm = ")   
        RL = self.ui.tf_rtOhms.text();self.RL = int(RL) #340
        labelRL = RL + "Ω"
        #self.ui.label_rtOhms.setText(labelRL)
        self.ui.label_rtOhms.setText(f"<html><head/><body><p><span style=\" font-weight:600; color:#3d8886;\">{labelRL}</span></p></body></html>")        
        
        if self.RS<self.RL:         K = (self.RL/self.RS)**0.5;        K -= 1 #360
        if self.RS>self.RL:        K = (self.RS/self.RL)**0.5;        K -= 1 #380
        if self.RS<self.RL:        X = 2*self.RL;        X *= (-1+1/self.IL)**0.5 #400
        if self.RS>self.RL:        X = 2*self.RS;        X *= (-1+1/self.IL)**0.5 #420
        
        print("X=",X)
        print("W=",W)
        print("K=",K)
        
        self.L = X/(W*K) #440
        
        self.C2 = (1+K)*K*K*self.L/(X**2) #460
        self.C1 = self.C2/K   #480
        print("") #500
        print("HEREHEREHEREHERE", self.C1*10**13)
        print("          C1=" , int(self.C1*10**13)/10 , "pF") #520
        c1pF = int(self.C1*10**13)/10
        c1pF = str(c1pF)
        labelc1pF = c1pF + "pF"
        #self.ui.label_c1pF.setText(labelc1pF)
        self.ui.label_c1pF.setText(f"<html><head/><body><p><span style=\" font-weight:600; color:#3d8886;\">{labelc1pF}</span></p></body></html>")

        
        print("") #540
        print("          C2=" , int(self.C2*10**13)/10 , "pF") #560
        c2pF = int(self.C2*10**13)/10
        c2pF = str(c2pF)
        labelc2pF = c2pF + "pF"
        #self.ui.label_c2pF.setText(labelc2pF)
        self.ui.label_c2pF.setText(f"<html><head/><body><p><span style=\" font-weight:600; color:#3d8886;\">{labelc2pF}</span></p></body></html>")
        
        
        print("") #580
        print("           L=" , int(self.L*10**9)/1000 , "uH") #600
        
        L = int(self.L*10**9)/1000
        L = str(L)
        label_L = L + "uH"
        #self.ui.label_L.setText(label_L)
        self.ui.label_L.setText(f"<html><head/><body><p><span style=\" font-weight:600; color:#3d8886;\">{label_L}</span></p></body></html>")
        
        
        
        print() #620
        print() #640 
        if self.RS<self.RL:        B = "C2" # B$ var B is a string #650
        if self.RS<self.RL:        C="L" # C$ var C is a string #680
        if self.RS>self.RL:        B="L" # B$ var B is a string #700
        if self.RS>self.RL:        C="C2" # C$ var C is a string #720
        print("            -----o----o--- C1 ---o-----") #740
        print("           |          |          |     |") #760
        print("           |          |          |     |") #780
        print("           R1         "+B+"          "+C+"    Rt") #800
        print("           |          |          |     |") #820
        print("           |          |          |     |") #840
        print("            -----o----o----------o-----") #860
        print() #880
        # = input("          press RETURN for next") #900
        print("          press RETURN for next") #900
        #self.fn920() #TO PASS ONTO THE NEXT FUNCTION
        
    def fn920(self):   
        print("fn920 RUNNING")
        #os.system("clear") #920
        #self.F1, self.F2, self.FS = input("Enter Fmin, Fmax, step (MHz): ").split(",") #940
        self.F1 = self.ui.tf_minFreq.text(); self.F2 = self.ui.tf_maxFreq.text(); self.FS = self.ui.tf_stepFreq.text()
        self.F1=str(self.F1); self.F2=str(self.F2); self.FS =str(self.FS)
        print(self.F1)
        print(self.F2)
        print(self.FS)
        self.F1 = float(self.F1);self.F2 = float(self.F2);self.FS = float(self.FS)
        print("");print("");print("") #960
        self.fn1200() #980
        
    def fn1200(self):
        print("fn1200 RUNNING")
        s1="  F"+"               Zin"+"                                   IL" 
        s2=" MHz"+"               ohm"+"                                   dB" 
        print( s1 ) #1200
        print( s2 ) #1220
        print #1240
        self.W1 = self.F1*6280000; self.W2 = self.F2*6280000; self.WS = self.FS*6280000 #1260
        #print(self.W1, self.W2, self.WS)
        
        if self.RS>self.RL: 
            self.fn1600()
        
        else:
            self.fn1300()
            
    # RS<RL    
    def fn1300(self):
        
        print("FN1300 RUNNING")
        
        W = self.W1 # CANT BE PLACED INTO THE FOR LOOP
        
        self.freq_xAxis = []
        self.IL_yAxis = []
        
        self.ui.te_chart.clear()
        
        while W<=self.W2:
            
            XL=W*self.L #1320
            D1=XL*XL+self.RL*self.RL #1340
            R1=XL*XL*self.RL/D1 #1360
            X1=XL*self.RL*self.RL/D1 #1380
            X2=-1/(W*self.C1)+X1 #1400
            XC=-1/(W*self.C2) #1420
            D2=R1*R1+(X2+XC)**2 #1440
            D2=D2*(self.RL*self.RL+XL*XL)**2 #1460
            R2=-self.RL*XL*XL*XC*XC*(XL*XL+self.RL*self.RL) #1480
            D2=-D2 #1500
            R2=R2/D2 #1520
            X3=-XC*(self.RL**2*(self.RL**2*X2*(XC+X2)+XL**2*(2*X2*(XC+X2)+XL**2))+XL**4*X2*(XC+X2)) #1540
            X3=X3/D2 #1560
            N1=4*self.RS*R2 #1760
            D3=(self.RS+R2)**2+X3**2 #1780 
            IL1=10*math.log(N1/D3)/math.log(10) #1800
            if X3<0 : B="-j" # B$ var B is a string #1820
            if X3>=0 : B="+j" # B$ var B is a string #1840
            X3=abs(int(100*X3)/100) #1860
            R2=int(100*R2)/100 #1880
            IL1=int(100*IL1)/100 #1900
            IL2=74+IL1 #1920
            
            print(W/6280000,R2,B,X3,IL1)
            
            chartText = self.ui.te_chart.toPlainText()
            
            val = f"{W/6280000:.2f}          {R2:.2f} {B} {X3:.2f} {IL1:.2f}"
            chartText += f"{val}\n"
            
            self.ui.te_chart.setText(chartText)
            

            W=W+self.WS
        
        self.plotValues()
    
    
    # RS>RL        
    def fn1600(self):
        print("fn1600 RUNNING")
        #REM RS>RL #1600
        W = self.F * float(6280000)

        W = self.W1 # CANT BE PLACED INTO THE FOR LOOP

        self.freq_xAxis = []
        self.IL_yAxis = []
        
        self.ui.te_chart.clear()

        
        while W<=self.W2:        
        
            self.D1=1+(W*self.C2*self.RL)**2 #1620 
            self.XO=-1/(W*self.C1) #1640
            self.R1=self.RL/self.D1;    X1=-W*self.C2*self.RL*self.RL/self.D1 #1660
            self.X2=self.XO+X1 #1680
            self.D2=self.R1*self.R1+(self.X2+W*self.L)**2 #1700
            self.R2=self.R1*(W*self.L)**2/self.D2 #1720
            self.X3=W*self.L*(self.R1*self.R1+self.X2*self.X2+W*self.L*self.X2)/self.D2 #1740
            N1=4*self.RS*self.R2 #1760
            D3=(self.RS+self.R2)**2+self.X3**2 #1780 
            IL1=10*math.log(N1/D3)/math.log(10) #1800
            if self.X3<0 : B="- j" # B$ var B is a string #1820
            if self.X3>=0 : B="+ j" # B$ var B is a string #1840
            X3=abs(int(100*self.X3)/100) #1860
            R2=int(100*self.R2)/100 #1880
            IL1=int(100*IL1)/100 #1900
            IL2=74+IL1 #1920
            
            print(W/6280000,R2,B,X3,IL1)
            
            self.freq_xAxis.append(W/6280000)
            self.IL_yAxis.append(IL1)
                                   
            chartText = self.ui.te_chart.toPlainText()
            
            val = f"{W/6280000:.2f} \t             {R2:.2f} {B} {X3:.2f} \t             {IL1:.2f}"
            chartText += f"{val}\n"
            
            self.ui.te_chart.setText(chartText)
            

            W=W+self.WS
        
        self.plotValues()

    def plotValues(self):
        
        self.ui.graphicsView.clear()
        self.ui.graphicsView.showGrid(x=True, y=True)
        self.ui.graphicsView.setLabel('left', 'IL [dB]')
        self.ui.graphicsView.setLabel('bottom', 'Freq [MHz]')
        
        penCustomized = pg.mkPen(color=self.curve_color, width=2)
        
        self.graph = self.ui.graphicsView.plot(self.freq_xAxis, self.IL_yAxis, pen=penCustomized)  # Store the new tangent line
        
        # Plot the points as small circles with the same color as the line
        dot_pen = pg.mkPen('y')           # Match the line color
        dot_brush = pg.mkBrush('y')       # Fill color, match the line
        dot_size = 10                     # Size of the dots
        
        # Create dots at peaks
        # for px, py in zip(peaks_x, peaks_y):
        #     plot.plot(px, py, pen=dot_pen, symbol='o', symbolSize=dot_size, symbolBrush=dot_brush)        
        
        user_center_freq = float(self.ui.tf_passbandCenterFrq.text())
        
        # Finding the closest frequency index
        closest_index = 0
        closest_distance = float('inf')  # Start with a very large number
        
        for i in range(len(self.freq_xAxis)):
            distance = abs(self.freq_xAxis[i] - user_center_freq)
            if distance < closest_distance:
                closest_distance = distance
                closest_index = i
        
        # Validating the index before accessing
        if closest_index < len(self.freq_xAxis) and closest_index < len(self.IL_yAxis):
            centerFreq_x = self.freq_xAxis[closest_index]
            centerFreq_y = self.IL_yAxis[closest_index]        
         
        self.centerFreqPoint = self.ui.graphicsView.plot([centerFreq_x], [centerFreq_y], pen=dot_pen, symbol='o', symbolSize=dot_size, symbolBrush=dot_brush)
        
        # Create a text label for the dot
        label_text = "center frequency"
        label = pg.TextItem(label_text, anchor=(0, 0), color='y')  # Anchor to the left and bottom
        label.setPos(centerFreq_x+1, centerFreq_y-0.3)  # Position it at the dot's coordinates
        self.ui.graphicsView.addItem(label)   # Add the label to the plot                        


if __name__=='__main__':
    
    app=qtw.QApplication([])
    
    widget=Main()
    widget.show()
    

    
    app.exec_()

