import customtkinter 
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


def open_about_window():
 about_window = Toplevel(root)
 about_window.title("About")
 about_window.geometry("100x200")
 Label(about_window, text="This is the About page.").pack(pady=20)

root = customtkinter.CTk()
root.title("PATIENT TREATMENT RECORDS")
root.geometry("1000x500")
root.config(bg='#022c22')

Menubar = Menu(root)
root.config(menu=Menubar)#displays ur menu bar on the window

File = Menu(Menubar,tearoff=0)
Menubar.add_cascade(label="Files",menu=File)

File.add_command(label="home")
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


label3 = customtkinter.CTkLabel(master= root, text="patient_id:",font=font1,bg_color=CO1)
label3.place(x=20,y=50)
label4 = customtkinter.CTkEntry(master= root,text_color='#000', placeholder_text="patient_id",border_color=CO2,bg_color=CO2,fg_color=CO3)
label4.place(x=100,y=50)

label5 = customtkinter.CTkLabel(master= root, text="nurse_id:",font=font1,bg_color=CO1)
label5.place(x=20,y=80)
label6 = customtkinter.CTkEntry(master= root,text_color='#000', placeholder_text="Last_name",border_color=CO2,bg_color=CO2,fg_color=CO3)
label6.place(x=100,y=80)

label7 = customtkinter.CTkLabel(master= root, text="Date:",font=font1,bg_color=CO1)
label7.place(x=20,y=110)
label8 = customtkinter.CTkEntry(master= root,text_color='#000',border_color=CO2,bg_color=CO2,fg_color=CO3)
label8.place(x=100,y=110)

label9 = customtkinter.CTkLabel(master= root, text="treatment_id:",font=font1,bg_color=CO1)
label9.place(x=20,y=140)
label10 = customtkinter.CTkEntry(master= root,text_color='#000',border_color=CO2,bg_color=CO2,fg_color=CO3)
label10.place(x=100,y=140)

label11 = customtkinter.CTkLabel(master= root, text="Symptoms:",font=font1,bg_color=CO1)
label11.place(x=20,y=170)
label12 = customtkinter.CTkEntry(master= root,text_color='#000',border_color=CO2,bg_color=CO2,fg_color=CO3)
label12.place(x=100,y=170)

label13 = customtkinter.CTkLabel(master= root, text="Gender:",font=font1,bg_color=CO1)
label13.place(x=20,y=200)
options=['male', 'female']
variable1=StringVar()
label14 = customtkinter.CTkComboBox(master= root,text_color='#000',variable=variable1,dropdown_fg_color=CO1,values=options,border_color=CO2,bg_color=CO2,fg_color=CO3,state='readonly')
label14.place(x=100,y=200)



button1= customtkinter.CTkButton(master= root,text="submit patient", border_color=CO2,corner_radius=32,bg_color=CO1,hover_color='#064e3b',fg_color='#065f46')
button1.place(x=80,y=270)

#button2= customtkinter.CTkButton(master= root,text="add patient",command=load_patient,border_color=CO2,bg_color=CO1,corner_radius=32,hover_color='#064e3b',fg_color='#065f46')
#button2.place(x=290,y=400)

button1= customtkinter.CTkButton(master= root,text="update patient",border_color=CO2,corner_radius=32,bg_color=CO1,hover_color='#064e3b',fg_color='#065f46')
button1.place(x=470,y=400)

button1= customtkinter.CTkButton(master= root,text="delete patient",border_color=CO2,corner_radius=32,bg_color=CO1,hover_color='#064e3b',fg_color='#065f46')
button1.place(x=650,y=400)
style = ttk.Style(root)

style.theme_use('clam')
style.configure('treeview',foreground=CO2,background=CO3,fieldbackground=CO1)
style.map('treeview',background=[('selected','#bbf7d0')])

tree = ttk.Treeview(root,height = 15)

tree['columns'] = ('id','patient_id','nurses_id','day_of_treatment','treatment_id','symptoms' )

tree.column('#0',width=0,stretch=tk.NO)
tree.column('id',anchor=tk.CENTER,width=50)
tree.column('patient_id',anchor=tk.CENTER,width=120)
tree.column('nurses_id',anchor=tk.CENTER,width=120)
tree.column('day_of_treatment',anchor=tk.CENTER,width=120)
tree.column('treatment_id',anchor=tk.CENTER,width=120)
tree.column('symptoms',anchor=tk.CENTER,width=80)

tree.heading('id',text='ID')
tree.heading('patient_id',text='patient_id')
tree.heading('nurses_id',text='nurse_id')
tree.heading('day_of_treatment',text='Contact')
tree.heading('treatment_id',text='treatment_id')
tree.heading('symptoms',text='symptoms')

tree.place(y=20,x=280)
root.mainloop()