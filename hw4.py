import tkinter

counter = tkinter.Tk()

clicks = 0

def addClick():
  global clicks
  clicks = clicks + 1
  lbl.configure(text=clicks)

lbl = tkinter.Label(counter, text = clicks)
lbl.pack()

btn = tkinter.Button(counter, text="buttton", command=addClick)
btn.pack()

counter.mainloop()