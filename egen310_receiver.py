from tkinter import *
from tkinter import Tk, Canvas
from tkinter import messagebox
import serial
import re
import threading
import time
top = Tk()
top.geometry("800x900")
ser = serial.Serial('COM3',baudrate= 9600,timeout=1)#opens serial communication with the board
#the global variables for all the information being sent in
Xangle=0
Yangle=0
Zangle=0
Xspeed=0
Yspeed=0
Zspeed=0
Currface=""
mxa=0
mya=0
mza=0
mxs=0
mys=0
mzs=0
dist=0
#reads the actual values sent in from the board and sends back each piece
def getValues():

    Fd= ser.readline().decode().split('\r\n')
    return Fd[0]

#formats the data into usable form, and assigns them to variables to be used in the GUI
def manageData(data):
    global Xangle
    global Yangle
    global Zangle
    global Xspeed
    global Yspeed
    global Zspeed
    global Currface
    global mxa
    global mya
    global mza
    global mxs
    global mys
    global mzs
    global dist
    
    inData= re.split(':',data) #uses regular expressions to split the identifier and the actual data into a list
    print(inData)
    lead=inData[0]
    if lead=='X':
        
      Xangle=int(inData[1])
      if abs(Xangle)>abs(mxa):
          mxa=Xangle #checks for max value, and updates if the old value is exceeded
          
          
        
      pass
    elif lead=='Y':
      Yangle=int(inData[1])
      if abs(Yangle)>abs(mya):
          mya=Yangle
          
          
      pass
    elif lead == 'Z':
      Zangle=int(inData[1])
      if abs(Zangle)>abs(mza):
          mza=Zangle
        
      pass
    elif lead == 'S':
      Xspeed=float(inData[1])
      if(Xspeed>0):
          dist = dist+ .5*Xspeed
      if abs(Xspeed)>abs(mxs):
          mxs=abs(Xspeed)
          
        
      pass
    elif lead == 'D':
      Yspeed =float(inData[1])
      if abs(Yspeed)>abs(mys):
          mys=Yspeed
      pass
    elif lead == 'F':
        Zspeed=float(inData[1])
        if abs(Zspeed)>abs(mzs):
          mzs=Zspeed
        
        pass
    elif lead != "":
        Currface = inData
        pass
    else:
        
        pass
def main():

        i=0
        while i<7:
            data = getValues()
            manageData(data)
            i+=1
        config()
        top.after(1000, lambda: main())

def config():
    xax.config(text=str(Xangle))
    yax.config(text=str(Yangle))
    zax.config(text=str(Zangle))
    xsp.config(text=str(Xspeed))
    ysp.config(text=str(Yspeed))
    zsp.config(text=str(Zspeed))
    xma.config(text=str(mxa))
    yma.config(text=str(mya))
    zma.config(text=str(mza))
    xms.config(text=str(mxs))
    distance.config(text=str(dist))
    crf.config(text=Currface)
def write():
    f= open("output.txt","w")
    f.write("X-axis max angle: "+str(mxa)+" max speed: "+ str(mxs)+"\n")
    f.write("Y-axis max angle: "+str(mya)+" max speed: "+ str(mys)+"\n")
    f.write("Z-axis max angle: "+str(mza)+" max speed: "+ str(mzs)+"\n")
    f.write("distance traveled: "+str(dist)+"\n")
    f.close()

titlex = Label(top,text = "X-axis angle")
titlex.pack()
xax = Label(top,fg = "green")
xax.pack()
titley = Label(top,text = "Y-axis angle")
titley.pack()
yax = Label(top,fg = "green")
yax.pack()
titlez = Label(top,text = "Z-axis angle")
titlez.pack()
zax = Label(top,fg = "green")
zax.pack()
titlex1 = Label(top,text = "X-axis speed")
titlex1.pack()
xsp = Label(top,fg = "green")
xsp.pack()
titley1 = Label(top,text = "Y-axis speed")
titley1.pack()
ysp = Label(top,fg = "green")
ysp.pack()
titlez1 = Label(top,text = "Z-axis speed")
titlez1.pack()
zsp = Label(top,fg = "green")
zsp.pack()
crftitle= Label(top, text ="current facing")
crftitle.pack()
crf = Label(top, fg = "green")
crf.pack()
titlex2 = Label(top,text = "X-axis steepest angle")
titlex2.pack()
xma = Label(top,fg = "green")
xma.pack()
titley2 = Label(top,text = "Y-axis steepest angle")
titley2.pack()
yma = Label(top,fg = "green")
yma.pack()
titlez2 = Label(top,text = "Z-axis steepest angle")
titlez2.pack()
zma = Label(top,fg = "green")
zma.pack()
titlex3 = Label(top,text = "X-axis fastest speed")
titlex3.pack()
xms = Label(top,fg = "green")
xms.pack()
distlab = Label(top,text = "distance traveled")
distlab.pack()
distance = Label(top,fg="green")
distance.pack()
start = Button(top, text="gather data", command = main, bg = "green")
start.place(x = 75,y = 500)
write = Button(top, text="write to file", command = write, bg = "green")
write.place(x = 150,y = 500)
top.mainloop
