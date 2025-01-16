import customtkinter 
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from Queries_patient_entity import insert_patient,get_patients,update_patient,delete_patient,get_last_patient_id
import re

def is_email_valid(email):
    way = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(way, email) is not None

def valid_contact(phone):
   return phone.isdigit() and len(phone)==10

def is_valid_age(age):
    return age.isdigit() and 0 <= int(age) <= 240

def submit_patients():
   id = label2.get()
   first_name =label4.get()
   last_name = label6.get()
   email = label8.get()
   phone = label10.get()
   address = label12.get()
   gender = label14.get()
   age = label16.get()

   if  first_name and last_name and email and phone and address and gender and age:
     if is_email_valid(email):
      if valid_contact(phone):
         if is_valid_age(age):
           insert_patient(id,first_name, last_name,email,phone,address,gender,age)
           messagebox.showinfo("success","patient inserted successfully")
           load_patient()
           reset()
         else:
           messagebox.showwarning("invalid age","enter valid age")
      else:
         messagebox.showwarning("invalid contact","enter valid phone number with 10 digits")
     else:
         messagebox.showwarning("invalid email","enter valid email") 
   else:
       messagebox.showwarning("warning","all inputs required")

def load_patient():
     for item in tree.get_children():
        tree.delete(item)
     patients = get_patients()
     for patient in patients:
        tree.insert("", "end", values=patient)
        
def reset():
    label2.delete(0,END)
    label4.delete(0,END)
    label6.delete(0,END)
    label8.delete(0,END)
    label10.delete(0,END)
    label12.delete(0,END)
    label14.set("")
    label16.delete(0,END)  
    update_id() 
def delete_selected_patient():
   selected_item  = tree.selection()
   if not selected_item:
      messagebox.showwarning("no selection","please select patient to delete")
      return  
   id= tree.item(selected_item)['values'][0]
   delete_patient(id)
   load_patient()
   #update_id()
   messagebox.showinfo("Success", "Patient successfully deleted")  
def update_id():
    next_id =  get_last_patient_id()
    label2.configure(state=NORMAL)
    label2.delete(0,END)
    label2.insert(0,next_id)
    label2.configure(state=DISABLED)

def open_about_window():
    about_window = Toplevel(root)
    about_window.title("About")
    about_window.geometry("100x200")
    Label(about_window, text="This is the About page.").pack(pady=20)

def initialize_gui():
 print("Initializing application...")
 root = customtkinter.CTk()
 print("Application started!")
 root.title("DISPENSARY MANAGEMENT")
 root.geometry("1000x500")
 root.config(bg='#022c22')

 Menubar = Menu(root)
 root.config(menu=Menubar)#displays ur menu bar on the window

 File = Menu(Menubar,tearoff=0)
 Menubar.add_cascade(label="Files",menu=File)


 File.add_command(label="reports")
 File.add_command(label="users")
 File.add_command(label="Medicine")
 File.add_command(label="Nurses")
 File.add_separator()
 File.add_command(label="Exit")

 Menubar.add_command(label="About", command=open_about_window)
 CO1='#022c22'
 CO2='#115e59'
 CO3='#ecfdf5'
 font1 = ('Helvetica',15)
 #font2 = ('Helvetica',12,'bold')

 label1 = customtkinter.CTkLabel(master= root, text="ID :",font=font1,bg_color=CO1)
 label1.place(x=20,y=20)
 label2 = customtkinter.CTkEntry(master= root,text_color='#000', border_color=CO2,bg_color=CO2,fg_color=CO3)
 label2.place(x=100,y=20)
 label2.configure(state=DISABLED)

 label3 = customtkinter.CTkLabel(master= root, text="F_name:",font=font1,bg_color=CO1)
 label3.place(x=20,y=50)
 label4 = customtkinter.CTkEntry(master= root,text_color='#000', placeholder_text="First_name",border_color=CO2,bg_color=CO2,fg_color=CO3)
 label4.place(x=100,y=50)

 label5 = customtkinter.CTkLabel(master= root, text="l_name:",font=font1,bg_color=CO1)
 label5.place(x=20,y=80)
 label6 = customtkinter.CTkEntry(master= root,text_color='#000', placeholder_text="Last_name",border_color=CO2,bg_color=CO2,fg_color=CO3)
 label6.place(x=100,y=80)

 label7 = customtkinter.CTkLabel(master= root, text="email:",font=font1,bg_color=CO1)
 label7.place(x=20,y=110)
 label8 = customtkinter.CTkEntry(master= root,text_color='#000',border_color=CO2,bg_color=CO2,fg_color=CO3)
 label8.place(x=100,y=110)

 label9 = customtkinter.CTkLabel(master= root, text="contact:",font=font1,bg_color=CO1)
 label9.place(x=20,y=140)
 label10 = customtkinter.CTkEntry(master= root,text_color='#000',border_color=CO2,bg_color=CO2,fg_color=CO3)
 label10.place(x=100,y=140)

 label11 = customtkinter.CTkLabel(master= root, text="Address:",font=font1,bg_color=CO1)
 label11.place(x=20,y=170)
 label12 = customtkinter.CTkEntry(master= root,text_color='#000',border_color=CO2,bg_color=CO2,fg_color=CO3)
 label12.place(x=100,y=170)

 label13 = customtkinter.CTkLabel(master= root, text="Gender:",font=font1,bg_color=CO1)
 label13.place(x=20,y=200)
 options=['male', 'female']
 variable1=StringVar()
 label14 = customtkinter.CTkComboBox(master= root,text_color='#000',variable=variable1,dropdown_fg_color=CO1,values=options,border_color=CO2,bg_color=CO2,fg_color=CO3,state='readonly')
 label14.place(x=100,y=200)

 label15 = customtkinter.CTkLabel(master= root, text="Age:",font=font1,bg_color=CO1)
 label15.place(x=20,y=230)
 label16 = customtkinter.CTkEntry(master= root,text_color='#000',border_color=CO2,bg_color=CO2,fg_color=CO3)
 label16.place(x=100,y=230)

 button1= customtkinter.CTkButton(master= root,text="submit patient",command=submit_patients, border_color=CO2,corner_radius=32,bg_color=CO1,hover_color='#064e3b',fg_color='#065f46')
 button1.place(x=80,y=270)

 button2= customtkinter.CTkButton(master= root,text="add patient",command=load_patient,border_color=CO2,bg_color=CO1,corner_radius=32,hover_color='#064e3b',fg_color='#065f46')
 button2.place(x=290,y=400)

 button1= customtkinter.CTkButton(master= root,text="update patient",border_color=CO2,corner_radius=32,bg_color=CO1,hover_color='#064e3b',fg_color='#065f46')
 button1.place(x=470,y=400)

 button1= customtkinter.CTkButton(master= root,text="delete patient",border_color=CO2,corner_radius=32,bg_color=CO1,hover_color='#064e3b',fg_color='#065f46')
 button1.place(x=650,y=400)
 style = ttk.Style(root)

 style.theme_use('clam')
 style.configure('treeview',foreground=CO2,background=CO3,fieldbackground=CO1)
 style.map('treeview',background=[('selected','#bbf7d0')])

 tree = ttk.Treeview(root,height = 15)

 tree['columns'] = ('id','fisrt_name','last_name','Contact','Address','Gender','Age' )

 tree.column('#0',width=0,stretch=tk.NO)
 tree.column('id',anchor=tk.CENTER,width=50)
 tree.column('fisrt_name',anchor=tk.CENTER,width=120)
 tree.column('last_name',anchor=tk.CENTER,width=120)
 tree.column('Contact',anchor=tk.CENTER,width=120)
 tree.column('Address',anchor=tk.CENTER,width=120)
 tree.column('Gender',anchor=tk.CENTER,width=80)
 tree.column('Age',anchor=tk.CENTER,width=50)

 tree.heading('id',text='ID')
 tree.heading('fisrt_name',text='fisrt_name')
 tree.heading('last_name',text='sirname')
 tree.heading('Contact',text='Contact')
 tree.heading('Address',text='Address')
 tree.heading('Gender',text='Gender')
 tree.heading('Age',text='Age')
 tree.place(y=20,x=280)

 root.mainloop()
print("Application closed.")
if __name__ == "__main__":
    initialize_gui()
