#timer trial

from Tkinter import*
import time
root=Tk()
w=Label(root,text="hello world")
w.pack()
def callback():
    print "clicked!"
def main():
    x=5
    #x = int(input("Enter number of seconds: "))
    for i in range(x + 1):
        time.sleep(1)
        print(formatTime(x))
        x -= 1
def formatTime(x):
    minutes = int(x / 60)
    seconds_rem = int(x % 60)
    if (seconds_rem < 10):
        return(str(minutes) + ":0" + str(seconds_rem))
    else:
        return(str(minutes) + ":" + str(seconds_rem))
b=Button(root,text="GO", command= main)
b.pack()
root.title("TimeIT")
root.minsize(600, 400)
root.configure(bg="white")
root.mainloop()
