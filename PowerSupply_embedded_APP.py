#Simple Program to use with an embedded device that use USB HID protocol (visa32)
#Protongamer 2021

#scope = rm.open_resource('USB0::0x1AB1::0x04CE::DS1ZA210801726::INSTR')
#
#scope.write(':CHANnel1:DISPlay ON')

import pyvisa
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont


#Set a fix Identifier (default id : Rigol DP831)
DEVICE_ID = 'USB0::0x1AB1::0x0E11::DP8F233900481::INSTR'

#####################################
##START PHASE
rm = pyvisa.ResourceManager()






#primitives
ON = 1
OFF = 0


channel1 = [OFF]
channel2 = [OFF]
channel3 = [OFF]

Voltage = [0.0,0.0,0.0]
Current = [0.0,0.0,0.0]

StrFV1 = ""
StrFV2 = ""
StrFV3 = ""
StrFA1 = ""
StrFA2 = ""
StrFA3 = ""

window = Tk()

window.title("Remote Power Supply App")

myFont = tkFont.Font(family='Arial', size=16, weight='bold')



window.geometry('1024x200')

try:
	pwsp = rm.open_resource(DEVICE_ID)
except:
	messagebox.showerror("Error", "Failed to connect the device")


pwsp.write('*IDN?')
DEVICE_NAME = pwsp.read()
#print(DEVICE_NAME)



lbl = Label(window, text="Power Supply App", font=myFont)
lb2 = Label(window, text="Channel 1")
lb3 = Label(window, text="Channel 2")
lb4 = Label(window, text="Channel 3")

lb5 = Label(window, text="Set V1 : 0.0V   Set A1 : 0.0A", font=myFont)
lb6 = Label(window, text="Set V2 : 0.0V   Set A2 : 0.0A", font=myFont)
lb7 = Label(window, text="Set V3 : 0.0V   Set A3 : 0.0A", font=myFont)

lb8 = Label(window, text="V1 : 0.0V   A1 : 0.0A", font=myFont)
lb9 = Label(window, text="V2 : 0.0V   A2 : 0.0A", font=myFont)
lb10 = Label(window, text="V3 : 0.0V   A3 : 0.0A", font=myFont)

lb_device = Label(window, text="Device : " + DEVICE_NAME)

lbm_title = Label(window, text="       Measure   ", font=myFont)

lbl.grid(column=0, row=0)
lb2.grid(column=1, row=1)
lb3.grid(column=2, row=1)
lb4.grid(column=3, row=1)
lbm_title.grid(column=4, row=0)

lb5.config(fg= "red")
lb6.config(fg= "red")
lb7.config(fg= "red")
lb5.grid(column=0, row=2)
lb6.grid(column=0, row=3)
lb7.grid(column=0, row=4)

lb8.config(fg= "green")
lb9.config(fg= "green")
lb10.config(fg= "green")
lb8.grid(column=4, row=2, padx = 50)
lb9.grid(column=4, row=3, padx = 50)
lb10.grid(column=4, row=4, padx = 50)
lb_device.grid(column=0, row=6)

def setChannel(channel):

	channel[0] = not(channel[0])
	localStr = ""
#	lbl.configure(text="Button was clicked !!")
	#print("channel " + ("ON" if channel == [True] else "OFF"))
	if(channel is channel1):
		pwsp.write(':INST CH1')
		pwsp.write(':OUTP CH1, ' + ('ON' if channel == [True] else 'OFF'))
		pwsp.write(':OUTP?')
		localStr = pwsp.read()
		#print(localStr == 'ON\n')
		if(localStr == 'ON\n'):
			lb5.config(fg= "green")
		elif(localStr == 'OFF\n'):
			lb5.config(fg= "red")
		btn.configure(text="Channel 1 " + ("ON" if channel == [True] else "OFF"))
	elif(channel is channel2):
		pwsp.write(':INST CH2')
		pwsp.write(':OUTP CH2, ' + ('ON' if channel == [True] else 'OFF'))
		pwsp.write(':OUTP?')
		localStr = pwsp.read()
		if(localStr == 'ON\n'):
			lb6.config(fg= "green")
		elif(localStr == 'OFF\n'):
			lb6.config(fg= "RED")
		btn2.configure(text="Channel 2 " + ("ON" if channel == [True] else "OFF"))
	elif(channel is channel3):
		pwsp.write(':INST CH3')
		pwsp.write(':OUTP CH3, ' + ('ON' if channel == [True] else 'OFF'))
		pwsp.write(':OUTP?')
		localStr = pwsp.read()
		if(localStr == 'ON\n'):
			lb7.config(fg= "green")
		elif(localStr == 'OFF\n'):
			lb7.config(fg= "RED")
		btn3.configure(text="Channel 3 " + ("ON" if channel == [True] else "OFF"))
	#print(localStr)
		

def setPreset():
#	lbl.configure(text="Button was clicked !!")
	#print("V1 : " + FieldV1.get())
	#print("V2 : " + FieldV2.get())
	#print("V3 : " + FieldV3.get())
	#print("A1 : " + FieldA1.get())
	#print("A2 : " + FieldA2.get())
	#print("A3 : " + FieldA3.get())
	
	localStrV = 0
	localStrA = 0
	
	pwsp.write(':INST CH1')
	pwsp.write(':VOLT ' + FieldV1.get())
	pwsp.write(':CURR ' + FieldA1.get())
	pwsp.write(':VOLT?')
	localStrV = float(pwsp.read())
	pwsp.write(':CURR?')
	localStrA = float(pwsp.read())
	lb5.configure(text="Set V1 : "+ str(localStrV) + "V   Set A1 : " + str(localStrA) + "A")
	
	
	pwsp.write(':INST CH2')
	pwsp.write(':VOLT ' + FieldV2.get())
	pwsp.write(':CURR ' + FieldA2.get())
	pwsp.write(':VOLT?')
	localStrV = float(pwsp.read())
	pwsp.write(':CURR?')
	localStrA = float(pwsp.read())
	lb6.configure(text="Set V2 : "+ str(localStrV) + "V   Set A2 : " + str(localStrA) + "A")
	
	pwsp.write(':INST CH3')
	pwsp.write(':VOLT ' + FieldV3.get())
	pwsp.write(':CURR ' + FieldA3.get())
	pwsp.write(':VOLT?')
	localStrV = float(pwsp.read())
	pwsp.write(':CURR?')
	localStrA = float(pwsp.read())
	lb7.configure(text="Set V3 : "+ str(localStrV) + "V   Set A3 : " + str(localStrA) + "A")
	
	
		

def multimeter():
    #Every timeout send reading sequence
	localStrV = 0
	localStrA = 0
	#read voltage on channel 1
	pwsp.write(':MEAS:VOLT? CH1')
	localStrV = float(pwsp.read())
	#read current on channel 1
	pwsp.write(':MEAS:CURR? CH1')
	localStrA = float(pwsp.read())
	#Display channel 1
	lb8.configure(text="V1 : " + str(localStrV) + "V   A1 : " + str(localStrA) + "A")
	
	pwsp.write(':MEAS:VOLT? CH2')
	localStrV = float(pwsp.read())
	pwsp.write(':MEAS:CURR? CH2')
	localStrA = float(pwsp.read())
	lb9.configure(text="V2 : " + str(localStrV) + "V   A2 : " + str(localStrA) + "A")
	
	pwsp.write(':MEAS:VOLT? CH3')
	localStrV = float(pwsp.read())
	pwsp.write(':MEAS:CURR? CH3')
	localStrA = float(pwsp.read())
	lb10.configure(text="V3 : " + str(localStrV) + "V   A3 : " + str(localStrA) + "A")
	
	window.after(500, multimeter)  # reschedule event in 2 seconds







btn = Button(window, text= "Channel 1 OFF", command= lambda : setChannel(channel1))
btn2 = Button(window, text= "Channel 2 OFF", command= lambda : setChannel(channel2))
btn3 = Button(window, text= "Channel 3 OFF", command= lambda : setChannel(channel3))

btn_set = Button(window, text= "Set presets", command=setPreset)

FieldV1 = Entry(window, textvariable= StrFV1, bg ="bisque", fg="maroon", width="10")
FieldV2 = Entry(window, textvariable= StrFV2, bg ="bisque", fg="maroon", width="10")
FieldV3 = Entry(window, textvariable= StrFV3, bg ="bisque", fg="maroon", width="10")
FieldA1 = Entry(window, textvariable= StrFA1, bg ="bisque", fg="maroon", width="10")
FieldA2 = Entry(window, textvariable= StrFA2, bg ="bisque", fg="maroon", width="10")
FieldA3 = Entry(window, textvariable= StrFA3, bg ="bisque", fg="maroon", width="10")

lbvoltage1 = Label(window, text="V")
lbvoltage2 = Label(window, text="V")
lbvoltage3 = Label(window, text="V")
lbcurrent1 = Label(window, text="A")
lbcurrent2 = Label(window, text="A")
lbcurrent3 = Label(window, text="A")




btn.grid(column=1, row=2, padx = 20)
btn2.grid(column=2, row=2, padx = 20)
btn3.grid(column=3, row=2, padx = 20)
btn_set.grid(column=2, row=5, padx = 20)

FieldV1.grid(row=3,column=1, padx = 5, pady = 5)
lbvoltage1.grid(row=3,column=1, sticky=tk.E, padx = 0, pady = 5)
FieldV2.grid(row=3,column=2, padx = 5, pady = 5)
lbvoltage2.grid(row=3,column=2, sticky=tk.E, padx = 0, pady = 5)
FieldV3.grid(row=3,column=3, padx = 5, pady = 5)
lbvoltage3.grid(row=3,column=3, sticky=tk.E, padx = 0, pady = 5)
FieldA1.grid(row=4,column=1, padx = 5, pady = 5)
lbcurrent1.grid(row=4,column=1, sticky=tk.E, padx = 0, pady = 5)
FieldA2.grid(row=4,column=2, padx = 5, pady = 5)
lbcurrent2.grid(row=4,column=2, sticky=tk.E, padx = 0, pady = 5)
FieldA3.grid(row=4,column=3, padx = 5, pady = 5)
lbcurrent3.grid(row=4,column=3, sticky=tk.E, padx = 0, pady = 5)


window.after(500, multimeter)
window.mainloop()