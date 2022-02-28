import tkinter as tk

def exit():
    window.destroy()
 
def convert():
    c = int(e1.get())
    f = ((c*9)/(5))+32
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,f)
    t1.config(state='disabled')

window = tk.Tk()
window.geometry("300x250")
window.config(bg="#A569BD")
window.resizable(width=False,height=False)
window.title('Celsius to Fahrenheit Converter!')
 
l1 = tk.Label(window,text="Celsius to Fahrenheit Converter",font=("Arial", 15),fg="white",bg="black")
l2= tk.Label(window,text="Enter temperature in Celsius: ",font=("Arial", 10,"bold"),fg="white",bg="#A569BD")
l3= tk.Label(window,text="Temperature in Fahrenheit is: ",font=("Arial", 10,"bold"),fg="white",bg="#A569BD")
 
empty_l1 = tk.Label(window,bg="#A569BD")
empty_l2 = tk.Label(window,bg="#A569BD")
 
e1= tk.Entry(window,font=('Arial',10))
 
btn1 = tk.Button(window,text="Convert to Fahrenheit!",font=("Arial", 10),command=convert)
btn2 = tk.Button(window,text="Exit application",font=("Arial", 10),command=exit)
 
t1=tk.Text(window,state="disabled",width=15,height=0)
 
l1.pack()
l2.pack()
e1.pack()
empty_l1.pack()
btn1.pack()
l3.pack()
t1.pack()
empty_l2.pack()
btn2.pack()
 
window.mainloop()