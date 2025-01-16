import tkinter as tk
from tkinter import messagebox
#import db_operations

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Management System")

        # Table Frame
        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack(pady=10)
        
        self.table_label = tk.Label(self.table_frame, text="Tables")
        self.table_label.pack(side=tk.LEFT, padx=10)
        
        self.table_listbox = tk.Listbox(self.table_frame, height=10)
        self.table_listbox.pack(side=tk.LEFT)
        
        self.fetch_tables_button = tk.Button(self.table_frame, text="Fetch Tables", command=self.fetch_tables)
        self.fetch_tables_button.pack(side=tk.LEFT, padx=10)
        
        # Record Frame
        self.record_frame = tk.Frame(self.root)
        self.record_frame.pack(pady=10)
        
        self.record_label = tk.Label(self.record_frame, text="Records")
        self.record_label.pack(side=tk.LEFT, padx=10)
        
        self.record_listbox = tk.Listbox(self.record_frame, height=10)
        self.record_listbox.pack(side=tk.LEFT)
        
        self.fetch_records_button = tk.Button(self.record_frame, text="Fetch Records", command=self.fetch_records)
        self.fetch_records_button.pack(side=tk.LEFT, padx=10)
        
        # Insert Frame
        self.insert_frame = tk.Frame(self.root)
        self.insert_frame.pack(pady=10)
        
        self.insert_label = tk.Label(self.insert_frame, text="Insert Record (comma-separated values)")
        self.insert_label.pack(side=tk.LEFT, padx=10)
        
        self.insert_entry = tk.Entry(self.insert_frame)
        self.insert_entry.pack(side=tk.LEFT, padx=10)
        
        self.insert_button = tk.Button(self.insert_frame, text="Insert Record", command=self.insert_record)
        self.insert_button.pack(side=tk.LEFT, padx=10)
    
    def fetch_tables(self):
        tables = db_operations.fetch_tables()
        self.table_listbox.delete(0, tk.END)
        for table in tables:
            self.table_listbox.insert(tk.END, table[0])
    
    def fetch_records(self):
        selected_table = self.table_listbox.get(tk.ACTIVE)
        if selected_table:
            records = db_operations.fetch_records(selected_table)
            self.record_listbox.delete(0, tk.END)
            for record in records:
                self.record_listbox.insert(tk.END, record)
        else:
            messagebox.showerror("Error", "No table selected")
    
    def insert_record(self):
        selected_table = self.table_listbox.get(tk.ACTIVE)
        values = self.insert_entry.get().split(',')
        if selected_table and values:
            db_operations.insert_record(selected_table, values)
            messagebox.showinfo("Success", "Record inserted successfully")
        else:
            messagebox.showerror("Error", "No table selected or values provided")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
