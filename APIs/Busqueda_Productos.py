from flask import Flask, jsonify, request, abort, render_template
import psycopg2

app = Flask(__name__)

table_name = 'public.inventario'
columna_principal = 'nombre'

'''Configuro la conexión a PostgreSQL'''
connection = psycopg2.connect(host='monorail.proxy.rlwy.net', user='postgres', password='BzZBcWrNubzzjWJNqnaMIswyAxAkuQrK',
                              database='railway', port='51772')


'''Usamos el decorador @app.route para enrutar a la URL principal. La función index()
   se ejecutará cuando un cliente haga una solicitud GET en la ruta "/productos".'''

@app.route('/')
def index():
    return render_template('index.html')

'''Usamos el decorador @app.route para enrutar a la URL '/productos'. La función get_productos()
   se ejecutará cuando un cliente haga una solicitud GET en la ruta "/productos".'''

@app.route('/productos', methods=['GET'])
def get_productos():

    cur = connection.cursor() # Creamos un cursor para ejecutar comandos SQL en la base de datos.

    termino_busqueda = request.args.get('search') # Obtenemos el término de búsqueda del parámetro de consulta 'search'.

    # Construimos la consulta SQL para seleccionar el o los productos solicitados:
    if termino_busqueda:
        consulta = f"SELECT * FROM {table_name} WHERE {columna_principal} ILIKE '%{termino_busqueda}%'" # Este bloque sólo se ejecutará si termino_busqueda es una cadena no vacía.
    else:
        consulta = f'SELECT * FROM {table_name}' # Este bloque sólo se ejecutará si termino_busqueda es None o una cadena vacía.
    
    cur.execute(consulta) # Ejecución de consulta para que devuelva todos los productos.
    productos = cur.fetchall() # Almacenamiento de resultados de la consulta en la var productos en forma de lista de tuplas, en la que cada tupla describe a un producto en particular.
    cur.close() # Cerramos el cursor y liberamos cualquier recurso en memoria asociado a él.

    return jsonify(productos) # Convertimos los resultados de la consulta a un formato JSON para devolverlos con return.


'''La función subir_producto()se ejecutará cuando un cliente haga
   una solicitud POST (agregar un producto a la base para venerlo) en la ruta "/productos".'''

@app.route('/productos', methods=['POST'])
def subir_producto():

    data = request.get_json() # Obtenemos los datos del producto del cuerpo de la solicitud.

    # Verificamos y validamos que estén todos los datos obligatorios y bien pasados:
    if 'nombre' not in data or 'precio' not in data:
        abort(400, 'Se requieren el nombre y el precio del producto')

    # Verificamos si el precio es un número positivo
    if not isinstance(data['precio'], (int, float)) or data['precio'] <= 0:
        abort(400, 'El precio del producto debe ser un número positivo')
    
    cur = connection.cursor() #  Creamos un cursor para ejecutar comandos SQL en la base de datos.
    # Ejecución de consulta para que agregue el producto:
    cur.execute(f"INSERT INTO {table_name} (nombre, precio) VALUES (%s, %s)", (data['nombre'], data['precio']))
    connection.commit() # Guardamos los cambios en la Base de Datos.
    cur.close() # Cerramos el cursor y liberamos cualquier recurso en memoria asociado a él.

    # Devolvemos una respuesta exitosa:
    return jsonify({'message': 'Producto creado exitosamente'}), 201


'''Iniciamos la app'''
if __name__ == '__main__':
    app.run(debug=True)