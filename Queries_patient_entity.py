import mysql.connector
from mysql.connector import Error
from connection import create_connection


def insert_patient(id,first_name,last_name,email,phone,address,gender,age):
    conn = create_connection()
    if conn is not None:
      try:
        cursor = conn.cursor()
        query = """INSERT INTO patients (id,first_name,last_name,email,phone,address,gender,age)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

        cursor.execute(query,(id,first_name,last_name,email,phone,address,gender,age))
        conn.commit()
      except Error as e:
          print(f"Error inserting patient:{e}")
      finally:
        cursor.close()
        conn.close()

def get_patients():
    conn = create_connection()
    if conn is not None:
       try:
        cursor = conn.cursor()
        query = "SELECT * FROM patients"
        cursor.execute(query)
        patients = cursor.fetchall()
    
        return patients        
       except Error as e:
            print(f"Error fetching patients:{e}")
            return[]
       finally:
           cursor.close()
           conn.close()


def update_patient(id,first_name, last_name,email,phone,address,gender,age):

    conn = create_connection()
    if conn is not None:
       try:
        cursor = conn.cursor()
        query = "UPDATE patients SET id = %s,first_name=%s,last_name=%s,email=%s,phone=%s,address=%s,gender=%s,age=%s,WHERE id = %s"

        
        cursor.execute(query,(id,first_name, last_name,email,phone,address,gender,age))
        conn.commit()
       except Error as e:
            print(f"Error updating patient:{e}")
       finally:
           cursor.close()
           conn.close()

        
def delete_patient(id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM patients WHERE id = %s"
            cursor.execute(query, (id,))
            conn.commit()
            print("Patient deleted successfully.")
        except mysql.connector.Error as e:
            print(f"Error deleting patient: {e}")
        finally:
            cursor.close()
            conn.close()        

def get_last_patient_id():
   conn = create_connection()
   cursor = conn.cursor()
   query = """
       SELECT MIN(t1.id + 1) AS next_id
       FROM patients t1
       LEFT JOIN patients t2 ON t1.id + 1 = t2.id
       WHERE t2.id IS  NULL"""
   cursor.execute(query)
   next_id = cursor.fetchone()[0]
   cursor.close()
   conn.close()
   return (next_id + 1) if next_id else 1

def treatment(id,medicine_id,quantity,dosage):
    conn = create_connection()
    if conn is not None:
       try:
        cursor = conn.cursor()
        query = "INSERT INTO treatment (id,medicine_id,quantity,dosage) VALUES (%s,%s,%s,%s)"
        cursor.execute(query,(id,medicine_id,quantity,dosage))
        conn.commit()
       except Error as e:
            print(f"Error updating patient:{e}")
       finally:
           cursor.close()
           conn.close()

def patient_treatment_information(id,patient_id,nurse_id,day_of_treatment,treatment_id,symptoms):
   conn=create_connection()
   if conn is not None:
     try:
        cursor = conn.cursor()
        query = "INSERT INTO patient_treatment_information (id,patient_id,nurse_id,day_of_treatment,treatment_id,symptoms) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(id,patient_id,nurse_id,day_of_treatment,treatment_id,symptoms))
        conn.commit()
     except Error as e:
          print(f"Error updating patient:{e}")
     finally:
          cursor.close()
          conn.close()