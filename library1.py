from tkinter import *
from PIL import ImageTk, Image
def lib():
    fm=Tk()
    fm.geometry('1600x1000')
    fm.configure(background='powder blue')
    img1=ImageTk.PhotoImage(Image.open("book.png"))
    img2=ImageTk.PhotoImage(Image.open("issue.png"))
    img3=ImageTk.PhotoImage(Image.open("return.png"))
    img4=ImageTk.PhotoImage(Image.open("exit.png"))
    #img1=PhotoImage(file=r"C:\\Desktop\\hello.png")
    def books():
        import lib_entry
        fm.destroy()
        lib_entry.entry()
    def issuee():
        import lib_issue
        fm.destroy()
        lib_issue.issues()
    def returnn():
        import lib_return
        fm.destroy()
        lib_return.returns()
    def ex():
        fm.destroy()
    l=Label(fm,text="WELCOME",fg='black',bg='blue',font=('Arial','50')).grid(row=0,column=2)
    l1=Label(fm,text="      ",bg='powder blue',font=('Arial','100')).grid(column=0)
    entry=Button(fm,image=img1,width=300,height=250,command=books).grid(row=1,column=1,pady=20,padx=20)
    entry2=Button(fm,text="BOOK ENTRY",fg='black',bg='blue',font=('Arial','20'),command=books).grid(row=2,column=1)

    issue=Button(fm,image=img2,width=300,height=250,command=issuee).grid(row=1,column=4,pady=20,padx=20)
    issue2=Button(fm,text="ISSUE BOOK",fg='black',bg='blue',font=('Arial','20'),command=issuee).grid(row=2,column=4)

    retur=Button(fm,image=img3,width=300,height=250,command=returnn).grid(row=3,column=1,pady=20)
    retur=Button(fm,text="RETURN BOOK",fg='black',bg='blue',font=('Arial','20'),command=returnn).grid(row=4,column=1)

    exits=Button(fm,image=img4,width=300,height=250,command=ex).grid(row=3,column=4,pady=20)
    exits=Button(fm,text="EXIT",fg='black',bg='blue',font=('Arial','20'),command=ex).grid(row=4,column=4)
    fm.mainloop()
