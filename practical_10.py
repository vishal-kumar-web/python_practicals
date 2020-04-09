from tkinter import *
from tkinter import ttk
import mysql.connector

def sql_execution(sql):
    conn = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='dbone',
                              auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    #cursor.execute('''create table student(f_name text,l_name text,father_name text,gender text,phone int,email text,college text);''')
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
def on_submit():
    Insert_sql = "insert into student values('{0}','{1}','{2}','{3}','{4}','{5}','{6}');".format(first_name.get(),last_name.get(),father_name.get()                                                                                         ,gender_choice.get(),phone_no.get(),email_id.get(),college.get())
    sql_execution(Insert_sql)
   
def show_db():
    sql = "Select * from student;"
    conn = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='dbone',
                              auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print("First Name: ",row[0],end=" ")
        print("Last Name: ",row[1],end=" ")
        print("Father's Name: ",row[2],end=" ")
        print("Gender: ",row[3],end=" ")
        print("Phone Number: ",row[4],end=" ")
        print("Email ID: ",row[5],end=" ")
        print("College Name: ",row[6])
    conn.close()
    
def on_clear():
    first_name.delete(0,END)
    last_name.delete(0,END)
    father_name.delete(0,END)
    phone_no.delete(0,END)
    email_id.delete(0,END)

r = Tk()
r.title('registration form')
#r.geometry('400x400')
l_heading = Label(r,text = 'Registration Form')
l_heading.grid(row=0,column=1)

l_first_name = Label(r,text = 'First Name: ').grid(row=1,column=0)
first_name = Entry(r,width=25)
first_name.grid(row=1,column=1)

l_last_name = Label(r,text = 'Last Name: ').grid(row=2,column=0)
last_name = Entry(r,width=25)
last_name.grid(row=2,column=1)

l_father_name = Label(r,text = "Father's Name: ").grid(row=3,column=0)
father_name = Entry(r,width=25)
father_name.grid(row=3,column=1)

l_gender = Label(r,text = "Gender: ").grid(row=4,column=0)
gender_choice = StringVar()
gender_M = Radiobutton(r,text='Male',variable=gender_choice,value='M')
gender_M.grid(row=4,column=1)
gender_F = Radiobutton(r,text='Female',variable=gender_choice,value='F')
gender_F.grid(row=4,column=2)

l_phone_no = Label(r,text = "Phone No: ").grid(row=5,column=0)
phone_no = Entry(r,width=25)
phone_no.grid(row=5,column=1)

l_email_id = Label(r,text = "Email ID: ").grid(row=6,column=0)
email_id = Entry(r,width=25)
email_id.grid(row=6,column=1)

l_college = Label(r,text= " College Name: ").grid(row=7,column=0)
college_var = StringVar()
college = ttk.Combobox(r,width='25',textvariable=college_var)
college['values'] = ('CGC, Landran','CGC, Janjeri','CU')
college.grid(row=7,column=1)
college.current(0)

submit_button = Button(r,text="Submit",padx=15,pady=10,command = on_submit).grid(row=8,column=1)
clear_button = Button(r,text="Clear",padx=15,pady=10,command = on_clear).grid(row=9,column=1)
show_db_button = Button(r,text="Show Database",padx=15,pady=10,command = show_db).grid(row=10,column=1)

r.mainloop()
