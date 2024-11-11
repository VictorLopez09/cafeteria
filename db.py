# db.py
import psycopg2
from config import DATABASE

def get_db_connection():
    conn = psycopg2.connect(**DATABASE)
    return conn

def insert_employee(primer_nombre, apellido_paterno, apellido_materno, email, telefono, id_puesto, contrasena_hash):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO EMPLEADOS (primer_nombre, apellido_paterno, apellido_materno, email, telefono, id_puesto, contrasena)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (primer_nombre, apellido_paterno, apellido_materno, email, telefono, id_puesto, contrasena_hash))
    conn.commit()
    conn.close()

def get_employee_by_email(email):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM EMPLEADOS WHERE email = %s", (email,))
        empleado = cursor.fetchone()
    conn.close()
    return empleado
