# -*- coding: utf-8 -*-


import tkinter as tk
def creator():
    w=tk.Tk()
    
        
    
    yname=tk.StringVar()
    thname=tk.StringVar()
    def strtfn():
        nm1=yname.get()
        nm2=thname.get()
        print(nm1,nm2)
        exit()
        
        
    def dest():
        name_2.delete(0,"end")
        name_1.delete(0,"end")
        
      
    def valsender():
        return(yname,thname)  
   
        
    w.title("Art")
    w.geometry("400x400")
    w.configure(bg='crimson')
    
    label1=tk.Label(w,text="ENTER THE NAMES")
    label1.grid(row=1,column=1)
    
    name_1=tk.Entry(textvariable=yname , font=("ariel ",10))
    name_1.grid(row=1,column=3,pady=5)
    name_2=tk.Entry(textvariable=thname, font=("ariel",10))
    name_2.grid(row=2,column=3,pady=5)
    
    
    sub_btn=tk.Button(text="Start",command=strtfn,width=20)
    sub_btn.grid(row=4,column=3,pady=15)
    sub_btn.config(bg="crimson")
    
    
    clrbtn=tk.Button(w,text="Clear", command=dest)
    clrbtn.grid(row=3,column=3)
    tk.mainloop()

def emp():
    creator()
    


