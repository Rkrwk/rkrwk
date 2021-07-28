from tkinter import *
import datetime
import time
from tkinter import messagebox
from threading import *
from time import strftime

root = Tk()
root.title("timetable")

les = Label(root, text="                         Recess", pady=10)
lun = Label(root, text="                         Lunch", pady=20)

def timed():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, timed)

lbl = Label(root, )

def Threading():
    t1 = Thread(target=alarm)
    t2 = Thread(target=timetable)
    t1.start()
    t2.start()



def alarm():
    print("started")
    set_alarm_time2 = f"{9}:{15}:{0}"
    set_alarm_time3 = f"{10}:{5}:{0}"
    set_alarm_time4 = f"{10}:{55}:{0}"
    set_alarm_time5 = f"{11}:{15}:{0}"
    set_alarm_time6 = f"{12}:{5}:{0}"
    set_alarm_time7 = f"{12}:{55}:{0}"
    set_alarm_time8 = f"{13}:{35}:{0}"
    set_alarm_time9 = f"{14}:{25}:{0}"
    set_alarm_time10 = f"{15}:{15}:{0}"
    while True:
        # Set Alarm
        set_alarm_time = f"{hour}:{minute}:{second}"

        # Wait for one seconds
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")



        print(current_time)
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            period = "Period 0"
            print(period)
            messagebox.showinfo("This is time to study", "It is " + period)
        elif current_time == set_alarm_time2:
            period = "Period 1"
            print("My time has come")
            messagebox.showinfo("This is time to study", "It is "+ period)
        elif current_time == set_alarm_time3:
            print("My time has come")
            period = "Period 2"
            messagebox.showinfo("This is time to study", "It is " + period)
        elif current_time == set_alarm_time4:
            print("My time has come")
            period = "recess"
            messagebox.showinfo("This is time to study", "It is " + period)
        elif current_time == set_alarm_time5:
            print("My time has come")
            period = "Period 3"
            messagebox.showinfo("This is time to study", "It is " + period)
        elif current_time == set_alarm_time6:
            print("My time has come")
            period = "Period 4"
            messagebox.showinfo("This is time to study", "It is " + period)
        elif current_time == set_alarm_time7:
            print("My time has come")
            period = "Lunch"
            messagebox.showinfo("This is time to study", "It is " + period)
        elif current_time == set_alarm_time8:
            print("My name has come")
            period = "Period 5"
            messagebox.showinfo("This is time to study", "It is " + period)
        elif current_time == set_alarm_time9:
            print("My name has come")
            period = "Period 6"
            messagebox.showinfo("This is time to study", "It is " + period)
        elif current_time == set_alarm_time10:
            print("My name has come")
            period = "end of the day"
            messagebox.showinfo("This is time to study", "It is " + period)







# Add Labels, Frame, Button, Optionmenus
lb1 = Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red")
lb1.pack(pady=10)
lb2 = Label(root, text="Set Time", font=("Helvetica 15 bold"))
lb2.pack()



hour = '21'
minute = '15'
second = '00'



alb = Button(root, text="Set Alarm", font=("Helvetica 15"), command=lambda: [Threading(), alb.pack_forget(), lb1.pack_forget(), lb2.pack_forget(),],  )
alb.pack(pady=20,)


options = [
    "----",
    "Maths",
    "English",
    "Chemistry",
    "Biology",
    "Physics",
    "SDD",
    "Economic",
    "Hospitality",
    "Visual Art",
    "Legal Studies",
    "Engineering"
]


period0 = Label(root, text="0", padx=40)
period1 = Label(root, text="1", padx=40)
period2 = Label(root, text="2", padx=40)
period3 = Label(root, text="3",  padx=40)
period4 = Label(root, text="4", padx=40)
period5 = Label(root, text="5", padx=40)
period6 = Label(root, text="6", padx=40)

mon = Label(root, text="Monday", pady=10, padx=10)
tue = Label(root, text="Tuesday", pady=10, padx=10)
wed = Label(root, text="Wednesday", pady=10, padx=10)
thu = Label(root, text="Thursday", pady=10, padx=10)
fri = Label(root, text="Friday", pady=10, padx=10)


clicked11 = StringVar()
clicked12 = StringVar()
clicked13 = StringVar()
clicked14 = StringVar()
clicked15 = StringVar()
clicked16 = StringVar()
clicked17 = StringVar()
clicked11.set(options[0])
clicked12.set(options[0])
clicked13.set(options[0])
clicked14.set(options[0])
clicked15.set(options[0])
clicked16.set(options[0])
clicked17.set(options[0])

clicked112 = StringVar()
clicked122 = StringVar()
clicked132 = StringVar()
clicked142 = StringVar()
clicked152 = StringVar()
clicked162 = StringVar()
clicked172 = StringVar()
clicked112.set(options[0])
clicked122.set(options[0])
clicked132.set(options[0])
clicked142.set(options[0])
clicked152.set(options[0])
clicked162.set(options[0])
clicked172.set(options[0])

clicked113 = StringVar()
clicked123 = StringVar()
clicked133 = StringVar()
clicked143 = StringVar()
clicked153 = StringVar()
clicked163 = StringVar()
clicked173 = StringVar()
clicked113.set(options[0])
clicked123.set(options[0])
clicked133.set(options[0])
clicked143.set(options[0])
clicked153.set(options[0])
clicked163.set(options[0])
clicked173.set(options[0])

clicked114 = StringVar()
clicked124 = StringVar()
clicked134 = StringVar()
clicked144 = StringVar()
clicked154 = StringVar()
clicked164 = StringVar()
clicked174 = StringVar()
clicked114.set(options[0])
clicked124.set(options[0])
clicked134.set(options[0])
clicked144.set(options[0])
clicked154.set(options[0])
clicked164.set(options[0])
clicked174.set(options[0])

clicked115 = StringVar()
clicked125 = StringVar()
clicked135 = StringVar()
clicked145 = StringVar()
clicked155 = StringVar()
clicked165 = StringVar()
clicked175 = StringVar()
clicked115.set(options[0])
clicked125.set(options[0])
clicked135.set(options[0])
clicked145.set(options[0])
clicked155.set(options[0])
clicked165.set(options[0])
clicked175.set(options[0])


ff1 = OptionMenu(root, clicked11, *options)
ff2 = OptionMenu(root, clicked12, *options)
ff3 = OptionMenu(root, clicked13, *options)
ff4 = OptionMenu(root, clicked14, *options)
ff5 = OptionMenu(root, clicked15, *options)
ff6 = OptionMenu(root, clicked16, *options)
ff7 = OptionMenu(root, clicked17, *options)

qff1 = OptionMenu(root, clicked112, *options)
qff2 = OptionMenu(root, clicked122, *options)
qff3 = OptionMenu(root, clicked132, *options)
qff4 = OptionMenu(root, clicked142, *options)
qff5 = OptionMenu(root, clicked152, *options)
qff6 = OptionMenu(root, clicked162, *options)
qff7 = OptionMenu(root, clicked172, *options)

ff13 = OptionMenu(root, clicked113, *options)
ff23 = OptionMenu(root, clicked123, *options)
ff33 = OptionMenu(root, clicked133, *options)
ff43 = OptionMenu(root, clicked143, *options)
ff53 = OptionMenu(root, clicked153, *options)
ff63 = OptionMenu(root, clicked163, *options)
ff73 = OptionMenu(root, clicked173, *options)

ff14 = OptionMenu(root, clicked114, *options)
ff24 = OptionMenu(root, clicked124, *options)
ff34 = OptionMenu(root, clicked134, *options)
ff44 = OptionMenu(root, clicked144, *options)
ff54 = OptionMenu(root, clicked154, *options)
ff64 = OptionMenu(root, clicked164, *options)
ff74 = OptionMenu(root, clicked174, *options)

ff15 = OptionMenu(root, clicked115, *options)
ff25 = OptionMenu(root, clicked125, *options)
ff35 = OptionMenu(root, clicked135, *options)
ff45 = OptionMenu(root, clicked145, *options)
ff55 = OptionMenu(root, clicked155, *options)
ff65 = OptionMenu(root, clicked165, *options)
ff75 = OptionMenu(root, clicked175, *options)



def timetable():
  mon.grid(row=0, column=1)
  tue.grid(row=0, column=2)
  wed.grid(row=0, column=3)
  thu.grid(row=0, column=4)
  fri.grid(row=0, column=5)

  period0.grid(row=1, column=0)
  period1.grid(row=2, column=0)
  period2.grid(row=3, column=0)
  period3.grid(row=5, column=0)
  period4.grid(row=6, column=0)
  period5.grid(row=8, column=0)
  period6.grid(row=9, column=0)

  ff1.grid(row=1, column=1, )
  ff2.grid(row=2, column=1, )
  ff3.grid(row=3, column=1, )
  ff4.grid(row=5, column=1, )
  ff5.grid(row=6, column=1, )
  ff6.grid(row=8, column=1, )
  ff7.grid(row=9, column=1, )

  qff1.grid(row=1, column=2, )
  qff2.grid(row=2, column=2, )
  qff3.grid(row=3, column=2, )
  qff4.grid(row=5, column=2, )
  qff5.grid(row=6, column=2, )
  qff6.grid(row=8, column=2, )
  qff7.grid(row=9, column=2, )

  ff13.grid(row=1, column=3, )
  ff23.grid(row=2, column=3, )
  ff33.grid(row=3, column=3, )
  ff43.grid(row=5, column=3, )
  ff53.grid(row=6, column=3, )
  ff63.grid(row=8, column=3, )
  ff73.grid(row=9, column=3, )

  ff14.grid(row=1, column=4, )
  ff24.grid(row=2, column=4, )
  ff34.grid(row=3, column=4, )
  ff44.grid(row=5, column=4, )
  ff54.grid(row=6, column=4, )
  ff64.grid(row=8, column=4, )
  ff74.grid(row=9, column=4, )

  ff15.grid(row=1, column=5, )
  ff25.grid(row=2, column=5, )
  ff35.grid(row=3, column=5, )
  ff45.grid(row=5, column=5, )
  ff55.grid(row=6, column=5, )
  ff65.grid(row=8, column=5, )
  ff75.grid(row=9, column=5, )
  les.grid(row=4, column=0, columnspan=7)    
  lun.grid(row=7, column=0, columnspan=7)

  timed()
  lbl.grid(row=10, column=3)




root.minsize(530, 375)

root.mainloop()

