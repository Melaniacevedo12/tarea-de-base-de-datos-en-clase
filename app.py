from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

# Ruta principal que muestra el formulario
@app.route('/')
def index():
    return render_template('formulario.html')

# Ruta que recibe los datos del formulario
@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    correo = request.form['correo']
    mensaje = request.form['mensaje']

    try:
        # Conectar a PostgreSQL
        conexion = psycopg2.connect(
            host="localhost",
            database="FORMULARIO",
            user="postgres123",
            password="123456"
        )
        # Forzar codificación UTF-8 para aceptar tildes y ñ
        conexion.set_client_encoding('UTF8')

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
