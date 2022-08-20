import sqlite3
from tkinter import *
from tkinter import messagebox

def entry():
    root=Tk()
    root.geometry('500x400')
    root.configure(background='powder blue')
    con=sqlite3.connect('library.db')
    print('Database connected')

    l=Label(root,text="BOOK ENTRY",fg='black',bg='blue',font=('Arial','50'))

    l1=Label(root,text="Book id",fg='black',bg='blue',font=('Arial','12'))
    l2=Label(root,text="Name",fg='black',bg='blue',font=('Arial','12'))
    l3=Label(root,text="Author",fg='black',bg='blue',font=('Arial','12'))
    l4=Label(root,text="Publisher",fg='black',bg='blue',font=('Arial','12'))
    l5=Label(root,text="No. of copies",fg='black',bg='blue',font=('Arial','12'))

    e1=Entry(root,width=50,font=('Arial','12'))
    e2=Entry(root,width=50,font=('Arial','12'))
    e3=Entry(root,width=50,font=('Arial','12'))
    e4=Entry(root,width=50,font=('Arial','12'))
    e5=Entry(root,width=50,font=('Arial','12'))

    l.grid(row=0,column=3,sticky=E,padx=50,pady=50)
    l1.grid(row=2,padx=20)
    l2.grid(row=3,padx=20)
    l3.grid(row=4,padx=20)
    l4.grid(row=5,padx=20)
    l5.grid(row=6,padx=20)

    e1.grid(row=2,column=3)
    e2.grid(row=3,column=3)
    e3.grid(row=4,column=3)
    e4.grid(row=5,column=3)
    e5.grid(row=6,column=3)

    def Save():
        a=[]
        r=con.execute('Select * from entry where id={0}'.format(int(e1.get())))
        x=r.fetchall()
        if(not x):  
            a.append(int(e1.get()))
            a.append(e2.get())
            a.append(e3.get())
            a.append(e4.get())
            a.append(int(e5.get()))
            
            con.execute('Insert into entry values(?,?,?,?,?)',a)
            con.commit()
            messagebox.showinfo('hello','Record saved')
        else:
            messagebox.showinfo('hello','Record already exist')
    b1=Button(root,text='Save',bg='blue',command=Save,font=('Arial','20'))
    b1.grid(row=7,column=1,padx=20,pady=50)

    def Retrieve():
        a=[]
        r=con.execute('Select * from entry where id={0}'.format(int(e1.get())))
        x=r.fetchall()
        if(not x):  
            messagebox.showinfo('hello','Record not found')
        else:
            e2.insert(0,x[0][1])
            e3.insert(0,x[0][2])
            e4.insert(0,x[0][3])
            e5.insert(0,x[0][4])
            
    b2=Button(root,text='Retrieve',bg='blue',command=Retrieve,font=('Arial','20'))
    b2.grid(row=7,column=2)

    def Clear():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
         
    b3=Button(root,text='Clear',bg='blue',command=Clear,font=('Arial','20'))
    b3.grid(row=7,column=4,padx=20)

    def Update():
        a=[]
        r=con.execute('Select * from entry where id={0}'.format(int(e1.get())))
        x=r.fetchall()
        if(not x):  
            messagebox.showinfo('hello','Record not found')
        else:
            ans=messagebox.askyesno('hello','Want to update this record ?')
            if(ans):
                a.append(e2.get())
                a.append(e3.get())
                a.append(e4.get())
                a.append(int(e5.get()))
                a.append(int(e1.get()))
                con.execute('update entry set name=?,author=?,publisher=?,copy=? where id=?',a)
                con.commit()
                messagebox.showinfo('hello','Record updated')
            else:
                messagebox.showinfo('hello','not updated')
                
    b4=Button(root,text='Update',bg='blue',command=Update,font=('Arial','20'))
    b4.grid(row=7,column=5)

    def homee():
        root.destroy()
        import library
        library.lib()
    b5=Button(root,text='Home',bg='blue',command=homee,font=('Arial','30'))
    b5.grid(row=7,column=3,padx=200)
    root.mainloop()


