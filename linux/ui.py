from tkinter import *
from tkinter import messagebox
from instagram_modular import execute_GUI
from instagram_modular import handle_files

parent=Tk()
parent.title("Insta Checker")

A=[]
user=StringVar()
password=StringVar()
name=StringVar()
show_pass=IntVar()
radioIF=IntVar()
radioBr=IntVar()

sclist=""

def clear_results():
    message="Results will be shown once \nthe application is executed\n"
    
    f=open("./results/followers_list.txt","w+")
    f.write(message)
    f.close()
    
    f=open("./results/followings_list.txt","w+")
    f.write(message)
    f.close()
    
    f=open("./results/following_not_followerBack_list.txt","w+")
    f.write(message)
    f.close()
    
    f=open("./results/follower_not_followed_list.txt","w+")
    f.write(message)
    f.close()

def fill_followers():
    if sclist.size() != 0:
        sclist.delete(0,sclist.size())
    f=open("./results/followers_list.txt","r")
    fill=f.read()
    f.close()
    fill_list=list(fill.split("\n"))
    for i in fill_list:
        sclist.insert(END, i)

def fill_followings():
    if sclist.size() != 0:
        sclist.delete(0,sclist.size())
    f=open("./results/followings_list.txt","r")
    fill=f.read()
    f.close()
    fill_list=list(fill.split("\n"))
    for i in fill_list:
        sclist.insert(END, i)

def not_Fol_back():
    if sclist.size() != 0:
        sclist.delete(0,sclist.size())
    f=open("./results/following_not_followerBack_list.txt","r")
    fill=f.read()
    f.close()
    fill_list=list(fill.split("\n"))
    for i in fill_list:
        sclist.insert(END, i)

def you_not_fol_back():
    if sclist.size() != 0:
        sclist.delete(0,sclist.size())
    f=open("./results/follower_not_followed_list.txt","r")
    fill=f.read()
    f.close()
    fill_list=list(fill.split("\n"))
    for i in fill_list:
        sclist.insert(END, i)

def get():

    if len(user.get()) == 0:
        messagebox.showerror("error","feilds are empty")
        return
    if len(password.get()) == 0:
        messagebox.showerror("error","feilds are empty")
        return
    if(len(name.get()) == 0):
        messagebox.showerror("error","feilds are empty")
        return
    if radioIF.get()==0:
        messagebox.showerror("error","feilds are empty")
        return
    if radioBr.get()==0:
        messagebox.showerror("error","feilds are empty")
        return
                    
    A.append(user.get())
    A.append(password.get())        
    A.append(name.get())
    A.append(radioIF.get())
    A.append(radioBr.get())
    if messagebox.askokcancel("confirm","are the values provided by you correct?"):
        messagebox.showinfo("yeah","this may take a while!! please dont touch anything!!") 
        try:
            execute_GUI(A)
            messagebox.showinfo("Done!","You can now see the results") 
        except:
            handle_files()
            messagebox.showerror("error","unexpected error please restart process")
        handle_files()
        
def sh_pas():
    if show_pass.get() == 1:
        Entry(parent,textvariable = password).place(x=140,y=60)
    else:
        Entry(parent,textvariable = password,show="*").place(x=140,y=60)

def form():  
    global sclist
    parent.geometry("560x650")
    parent.resizable(0,0)

    sb=Scrollbar(parent,orient=VERTICAL)
    sb.place(x=533,y=28,height=600)
    
    clear_results()
    
    sclist=Listbox(parent,yscrollcommand=sb.set)
    sclist.place(x=310,y=28,height=600,width=220)

    Label(parent,text="Username:",font=("Arial Bold",11)).place(x=30,y=29)
    Entry(parent,textvariable = user).place(x=140,y=30)
    
    Label(parent,text="Password:",font=("Arial Bold",11)).place(x=30,y=58)
    Entry(parent,textvariable = password,show="*").place(x=140,y=60)

    Label(parent,text="User To Search:",font=("Arial Bold",11)).place(x=15,y=88)
    Entry(parent,textvariable = name).place(x=140,y=90)

    Label(parent,text="Login Using:",font=("Arial Bold",11)).place(x=100,y=135)
    Radiobutton(parent,text="Instagram",font=("Arial",10),variable=radioIF,value=1).place(x=20,y=160)
    Radiobutton(parent,text="Facebook",font=("Arial",10),variable=radioIF,value=2).place(x=190,y=160)

    Label(parent,text="Preferred Browser:",font=("Arial Bold",11)).place(x=80,y=210)
    Radiobutton(parent,text="Firefox",font=("Arial",10),variable=radioBr,value=1).place(x=20,y=235)
    Radiobutton(parent,text="Chrome",font=("Arial",10),variable=radioBr,value=2).place(x=190,y=235)

    Checkbutton(parent,text="show password",variable=show_pass,onvalue=1,offvalue=0,command=sh_pas).place(x=90,y=270)
    Button(parent,text="submit" ,font=("Arial Bold",11),command=get).place(x=120,y=305)
    

    Label(parent,text="Show Results For",font=("Arial Bold",13)).place(x=80,y=372)
    
    Button(parent,text="Followers" ,font=("Arial Bold",11),command=fill_followers).place(x=30,y=400,height=50,width=250)
    Button(parent,text="Followings" ,font=("Arial Bold",11),command=fill_followings).place(x=30,y=450,height=50,width=250)
    Button(parent,text="did not followed back" ,font=("Arial Bold",11),command=not_Fol_back).place(x=30,y=500,height=50,width=250)
    Button(parent,text="you did not follow back" ,font=("Arial Bold",11),command=you_not_fol_back).place(x=30,y=550,height=50,width=250)
  
    parent.mainloop()

form()
