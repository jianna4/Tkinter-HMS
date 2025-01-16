import mysql.connector
from mysql.connector import Error
from connection import create_connection


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


          