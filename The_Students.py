from tkinter import *
import mysql.connector as m
from tkinter import messagebox as mb




#To create a database The_Student
con1=m.connect(host='localhost',port=3309,user='root',passwd='tiger')
cur_create=con1.cursor()
cur_create.execute("create database if not exists The_Student_Old_DB;")
cur_create.execute("use The_Student_Old_DB")

#To create a database cursor for executing queries
con=m.connect(host='localhost',port=3309,user='root',passwd='tiger',database='The_Student')
cur_insert=con.cursor()
cur_delete=con.cursor()
cur_create.execute("create table if not exists students(name varchar(50), passwd varchar(50), mobile varchar(10), email varchar(50), rollno varchar(10), batch varchar(20), dob varchar(10), adhaar varchar(20), address varchar(100), gender varchar(20));")      


def login_window():
    rootl=Tk()
    rootl.title("The Students")
    rootl.config(bg="LightBlue")
    rootl.geometry("500x300")
    rootl.minsize(500,300)
    rootl.maxsize(500,300)
    
    #Functions related to Login window
    def destry():
        rootl.destroy()

    def clr():
        e1_email.delete(first=0,last=300)
        e2_passwd.delete(first=0,last=300)

    #Connection of Database
    def login_DB():
        def clr():
            e1_email.delete(first=0,last=300)
            e2_passwd.delete(first=0,last=300)
    
        query=(f"select * from students where email='{e1_email.get()}' and passwd='{e2_passwd.get()}'")
        cur_insert.execute(query)
        a=cur_insert.fetchone()
        print(a)
        if a==None:
            b=mb.askretrycancel("Retry","You have entered incorrect credentials")
            if (b):
                clr()
            else:
                rootl.destroy()
                app_window()
        else:
            #Creating Profile Window
            rootl.destroy()
            root=Tk()
            root.title("The Students")
            root.config(bg="LightBlue")
            root.geometry("500x800")
            root.minsize(500,650)
            root.maxsize(500,650)
            #Logout Button Function
            def logO():
                a=mb.askyesno("Logout","Do you want to logout ?")
                if a==True:
                    root.destroy()
                    login_window()

            def feedback():
                a=mb.askquestion("Feedback","Do you like this Project ?")
                if a=="Yes":
                    mb.showinfo("Feedback","Thanks For your Feedback")

                else:
                    mb.showinfo("Feedback","We appreciate your kind Feedback")

            #Functions related to Update Button
            def stud_update():
                
                name=e1.get()
                print(name)
                mob=e7.get()
                print(mob)
                roll=e2.get()
                print(roll)
                batch=e3.get()
                print(batch)
                dob=e4.get()
                print(dob)
                gen=var1.get()
                print(gen)
                adh=e6.get()
                print(adh)
                addr=e9.get("1.0",END)
                print(addr)
                query=(f"update students set mobile='{mob}',rollno='{roll}',batch='{batch}',dob='{dob}',adhaar='{adh}',address='{addr}',gender='{gen}' where name='{name}'")
                cur_insert.execute(query)
                con.commit()
                mb.showinfo(" ","Information updated successfully")

            def stud_delete():
                a=mb.askquestion("Delete Student","Are you sure to delete this student permanently ?")
                print(a)
                print(e1.get())
                if a=='yes':                    
                    cur_delete.execute(f"delete from students where name='{e1.get()}'")
                    con.commit()
                    a=mb.askquestion("Delete Student","Student deleted successfully")
                    root.destroy()
                    login_window()
                    
                        
            #Creating Name Label
            l1=Label(root,text="Student Name",font=("arial",14,"bold"),bg="lightblue")
            l1.place(anchor=CENTER,x=150,y=130)
            #Creating Textbox of Name Label
            e1=Entry(root,width=26,font="calibri")
            e1.place(anchor=CENTER,x=350,y=130)
            

            #Creating RollNo Label
            l2=Label(root,text="Roll No",font=("arial",14,"bold"),bg="lightblue")
            l2.place(anchor=CENTER,x=155,y=170)
            #Creating RollNo textbox
            e2=Entry(root,width=23,font="calbri")
            e2.place(anchor=CENTER,x=350,y=170)
            
            #Creating Batch Label
            l3=Label(root,text="Batch",font=("arial",14,"bold"),bg="lightblue")
            l3.place(anchor=CENTER,x=155,y=210)
            #Creating Batch textbox
            e3=Entry(root,width=23,font="calbri")
            e3.place(anchor=CENTER,x=350,y=210)

            #Creating DOB Label
            l4=Label(root,text="Date of Birth",font=("arial",14,"bold"),bg="lightblue")
            l4.place(anchor=CENTER,x=155,y=250)
            #Creating DOB textbox
            e4=Entry(root,width=23,font="calbri")
            e4.place(anchor=CENTER,x=350,y=250)

            #Creating Label and Textbox of Gender
            var1=StringVar()
            var1.set(" ")
            l5=Label(root,text="Gender",font=("arial",14,"bold"),bg="lightblue")
            l5.place(anchor=CENTER,x=140,y=290)
            r1=Radiobutton(root,text="Male",font="airal 10 bold",activebackground="lightblue",variable=var1,value="Male",bg="lightblue")
            r1.place(anchor=CENTER,x=270,y=290)
            r2=Radiobutton(root,text="Female",font="arial 10 bold",activebackground="lightblue",variable=var1,value="Female",bg="lightblue")
            r2.place(anchor=CENTER,x=350,y=290)


            #Creating Adhaar Number Label
            l6=Label(root,text="Adhaar Number",font=("arial",14,"bold"),bg="lightblue")
            l6.place(anchor=CENTER,x=150,y=330)
            #Creating AdhaarNumber textbox
            e6=Entry(root,width=22,font="calbri")
            e6.place(anchor=CENTER,x=350,y=330)

            
            #Creating Mobile No Label
            l7=Label(root,text="Mobile Number",font=("arial",14,"bold"),bg="lightblue")
            l7.place(anchor=CENTER,x=150,y=370)
            #Creating Textbox of Mobile No Label
            e7=Entry(root,width=25,font="calibri")
            e7.place(anchor=CENTER,x=350,y=370)

            #Creating Email Label
            l8=Label(root,text="E-mail ID",font=("arial",14,"bold"),bg="lightblue")
            l8.place(anchor=CENTER,x=150,y=410)
            #Creating Textbox of Email Label
            e8=Entry(root,width=25,font="calibri")
            e8.place(anchor=CENTER,x=350,y=410)

            #Creating Address Label
            l9=Label(root,text="Address",font=("arial",14,"bold"),bg="lightblue")
            l9.place(anchor=CENTER,x=150,y=450)
            #Creating Textbox of Address Label
            e9=Text(root,width=25,height=3,font="calibri",wrap=WORD)
            e9.place(anchor=CENTER,x=350,y=470)

            #Creating a button to Update
            b1=Button(root,text="Update",relief="groove",font=("arial",13,"bold"),height=1)
            b1.place(anchor=CENTER,x=260.5,y=570)
            b1.config(command=stud_update)

            #Creating a button to Delete
            b1=Button(root,text="Delete",relief="groove",font=("arial",13,"bold"),height=1)
            b1.place(anchor=CENTER,x=260.5,y=620)
            b1.config(command=stud_delete)
            
            #Creating a button to back
            b2=Button(root,text="Logout",relief="groove",font=("arial",13,"bold"),width=6,height=1)
            b2.place(anchor=CENTER,x=167,y=570)
            b2.config(command=logO)

            #Inserting a image
            image1=PhotoImage(file="logopp.png")
            image1=image1.subsample(18,18)
            image_label=Label(root,text="Student Info",font="times 12 bold",image=image1,bg="lightblue",compound=TOP)
            image_label.pack(pady=8)

            #Creating a button to Feedback    
            b3=Button(root,text="Feedback",relief="groove",font=("arial",13,"bold"),width=8,height=1)
            b3.place(anchor=CENTER,x=360,y=570)
            b3.config(command=feedback)
            
            #Update Info
            e1.insert(0,a[0])
            e1.config(state=DISABLED)
            e2.insert(0,a[4])
            e3.insert(0,a[5])
            e4.insert(0,a[6])
            if a[9]=='':
                var1.set(" ")
            else:
                var1.set(a[9])
            e6.insert(0,a[7])
            e7.insert(0,a[2])
            e8.insert(0,a[3])
            e8.config(state=DISABLED)
            e9.insert(INSERT,a[8])
            root.mainloop()
            
    #Creating Email Label
    l1=Label(rootl,text="Email ID",font=("arial",15,"bold"),bg="lightblue")
    l1.place(anchor=CENTER,x=160,y=120)
    #Creating Textbox of Email Label
    e1_email=Entry(rootl,width=23,font="calibri")
    e1_email.place(anchor=CENTER,x=325,y=120)

    #Creating Password Label
    l2=Label(rootl,text="Password",font=("arial",15,"bold"),bg="lightblue")
    l2.place(anchor=CENTER,x=160,y=160)
    #Creating Password textbox
    e2_passwd=Entry(rootl,width=21,show="*",font="calbri")
    e2_passwd.place(anchor=CENTER,x=325,y=160)

    #Creating a button to login
    b1=Button(rootl,text="Login",relief="groove",font=("arial",13,"bold"),height=1)
    b1.place(anchor=CENTER,x=259,y=200)
    b1.config(command=login_DB)

    #Creating a button to back
    b2=Button(rootl,text="Back",relief="groove",font=("arial",13,"bold"),width=6,height=1)
    b2.place(anchor=CENTER,x=219,y=250)
    b2.config(command=lambda:[destry(),app_window()])

    #Inserting a image
    image1=PhotoImage(file="logop.png")
    image1=image1.subsample(18,18)
    image_label=Label(rootl,text="LOGIN",font="times 12 bold",image=image1,bg="lightblue",compound=TOP)
    image_label.pack(pady=8)

    #Creating a button to clear
    b3=Button(rootl,text="Clear",relief="groove",font=("arial",13,"bold"),width=6,height=1)
    b3.place(anchor=CENTER,x=299,y=250)
    b3.config(command=clr)
    
    rootl.mainloop()


###################################################### [ Register Window ] ###################################################################################
def register_window():
    root=Tk()
    root.title("The Students")
    root.config(bg="LightBlue")
    root.geometry("500x500")
    root.minsize(500,500)
    root.maxsize(500,500)



    #To destroy the window
    def destry():
        root.destroy()





    #Functions related to Register Button
    def chck_pass():
        if(e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()==""):
            blabel.config(text="Please enter all the required details for registeration!")
        else:
            if((e2.get())==(e3.get())):
                e3.config(fg="black")
                blabel.config(text="")
                register_DB()    
            else:
                e3.config(fg="red")
                blabel.config(text="Password does not match !")


                
    #Creating Funtion of Clear button
    def clr():
        e1.delete(first=0,last=300)
        e2.delete(first=0,last=300)
        e3.delete(first=0,last=300)
        e4.delete(first=0,last=300)
        e5.delete(first=0,last=300)
        blabel.config(text="")




    #Connection of Database
    def register_DB():
        try:
            query=(f"insert into students values('{e1.get()}','+91{e2.get()}',{e4.get()},'{e5.get()}','','','','','','')")
            a=cur_insert.execute(query)
            con.commit()
            mb.showinfo('Successfull Execution','Student registeration successfully')
            clr()

        except Exception:
            mb.showinfo("Unsuccessfull Execution","Error occured while Registering. Please retry")
            clr()



        
    #Creating Name Label
    l1=Label(root,text="Enter Name",font=("arial",14,"bold"),bg="lightblue")
    l1.place(anchor=CENTER,x=85,y=130)
    #Creating Textbox of Name Label
    e1=Entry(root,width=25,font="calibri")
    e1.place(anchor=CENTER,x=350,y=130)

    #Creating Password Label
    l2=Label(root,text="Enter Password",font=("arial",14,"bold"),bg="lightblue")
    l2.place(anchor=CENTER,x=105,y=170)
    #Creating Password textbox
    e2=Entry(root,width=23,show="*",font="calbri")
    e2.place(anchor=CENTER,x=350,y=170)

    #Creating RPassword Label
    l3=Label(root,text="Re-Enter Password",font=("arial",14,"bold"),bg="lightblue")
    l3.place(anchor=CENTER,x=120,y=210)
    #Creating RPassword textbox
    e3=Entry(root,width=23,font="calbri")
    e3.place(anchor=CENTER,x=350,y=210)
             
    #Creating Mobile No Label
    l1=Label(root,text="Enter Mobile",font=("arial",14,"bold"),bg="lightblue")
    l1.place(anchor=CENTER,x=90,y=250)
    #Creating Textbox of Mobile No Label
    e4=Entry(root,width=25,font="calibri")
    e4.place(anchor=CENTER,x=350,y=250)

    #Creating Email Label
    l1=Label(root,text="Enter E-mail",font=("arial",14,"bold"),bg="lightblue")
    l1.place(anchor=CENTER,x=90,y=290)
    #Creating Textbox of Email Label
    e5=Entry(root,width=25,font="calibri")
    e5.place(anchor=CENTER,x=350,y=290)

    #Creating a blank textbox
    blabel=Label(root,text="",bg="lightblue",fg="red",font="arial 12 bold",width=40)
    blabel.place(x=55,y=330)

    #Creating a button to Register
    b1=Button(root,text="Register",relief="groove",font=("arial",13,"bold"),height=1)
    b1.place(anchor=CENTER,x=265.5,y=400)
    b1.config(command=chck_pass)
    
    #Creating a button to back
    b2=Button(root,text="Back",relief="groove",font=("arial",13,"bold"),width=6,height=1)
    b2.place(anchor=CENTER,x=167,y=450)
    b2.config(command=lambda:[destry(),app_window()])

    #Inserting a image
    image1=PhotoImage(file="logo.png")
    image1=image1.subsample(18,18)
    image_label=Label(root,text="REGISTER",font="times 12 bold",image=image1,bg="lightblue",compound=TOP)
    image_label.pack(pady=8)

    #Creating a button to clear    
    b3=Button(root,text="Clear",relief="groove",font=("arial",13,"bold"),width=6,height=1)
    b3.place(anchor=CENTER,x=360,y=450)
    b3.config(command=clr)
    
    root.mainloop()
###################################################### [ Register Window End ] ###################################################################################
    
def app_window():
    #Creating the application window ( " The Students " )
    win1=Tk()
    win1.title("The Students")
    win1.config(bg="LightBlue")
    win1.geometry("500x270")
    win1.minsize(500,270)
    win1.maxsize(500,270)
    #To destroy the window
    def destry():
        win1.destroy()

    #Label for the Title
    l1=Label(win1,text=" THE STUDENTS ",font=("Times",30,"bold"),bg="LightBlue",fg="grey",relief="ridge")
    l1.pack(pady=40)

    #Register Button
    b1=Button(win1,text="Register",relief="groove",font=("arial",13,"bold"),width=15,height=1)
    b1.pack()
    b1.config(command=lambda:[destry(),register_window()])

    #Login Button
    b2=Button(win1,text="Login",relief="groove",font=("arial",13,"bold"),width=15,height=1)
    b2.pack(pady=10)
    b2.config(command=lambda:[destry(),login_window()])

    #Credit Label
    l2=Label(win1,text="designed by DATTARAM KOLTE",font=("calibri",8,"bold"),bg="LightBlue")
    l2.place(x=130,y=252)

    #Student Count
    cur_insert=con.cursor()
    query=(f"select count(*) from students")
    cur_insert.execute(query)
    a=cur_insert.fetchone()
    l3=Label(win1,text=f"Students Count: {a[0]}",font=("calibri",11,"bold"),bg="LightBlue")
    l3.place(x=200,y=230)

    win1.mainloop()

#MAIN PROGRAM EXECUTION
app_window()
