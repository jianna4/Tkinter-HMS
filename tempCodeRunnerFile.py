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
