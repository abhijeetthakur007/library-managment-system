import sqlite3
from tkinter import *
from tkinter import messagebox
import datetime
def returns():
    root=Tk()
    root.geometry('500x400')
    root.configure(background='powder blue')
    con=sqlite3.connect('library.db')
    print('Database connected')
    v=''
    l=Label(root,text="RETURN BOOK",fg='black',bg='blue',font=('Arial','50'))
    l1=Label(root,text="Roll no.",fg="black",bg="blue",font=('Arial','20'))
    e1=Entry(root,font=('Arial','20'))
    l.grid(row=0,column=3,padx=200)
    l1.grid(row=1,column=1,padx=20,pady=20)
    e1.grid(row=1,column=3)
    def find():
        root.geometry('500x400')
        root.configure(background='powder blue')
        f=[]
        f=[e1.get()]
        x=con.execute("select *from student where roll=?",f)
        z=x.fetchall()
        if not z:
            messagebox.showinfo("hello",'No books found')
        else:
            global v
            def Cursel(evt):
                global v
                v=l2.get(l2.curselection())
            l2=Listbox(root,font=('Arial','20'))
            l2.grid(row=6,column=3,rowspan=3,padx=20,pady=20)
            for i in z:
                l2.insert(0,i[3])
            l2.bind('<<ListboxSelect>>',Cursel)
            def fine():
                global v
                f.append(v)
                now=datetime.datetime.now()
                k=[]
                k=con.execute("Select *from student where roll=? and book=?",f)
                l=k.fetchall()
                print(l)
                j=l[0][4]
                a1=datetime.datetime.strptime(j,'%m/%d/%y')
                z=now.date()-a1.date()
                y=z.days
                if(y<=7):
                    e=messagebox.askyesno("hello","Fine = 0.0 \nDo you want to proceed to return the book")
                    if e==True:
                        con.execute("delete from student where roll=? and book=?",f)
                        con.commit()
                        b=[v]
                        x=con.execute("select *from entry where name=?",b)
                        z=x.fetchall()
                        b.insert(0,z[0][4]+1)
                        con.execute('update entry set copy=? where name=?',b)
                        con.commit()
                        messagebox.showinfo("hello","Book returned")
                    else:
                        quit()      
                else:
                    k=y-7
                    fi=k*5
                    fi=str(fi)
                    e=messagebox.showinfo("hello","Pay the fine amount ="+fi)
            b2=Button(root,text="Return",bg="blue",fg="black",command=fine,font=('Arial','20'))
            b2.grid(row=2,column=3)
    b1=Button(root,text="Find books",bg="blue",fg="black",command=find,font=('Arial','20'))
    b1.grid(row=3,column=3)
    def home():
        root.destroy()
        import library
        library.lib()
    b5=Button(root,text='Home',bg='blue',command=home,font=('Arial','30'))
    b5.grid(row=9,column=3,rowspan=3,pady=70)
