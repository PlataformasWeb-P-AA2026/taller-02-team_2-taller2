from fastapi import FastAPI
import psycopg2
from base import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT  # <--- importamos

app = FastAPI()

def conectar():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

@app.get("/empleados")
def empleados():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT nombre, departamento, salario FROM empleados")
    datos = cur.fetchall()
    conn.close()

    return [{"nombre": d[0], "departamento": d[1], "salario": d[2]} for d in datos]
