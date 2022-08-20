import sqlite3
import tkcalendar
import time
from datetime import datetime,timedelta
from tkinter import *
from tkinter import messagebox
def issues():
    root=Tk()
    root.configure(background='powder blue')
    global s
    s=''
    root.geometry('500x400')
    con=sqlite3.connect('library.db')
    print('Database connected')

    l=Label(root,text="BOOK ISSUE",bg='blue',font=('Arial','50'))

    l1=Label(root,text="Book name",fg='black',bg='blue',font=('Arial','12'))
    l2=Label(root,text="ID",fg='black',bg='blue',font=('Arial','12'))
    l3=Label(root,text="Author",fg='black',bg='blue',font=('Arial','12'))
    l4=Label(root,text="Publisher",fg='black',bg='blue',font=('Arial','12'))
    l5=Label(root,text="No. of copies",fg='black',bg='blue',font=('Arial','12'))
    l6=Label(root,text="Date",fg='black',bg='blue',font=('Arial','12'))
    l7=Label(root,text="Email",fg='black',bg='blue',font=('Arial','12'))

    e1=Entry(root,width=50,font=('Arial','12'))
    e2=Entry(root,width=50,font=('Arial','12'))
    e3=Entry(root,width=50,font=('Arial','12'))
    e4=Entry(root,width=50,font=('Arial','12'))
    e5=Entry(root,width=50,font=('Arial','12'))
    e6=Entry(root,width=50,font=('Arial','12'))
    e7=Entry(root,width=50,font=('Arial','12'))

    l.grid(row=0,column=3,sticky=E,padx=50,pady=50)
    l1.grid(row=2,sticky=E,padx=50)
    e1.grid(row=2,column=3)

    k1=Label(root,text="Student Name",fg='black',bg='blue',font=('Arial','12'))
    k2=Label(root,text="Roll number",fg='black',bg='blue',font=('Arial','12'))
    k3=Label(root,text="Class",fg='black',bg='blue',font=('Arial','12'))

    s1=Entry(root,width=50,font=('Arial','12'))
    s2=Entry(root,width=50,font=('Arial','12'))
    s3=Entry(root,width=50,font=('Arial','12'))

    def Search():
        a=[e1.get()]
        r=con.execute('Select * from entry where name=?',a)
        x=r.fetchall()
        if(not x):  
            messagebox.showinfo('Hello','Book not found in library.')
        else:
            d=x[0][4]
            if(d>0):
                l2.grid(row=3)
                l3.grid(row=4)
                l4.grid(row=5)
                l5.grid(row=6)
                l6.grid(row=11)
                l7.grid(row=10)
                e2.grid(row=3,column=3)
                e3.grid(row=4,column=3)
                e4.grid(row=5,column=3)
                e5.grid(row=6,column=3)
                e6.grid(row=11,column=3)
                e7.grid(row=10,column=3)
                e2.insert(0,x[0][0])
                e3.insert(0,x[0][2])
                e4.insert(0,x[0][3])
                e5.insert(0,x[0][4])

                

                k1.grid(row=7)
                k2.grid(row=8)
                k3.grid(row=9)

                s1.grid(row=7,column=3)
                s2.grid(row=8,column=3)
                s3.grid(row=9,column=3)
                
                cal=tkcalendar.Calendar(root)
                def calen():
                    cal.grid(row=10,column=0)
                    def show(event):
                        global s
                        s=cal.get_date()
                        e6.insert(0,s)
                    cal.bind('<<CalendarSelected>>',show)
                def hidecal():
                    cal.grid_forget()
                def issue():
                    mm=e7.get()
                    nn=e1.get()
                    dates=datetime.strptime(s,'%m/%d/%y').date()
                    kk=dates+timedelta(days=7)
                    kk=datetime.strftime(kk,'%m/%d/%y')
                    a=[]
                    r=con.execute('Select * from student where roll={0}'.format(int(s2.get())))
                    x=r.fetchall()
                    n=0
                    flag=True
                    for i in x:
                        n+=1
                        if(i[3]==e1.get()):
                            flag=False
                            break
                    if(flag==True and n<3):
                        a.append(s1.get())
                        a.append(int(s2.get()))
                        a.append(s3.get())
                        a.append(e1.get())
                        s
                        a.append(s)
                        b=[e1.get()]
                        r=con.execute('Select * from entry where name=?',b)
                        z=r.fetchall()
                        i=z[0][4]-1
                        b.insert(0,i)
                        con.execute('update entry set copy=? where name=?',b)
                        con.commit()
                        con.execute('Insert into student values(?,?,?,?,?)',a)
                        con.commit()
                        messagebox.showinfo('hello','Book issued')
                        clear()
                    elif(n==3):
                         messagebox.showinfo('hello','A student can issue maximum 3 books.')
                    elif(flag==False):
                        messagebox.showinfo('hello','Only one copy of book can be issued per student.')
                        
                    import smtplib
                    fromaddr='testingmahima@gmail.com'
                    toaddrs=mm
                    msg="\r\n".join([
                    "From: testingmahima@gmail.com",
                    "To: user_you@gmail.com",
                    "Subject: BOOK ISSUE RECEIPT",
                    "",
                    nn+" book has been issued.The book has to be returned on "+kk+"\n\n\nWarm Regards\nNCU LIBRARY"
                    ])
                    username='testingmahima@gmail.com'
                    password='ncuindia'
                    server=smtplib.SMTP('smtp.gmail.com:587')
                    server.ehlo()
                    server.starttls()
                    server.login(username,password)
                    server.sendmail(fromaddr,toaddrs,msg)
                    server.quit()
                b9=Button(root,text='Calendar',bg='blue',command=calen,font=('Arial','20'))
                b10=Button(root,text='Hide Calendar',bg='blue',command=hidecal,font=('Arial','20'))
                b9.grid(row=12,column=1,rowspan=3,padx=20,pady=50,sticky=E)
                b10.grid(row=12,column=2,rowspan=3,padx=20,pady=50,sticky=E) 
                def clear():
                    e1.delete(0,END)
                    e2.delete(0,END)
                    e3.delete(0,END)
                    e4.delete(0,END)
                    e5.delete(0,END)
                    e6.delete(0,END)
                    e7.delete(0,END)
                    s1.delete(0,END)
                    s2.delete(0,END)
                    s3.delete(0,END)
                b4=Button(root,text='Clear Data',bg='blue',command=clear,font=('Arial','20'))
                b4.grid(row=12,column=5,rowspan=3,padx=20,pady=50,sticky=E)
                b5=Button(root,text='Issue',bg='blue',command=issue,font=('Arial','20'))
                b5.grid(row=12,column=4,rowspan=3,padx=20,pady=50,sticky=E)                  
    b2=Button(root,text='Search book',bg='blue',command=Search,font=('Arial','20'))
    b2.grid(row=13,column=3,pady=50,padx=10)
    def home():
        root.destroy()
        import library
        library.lib()
    b6=Button(root,text='Home',bg='blue',command=home,font=('Arial','30'))
    b6.grid(row=14,column=3,rowspan=3,padx=200,pady=10)
