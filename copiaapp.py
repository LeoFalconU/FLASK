from flask import Flask, jsonify
import json

with open("API.json", "r") as json_api:
    datos_json = json.load(json_api)
app = Flask(__name__)

# Endpoint HTML
@app.route('/')
def inicio():
    print("Cambio")
    print("Hola")
    return datos_json["3D:RF:09:7F"]

@app.route('/json/<mac>')
def json_data(mac):
    print(mac)
    print(datos_json[mac]["Protocolos"])
    print(datos_json[mac]["VLANs"])
    print(datos_json[mac]["Status"])
    return datos_json[mac]["Name"]

# Endpoint JSON
@app.route('/api/saludo')
def saludo():
    return jsonify({
    "101":{
        "ip": "192.168.0.1",
        "name": "SERV-red",
        "policy": "ONLINE_ONLY",
        "status": "Activo"
    },
    "102":{
        "ip": "192.168.0.2",
        "name": "SERV-blue",
        "policy": "ONLINE_ONLY",
        "status": "Inactivo"
    },
    "103":{
        "ip": "192.168.0.3",
        "name": "SERV-green",
        "policy": "RESTRICTED_NAME",
        "status": "Activo"
    },
    "104":{
        "ip": "192.168.0.4",
        "name": "SERV-yellow",
        "policy": "REQUIRED_STATUS",
        "status": "Activo"
    },
    "105":{
        "ip": "192.168.0.5",
        "name": "SERV-white",
        "policy": "REQUIRED_STATUS",
        "status": "nulo"
    }
})

if __name__ == '__main__':
    app.run(debug=True)

#revisar los tabs e identacion
#Tener cuidado con las rutas, primera es ruta base y la segunda es la ruta de validacion en postman
#si usas flask, usar http en lugar de https
#fijarse en los nombres diferentes para cada funcion a tratar, "saludo" e "inicio"
#Tarea crear otras 10 funciones que interactuen con este diccionario, funciones de tipo .get
#En lugar de mostrar los 5 elemetnos, que muestren un elemento por cada funcion, que sean que agreguen elementos
#Debe ser tal cual el nombre de la funcion,ruta, comentarios de parametros que recibe, que enviam el autor y fecha de modificacion
#Cada una de las funciones debe tener su propia ruta y no pueden compartir nombres entre rutas y funciones

@app.route('/api/saludo')
def funcion1():
    """
    saludo
    /api

    parametros
    return
    autor
    fecha de modificacion
    """
#pasar parametros a traves de la url (postman) o en body , para editar la api en tiempo real



@app.route('/')
def inicio():
    print("Cambio")
    print("Hola")
    return datos_json["3D:RF:09:7F"]

@app.route('/')
def inicio():
    print("Cambio")
    print("Hola")
    return datos_json["3D:RF:09:7F"]

@app.route('/')
def inicio():
    print("Cambio")
    print("Hola")
    return datos_json["3D:RF:09:7F"]

@app.route('/')
def inicio():
    print("Cambio")
    print("Hola")
    return datos_json["3D:RF:09:7F"]

@app.route('/')
def inicio():
    print("Cambio")
    print("Hola")
    return datos_json["3D:RF:09:7F"]