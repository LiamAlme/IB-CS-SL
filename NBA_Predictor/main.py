#Python3
from tkinter import *    

master = Tk()

#------- function----------------------------------------------------
def calculate_score_team1():
   global v
   raw_data = ((float(three_point_team1.get())/100) * float(three_point_attempt_team1.get())) * 3
   raw_data += (float(fgp_team1.get())/100)*(float(fga_team1.get()))*2
   raw_data += (float(ftp_team1.get())/100)*(float(fta_team1.get()))
   print ('raw_data', raw_data)
   v.set("Score = " + str(int(raw_data)))

#-------------declare lables and entries----------------------------
master.title('NBA Predictor')
Label(master, text="Team 1").grid(row=0)
Label(master, text="Field Goal Attempts").grid(row=1)
Label(master, text="Field Goal %").grid(row=2)
Label(master, text="3 Point Attempts").grid(row=3)
Label(master, text="3 Point %").grid(row=4)
Label(master, text="Free Throw Attempts").grid(row=5)
Label(master, text="Free Throw %").grid(row=6)

v = StringVar()  #this is a variable for the Label that will display the score
v.set("Score =          ")
Label(master, textvariable=v).grid(row=2, column=3)
b = Button(master, text="Calculate Score", command=calculate_score_team1)

#-------------variables for the Entry boxes--------------------
team1 = Entry(master)
fga_team1 = Entry(master)
fgp_team1 = Entry(master)
three_point_team1 = Entry(master)
three_point_attempt_team1 = Entry(master)
atr_team1 = Entry(master)
fta_team1 = Entry(master)
ftp_team1 = Entry(master)
#score_team1 = Entry(master)

#----------layout for the widgets--------------------------
team1.grid(row=0, column=1)
fga_team1.grid(row=1, column=1)
fgp_team1.grid(row=2, column=1)
three_point_attempt_team1.grid(row=3, column=1)
three_point_team1.grid(row=4, column=1)
fta_team1.grid(row=5, column=1)
ftp_team1.grid(row=6, column=1)
#score_team1.grid(row = 3, column = 3)
b.grid(row=7, column =0)

mainloop()

