import mysql.connector
import csv
import os
import pandas as pd
#sistema1

def insertar_datos_en_base_de_datos(directorio):
    for archivo in os.listdir(directorio):
        if archivo.endswith('.csv'):
            ruta_archivo = os.path.join(directorio, archivo)
            print("Leyendo archivo:", archivo)
            
            # Leer datos desde el archivo CSV
            datos = pd.read_csv(Enero.csv)
            
            # Iterar sobre los datos y insertar en la base de datos
            cursor = conexion.cursor()
            for indice, fila in datos.iterrows():
                # Suponiendo que las columnas son 'columna1', 'columna2', 'columna3', etc.
                consulta = "INSERT INTO nombre_tabla (columna1, columna2, columna3) VALUES (%s, %s, %s)"
                valores = (fila['columna1'], fila['columna2'], fila['columna3'])
                cursor.execute(consulta, valores)
            
            conexion.commit()
            cursor.close()
            print(f"Datos insertados en la tabla desde el archivo {archivo}")

# Directorio donde se encuentran los archivos CSV
directorio = '/ruta/a/tu/directorio/csv'

# Llamar a la función para insertar datos en la base de datos desde archivos CSV
insertar_datos_en_base_de_datos(directorio)

# Cerrar la conexión a la base de datos
conexion.close()



#Sistema DOS


# Conectar a la base de datos MySQL
conexion = mysql.connector.connect(
    
            host='localhost',
            database='gestion_clientes',
            user='root',
            password='Wily20@4133.'
)

# Verificar si la conexión fue exitosa
if conexion.is_connected():
    print("Conexión exitosa a la base de datos")

    # Función para agregar un nuevo cliente
    def agregar_cliente(nombre, apellido, email, telefono):
        cursor = conexion.cursor()
        consulta = "INSERT INTO clientes (nombre, apellido, email, telefono) VALUES (%s, %s, %s, %s)"
        datos = (nombre, apellido, email, telefono)
        cursor.execute(consulta, datos)
        conexion.commit()
        print("Cliente agregado correctamente")

    # Función para obtener todos los productos
    def obtener_productos():
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        return cursor.fetchall()

    # Ejemplo de uso:
    # Agregar un nuevo cliente
    agregar_cliente("Juan", "Pérez", "juan@example.com", "123456789")
    agregar_cliente("Wilian", "Pérez", "juan@example.com", "123456789")

    # Obtener todos los productos y mostrarlos
    productos = obtener_productos()
    print("Lista de Productos:")
    for producto in productos:
        print(producto)

    # Cerrar la conexión a la base de datos
    conexion.close()
else:
    print("Error: No se pudo conectar a la base de datos")
