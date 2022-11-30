# Se importan las librerias necesarias

from pymongo import MongoClient
MONGO_URL = 'mongodb://localhost'
location = MongoClient(MONGO_URL)
database = location['COVID']
collection = database['CASOS']

# Se imprimen las opciones para que el usuario escoja.

print("OPCIONES")
print("         ")
print("1. Cuantos casos se registraron en Bogotá")
print("2. Cuantos casos se recuperaron en Bogotá")
print("3. Cual fue la ciudad que más se recuperaron")
print("4. Cual fue la ciudad que más se recuperaron siendo mujeres.")
print("5. Cuantos fallecidos que fueron mujeres y mayores de 50 años.")
print("6. Cuantos fallecidos que fueron hombres y menores de 50 años.")
print("7. Cuantos casos fueron por personas del extranjero")
print("8. Cuantos casos se registraron en Antioquía, menores de 30 años y por persona extranjeras")
print("9. Cuantos casos se registraron por personas de España")
print("10. Cuantos casos se registraron por personas de edad entre 20 y 50 años")

# Se crea la bandera para el ciclo while.

cuestion = True

# Se crea el menu para escoger las opciones.

while cuestion:  
    query = int(input("Seleccione la opcion que desea consultar"))
    if query == 1:
        fuction_one = collection.count_documents({})
    if query == 2:
        function_two()
    if query == 3:
        function_three()
    if query == 4:
        function_four()
    if query == 5:
        function_five()
    if query == 6:
        function_six()
    if query == 7:
        function_seven()
    if query == 8:
        function_eigth()
    if query == 9:
        function_nine()
    if query == 10:
        function_ten()