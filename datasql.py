from tkinter import*
import tkinter.messagebox as messagebox
import mysql.connector as mysql
def insert():
    name=txt.get()
    age=txt2.get()
    phone=txt3.get()
    if name=='' or age=='' or phone=='':
         messagebox.showinfo("Insert Status","Please fill all the fields")
    else:
         conn=mysql.connect(host='localhost',user='root',passwd='',database='kee')
         cursor=conn.cursor()
         cursor.execute("insert into salay values('%s','%s','%s')"%(name,age,phone))
         conn.commit()
         txt.delete(0,END)
         txt2.delete(0,END)
         txt3.delete(0,END)
         messagebox.showinfo("Insert Status","Inserted Successfully")
         cursor.close()
         conn.close()
def show():
    name=txt.get()
    if name=='':
         messagebox.showinfo("Insert Status","please fill all the fields")
    else:
         conn=mysql.connect(host='localhost',user='root',passwd='',database='kee')
         cursor=conn.cursor()
         cursor.execute("select * from salay where name='%s'"%name)
         rows=cursor.fetchall()
         for row in rows:
            txt2.insert(0,row[1])
            txt3.insert(0,row[2])
         cursor.close()
def update():
    name=txt.get()
    age=txt2.get()
    phone=txt3.get()
    if name=='' or age=='' or phone=='':
         messagebox.showinfo("Insert Status","Please fill all the fields")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='kee')
        cursor=conn.cursor()
        cursor.execute("update salay set age='%s',phone='%s' where name='%s'"%(age,phone,name))
        conn.commit()
        txt.delete(0,END)
        txt2.delete(0,END)
        txt3.delete(0,END)
        messagebox.showinfo("Update Status","Updated Successfully")
        cursor.close()
        conn.close()
def delete():
    name=txt.get()
    if name=='':
         messagebox.showinfo("Insert Status","Please fill all the fields")
    else:
         conn=mysql.connect(host='localhost',user='root',passwd='',database='kee')
         cursor=conn.cursor()
         cursor.execute("delete from salay where name='%s'"%name)
         conn.commit()
         txt.delete(0,END)
         txt2.delete(0,END)
         txt3.delete(0,END)
         messagebox.showinfo("Insert Status","Delete Successfully")
         cursor.close()
         conn.close()
def Clear():
          txt.delete(0,END)
          txt2.delete(0,END)
          txt3.delete(0,END)
x=Tk()
x.geometry("300x300")
lbl1=Label(x, text="NAME")
lbl2=Label(x, text="AGE")
lbl3=Label(x, text="PHONE")
txt=Entry(x)
txt2=Entry(x)
txt3=Entry(x)
btn=Button(text="Save", command=insert)
btn1=Button(text="show", command=show)
btn2=Button(text="update", command=update)
btn3=Button(text="delete",command=delete)
btn4=Button(text="Clear",command=Clear)
btn.place(x=20,y=130)
btn1.place(x=80,y=130)
btn2.place(x=140,y=130)
btn3.place(x=200,y=130)
btn4.place(x=250,y=130)
lbl1.place(x=20,y=20)
lbl2.place(x=20,y=60)
lbl3.place(x=20,y=100)
txt.place(x=80,y=20)
txt2.place(x=80,y=60)
txt3.place(x=80,y=100)
mainloop()