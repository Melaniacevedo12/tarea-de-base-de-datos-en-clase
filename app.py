from flask import Flask, request,jasonify , sang_filet 
import pgsycopg2 
from pgsycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv
app = Flask(__name__)

conexion = psycopg2.connect(
            host="localhost", 
            database="FORMULARIO", # nombre de la base de datos
            user="postgres123", # el usuario por defecto
            password="123456" # la contraseña
        )


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    correo = request.form['correo']
    mensaje = request.form['mensaje']

    try:
        conexion = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
        )
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO mensajes (nombre, apellido, direccion, telefono, correo, mensaje)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nombre, apellido, direccion, telefono, correo, mensaje))
        conexion.commit()
        cursor.close()
        conexion.close()
        return "<h3>✅ Datos guardados correctamente en la base de datos.</h3>"
    except Exception as e:
        return f"<h3>❌ Error al guardar los datos: {e}</h3>"

if __name__ == '__main__':
    app.run(debug=True)