from tkinter import *
from tracker import *
window = Tk()
window.title("Process Tracker")
window.geometry("1000x720")

label = Label(window,text="Show all process that are using the CPU").grid()

button = Button(window,text="Get", padx=40,pady=10,command=getListOfProcessSortedByMemory()).grid(row=1,column=0)

# e = Entry(window, width=35, borderwidth=5)
# e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
window.mainloop()