import tkinter  as tk 
import datetime as dt  
import time  
from playsound import playsound
from PIL import ImageTk, Image

def alarm(setAlarmTimer):  
    while True:  
        time.sleep(1)  
        actualTime = dt.datetime.now()  
        currentTime = actualTime.strftime("%H : %M : %S") 
        if currentTime == setAlarmTimer:
            playsound('alarmsound.mp3')
            break  
  
def getAlarmTime():  
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"  
    alarm(alarmSetTime) 
my_w = tk.Tk()
my_w.configure(bg = "#9A9ACD") 

from time import strftime
def my_time():
    time_string = strftime('%H:%M:%S ') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
	
my_font=("Helevetica", 15, "bold") # display size and style

l1=tk.Label(my_w,font=my_font, bg="#9A9ACD")
l1.grid(row=2,column=2,pady=10)

l2=tk.Label(my_w, text= "Current Time :",font=my_font, bg="#9A9ACD")
l2.grid(row=2,column=1,pady=10)

l3=tk.Label(my_w, text= "Set Time for Alarm :",font=my_font, bg="#9A9ACD")
l3.grid(row=4,column=1,pady=10)

l4=tk.Label(my_w, text= "Hour",font=my_font, bg="#9A9ACD")
l4.grid(row=3,column=2,pady=10)

l5=tk.Label(my_w, text= "Minute",font=my_font, bg="#9A9ACD")
l5.grid(row=3,column=3,pady=10)

l6=tk.Label(my_w, text= " Second",font=my_font, bg="#9A9ACD")
l6.grid(row=3,column=4,pady=10)

l7=tk.Label(my_w, text= "Alarm Clock",font=("Helevetica", 25, "bold"), bg="#9A9ACD")
l7.grid(row=1,column=1,pady=10)

l8=tk.Label(my_w, text= "Remember to set time in 24-hour format",font=("Helevetica", 15, "bold"), bg="#9A9ACD")
l8.grid(row=6,column=2,pady=10,columnspan=3)

image1 = Image.open("Clock.png")
image1 = image1.resize((150, 150))
image1_tk = ImageTk.PhotoImage(image1)
image1_tk = ImageTk.PhotoImage(image1)
l8 = tk.Label(my_w, image=image1_tk,bg = "#9A9ACD")
l8.grid(row=5,column=1 , rowspan=2)

hour = tk.StringVar()  
minute = tk.StringVar()  
second = tk.StringVar()

e1=tk.Entry(my_w, textvariable = hour , width = 10 ,  bg ="#FFFFB6")
e2=tk.Entry(my_w, textvariable = minute , width = 10 ,  bg = "#FFFFB6")
e3=tk.Entry(my_w, textvariable = second , width = 10 ,  bg = "#FFFFB6")
e1.grid(row=4,column=2,pady=10)
e2.grid(row=4,column=3,pady=10)
e3.grid(row=4,column=4,pady=10)

b1=tk.Button(my_w, text = "Set the Alarm" , width= 15,command = getAlarmTime , bg = "#88cffa" , font=15)
b1.grid(row=5,column=2,pady=10,columnspan=3)

my_time()
my_w.mainloop()
