from tkinter import *
from datetime import datetime
import sys
import pyautogui 
from threading import Timer
import time 

clickedkey=0
resettoken=0
hourin=0
minin=0
clickin=0
delayin=0
invalidinput=0


window = Tk()
window.title("wannaclicksomewhere")
window.geometry('1000x300+700+400')
background = 'gray0'
textcolor = 'snow'
window.config(bg= background )




lbl = Label(window,width=15,bg=background,fg = textcolor ,text="Enter the time")
lbl.grid(column=0, row=0)
lbl = Label(window,bg=background,fg = textcolor ,text="at which")
lbl.grid(column=0, row=1)
lbl = Label(window,bg=background,fg = textcolor ,text="u want your")
lbl.grid(column=0, row=2)
lbl = Label(window,bg=background,fg = textcolor ,text="mouse button")
lbl.grid(column=0, row=3)
lbl = Label(window,bg=background,fg = textcolor ,text="to be clicked")
lbl.grid(column=0, row=4)


txt = Entry(window , bg = 'darkgreen' ,fg = textcolor ,width=10)
txt.grid(column=1, row=0 , sticky = 's' )

txt1 = Entry(window, bg = 'darkgreen' ,fg = textcolor , width=10)
txt1.grid(column=2, row=0 , sticky = 's')

txt2 = Entry(window, bg = 'darkgreen' ,fg = textcolor , width=10)
txt2.grid(column=3, row=0 , sticky = 's')

txt3 = Entry(window, bg = 'darkgreen' ,fg = textcolor , width=10)
txt3.grid(column=3, row=2 , sticky = 's')



txt.insert(0,datetime.now().strftime("%H"))
txt1.insert(0,"0")
txt2.insert(0, "1")
txt3.insert(0, "0")

def clicked():
    global clickedkey
    clickedkey = 1
    global resettoken
    resettoken = 0
    

      
 
    
    inputgateway()
    
    
def mouseclicker():
    
    global hourin
    global minin
    global clickin
    global delayin    
    

    x=datetime.today()

    y=x.replace(day=x.day, hour=hourin, minute=minin, second=0, microsecond=0)

    delta_t=y-x
    secs=delta_t.seconds+1
    def escapu():
        if resettoken==0:
            for i in range(0,clickin):
                
                pyautogui.click()
                time.sleep(delayin)
                
        else:
            pass

    t = Timer(secs, escapu)
    t.setDaemon(True)
    t.start()





    
def reset():
    
    global resettoken
    resettoken=1
    
    global clickedkey
    clickedkey=0

    txt.config(state='normal')
    txt1.config(state='normal')
    txt2.config(state='normal')
    txt3.config(state='normal')
    
    txt.delete(0, END)   
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    
    txt.insert(0,datetime.now().strftime("%H"))
    txt1.insert(0,"0")
    txt2.insert(0, "1")
    txt3.insert(0, "0")
    
    
    
btn = Button(window ,bg='gray94' , text="start timer", command=clicked)
btn.grid(column=3, row=5 , sticky='n',ipadx=10)

btn = Button(window ,bg='gray94' , text="reset timer", command=reset)
btn.grid(column=3, row=6 , sticky='s',ipadx=10)


lbl = Label(window,bg=background, fg = textcolor ,text="Hours")
lbl.grid(column=1, row=1)
lbl = Label(window,bg=background,fg = textcolor , text="Minutes")
lbl.grid(column=2, row=1)
lbl = Label(window,bg=background,fg = textcolor , text="clicks")
lbl.grid(column=3, row=1)
lbl = Label(window,bg=background,fg = textcolor , text="timegap between clicks ")
lbl.grid(column=3, row=3)


lbl = Label(window,bg=background, fg = textcolor ,text="    ")
lbl.grid(column=1, row=2)
lbl = Label(window, bg=background,fg = textcolor , text="    ")
lbl.grid(column=2, row=2)

def quit():
    
    global stoploop
    stoploop=1
    window.destroy()
    

    
    
btn = Button(window , bg = 'gray94' , width=60 , text="Quit this application", command=quit)  
btn.grid(column=1, row=6 , columnspan=2 , sticky='w')

lbl = Label(window,bg=background, fg = textcolor ,text="Current time is :")
lbl.grid(column=1, row=3 )

lbl = Label(window,bg=background,font='bold', fg = 'red' ,text="TIME FOR IMPACT :")
lbl.grid(column=1, row=4 )

lbl = Label(window,bg=background,font='bold', fg = 'red' ,text="            ")
lbl.grid(column=1, row=5 )

window.resizable(False, False)  

def update_clock():
    
    hrs2 = int(datetime.now().strftime("%H"))
    ms2 = int(datetime.now().strftime("%M"))
    ss2 = int(datetime.now().strftime("%S"))
    dimee=str(hrs2)+" Hours:"+str(ms2)+" Minutes:"+str(ss2)+" Seconds"   
    lbl = Label(window,bg=background, width=40,fg = textcolor , text=dimee)
    lbl.grid(column=2, row=3)
    window.after(1000, update_clock)

def countdown_timer():
    
    global hourin
    global minin
 
    
    if clickedkey==1 :        

        hrs1 =int(datetime.now().strftime("%H"))
        ms1 = int(datetime.now().strftime("%M"))
        ss1 = int(datetime.now().strftime("%S"))
        hh=hourin-hrs1
        hh=hh*60
        mm=minin-ms1-1
        left=hh+mm
        
        if left>=60:
            h=left//60
            m=left%60
            s=59-ss1
        else:
            h=0
            m=left
            s=s=59-ss1
        
        if left<0:
            h=0
            m=0
            s=0
            
        dime=str(h)+" Hours:"+str(m)+" Minutes:"+str(s)+" Seconds"
        lbl = Label(window,font='bold', width=40 ,bg=background,fg = 'red' , text=dime )
        lbl.grid(column=2, row=4 )         
    else:

        h="0"
        m="0"
        s="0"
        
        dime=str(h)+" Hours:"+str(m)+" Minutes:"+str(s)+" Seconds"
        lbl = Label(window,font='bold', width=40 ,bg=background,fg = 'red' , text=dime )
        lbl.grid(column=2, row=4)         
        
        
    window.after(1000, countdown_timer)

def inputgateway():
    
    global hourin
    global minin
    global clickin
    global delayin
    global invalidinput
    global errormessage
    
    hh=txt.get()
    mm=txt1.get()
    cc=txt2.get()
    dd=txt3.get()
    
    try:
        
        if int(hh)>= int(datetime.now().strftime("%H")):
            
            hourin=int(hh)
        
        else:
            invalidinput=1 
            hourin=0
            txt.delete(0, END)
            txt.insert(0,datetime.now().strftime("%H"))
            
    except:
        
        invalidinput=1
        hourin=0
        txt.delete(0, END)
        txt.insert(0,datetime.now().strftime("%H"))
        
                    
            
    try:
        
        
        if (int(hh) == int(datetime.now().strftime("%H"))) and ( int(mm) > int(datetime.now().strftime("%M"))) :
            
            minin=int(mm)
            
        elif int(hh)> int(datetime.now().strftime("%H")) :
            
            minin=int(mm)
           
        else:
            invalidinput=1 
            minin=0
            txt1.delete(0, END)
            txt1.insert(0,"0")
    
    except:
        
        invalidinput=1        
        minin=0
        txt1.delete(0, END)
        txt1.insert(0,"0")
        
        
    try: 
        
        clickin=int(cc)
        
    except: 
        
        invalidinput=1        
        clickin=1
        txt2.delete(0, END)
        txt2.insert(0,"1")
        
    try:
        
        delayin=int(dd)
        
    except: 
        
        invalidinput=1        
        delayin=0
        txt3.delete(0, END)
        txt3.insert(0,"0") 
        

    
    if invalidinput==0:
        
  
        errormessage="                calm                 "
        
        
        txt.config(state='disabled')
        txt1.config(state='disabled')
        txt2.config(state='disabled')
        txt3.config(state='disabled') 
        
    elif invalidinput==1:
        
 
        errormessage="wrong input sweets "
       
        invalidinput=0
        txt.config(state='normal')
        txt1.config(state='normal')
        txt2.config(state='normal')
        txt3.config(state='normal')        
    
    errorlabel = Label(window,bg=background,font='magenta', fg = 'red' ,text=errormessage)
    errorlabel.grid(column=2, row=7 )     

    mouseclicker()

    

    

countdown_timer()
update_clock()    

    
window.mainloop()
