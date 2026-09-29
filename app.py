from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Carga del archivo API.json con manejo de excepciones por si no existe en el entorno local
try:
    with open("API.json", "r") as json_api:
        datos_json = json.load(json_api)
except FileNotFoundError:
    datos_json = {"3D:RF:09:7F": "Dispositivo por defecto"}

# Diccionario global de servidores para manipular en tiempo real
servidores_db = {
    "101": {
        "ip": "192.168.0.1",
        "name": "SERV-red",
        "policy": "ONLINE_ONLY",
        "status": "Activo"
    },
    "102": {
        "ip": "192.168.0.2",
        "name": "SERV-blue",
        "policy": "ONLINE_ONLY",
        "status": "Inactivo"
    },
    "103": {
        "ip": "192.168.0.3",
        "name": "SERV-green",
        "policy": "RESTRICTED_NAME",
        "status": "Activo"
    },
    "104": {
        "ip": "192.168.0.4",
        "name": "SERV-yellow",
        "policy": "REQUIRED_STATUS",
        "status": "Activo"
    },
    "105": {
        "ip": "192.168.0.5",
        "name": "SERV-white",
        "policy": "REQUIRED_STATUS",
        "status": "nulo"
    }
}

# ==========================================
# RUTAS BASE EXISTENTES
# ==========================================

@app.route('/')
def inicio():
    """
    Nombre: inicio
    Ruta: /
    Parametros: Ninguno
    Retorna: Informacion de la MAC por defecto desde datos_json
    Autor: Equipo de Desarrollo
    Fecha de modificacion: 28/09/2026
    """
    print("Cambio")
    print("Hola")
    return datos_json.get("3D:RF:09:7F", "No encontrado")


@app.route('/json/<mac>')
def json_data(mac):
    """
    Nombre: json_data
    Ruta: /json/<mac>
    Parametros: mac (string en URL)
    Retorna: Nombre del dispositivo asignado a la MAC
    Autor: Equipo de Desarrollo
    Fecha de modificacion: 28/09/2026
    """
    if mac in datos_json:
        print(mac)
        print(datos_json[mac].get("Protocolos"))
        print(datos_json[mac].get("VLANs"))
        print(datos_json[mac].get("Status"))
        return datos_json[mac].get("Name", "Sin nombre")
    return jsonify({"error": "MAC no encontrada"}), 404


@app.route('/api/saludo')
def saludo():
    """
    Nombre: saludo
    Ruta: /api/saludo
    Parametros: Ninguno
    Retorna: Diccionario completo de todos los servidores
    Autor: Equipo de Desarrollo
    Fecha de modificacion: 28/09/2026
    """
    return jsonify(servidores_db)


# ==========================================
# 5 FUNCIONES: OBTENER UN ELEMENTO ESPECÍFICO
# ==========================================

@app.route('/api/servidor/101')
def obtener_servidor_101():
    """
    Nombre: obtener_servidor_101
    Ruta: /api/servidor/101
    Parametros: Ninguno
    Retorna: Informacion individual del servidor 101
    Autor: Equipo de Desarrollo
    Fecha de modificacion: 28/09/2026
    """
    return jsonify({"101": servidores_db.get("101", "No encontrado")})


@app.route('/api/servidor/102')
def obtener_servidor_102():
    """
    Nombre: obtener_servidor_102
    Ruta: /api/servidor/102
    Parametros: Ninguno
    Retorna: Informacion individual del servidor 102
    Autor: Equipo de Desarrollo
    Fecha de modificacion: 28/09/2026
    """
    return jsonify({"102": servidores_db.get("102", "No encontrado")})


@app.route('/api/servidor/103')
def obtener_servidor_103():
    """
    Nombre: obtener_servidor_103
    Ruta: /api/servidor/103
    Parametros: Ninguno
    Retorna: Informacion individual del servidor 103
    Autor: Equipo de Desarrollo
    Fecha de modificacion: 28/09/2026
    """
    return jsonify({"103": servidores_db.get("103", "No encontrado")})


@app.route('/api/servidor/104')
def obtener_servidor_104():
    """
    Nombre: obtener_servidor_104
    Ruta: /api/servidor/104
    Parametros: Ninguno
    Retorna: Informacion individual del servidor 104
    Autor: Equipo de Desarrollo
    Fecha de modificacion: 28/09/2026
    """
    return jsonify({"104": servidores_db.get("104", "No encontrado")})


@app.route('/api/servidor/105')
def obtener_servidor_105():
    """
    Nombre: obtener_servidor_105
    Ruta: /api/servidor/105
    Parametros: Ninguno
    Retorna: Informacion individual del servidor 105
    Autor: Equipo de Desarrollo
    Fecha de modificacion: 28/09/2026
    """
    return jsonify({"105": servidores_db.get("105", "No encontrado")})


# ==========================================
# 5 FUNCIONES: FILTRAR, AGREGAR, MODIFICAR Y ELIMINAR
# ==========================================

@app.route('/api/servidores/filtrar/estado/<estado>')
def filtrar_por_estado(estado):
    """
    Nombre: filtrar_por_estado
    Ruta: /api/servidores/filtrar/estado/<estado>
    Parametros: estado (string recibido por URL, ej: Activo, Inactivo, nulo)
    Retorna: Diccionario con los servidores que coinciden con el estado
    Autor: Equipo de Desarrollo
    Fecha de modificacion: 28/09/2026
    """
    resultado = {
        key: val for key, val in servidores_db.items()
        if val.get("status").lower() == estado.lower()
    }
    return jsonify(resultado)


@app.route('/api/servidores/filtrar/politica/<politica>')
def filtrar_por_politica(politica):
    """
    Nombre: filtrar_por_politica
    Ruta: /api/servidores/filtrar/politica/<politica>
    Parametros: politica (string recibido por URL, ej: ONLINE_ONLY, REQUIRED_STATUS)
    Retorna: Diccionario con los servidores que coinciden con la politica
    Autor: Equipo de Desarrollo
    Fecha de modificacion: 28/09/2026
    """
    resultado = {
        key: val for key, val in servidores_db.items()
        if val.get("policy").lower() == politica.lower()
    }
    return jsonify(resultado)


@app.route('/api/servidores/agregar/<id_servidor>/<ip>/<name>/<policy>/<status>')
def agregar_servidor(id_servidor, ip, name, policy, status):
    """
    Nombre: agregar_servidor
    Ruta: /api/servidores/agregar/<id_servidor>/<ip>/<name>/<policy>/<status>
    Parametros: id_servidor, ip, name, policy, status (recibidos via URL)
    Retorna: Confirmacion y el servidor agregado al diccionario en tiempo real
    Autor: Equipo de Desarrollo
    Fecha de modificacion: 28/09/2026
    """
    servidores_db[id_servidor] = {
        "ip": ip,
        "name": name,
        "policy": policy,
        "status": status
    }
    return jsonify({
        "mensaje": "Servidor agregado correctamente",
        "id": id_servidor,
        "datos": servidores_db[id_servidor]
    })


@app.route('/api/servidores/actualizar_estado/<id_servidor>/<nuevo_estado>')
def actualizar_estado(id_servidor, nuevo_estado):
    """
    Nombre: actualizar_estado
    Ruta: /api/servidores/actualizar_estado/<id_servidor>/<nuevo_estado>
    Parametros: id_servidor, nuevo_estado (recibidos via URL)
    Retorna: Confirmacion del cambio de estado del servidor
    Autor: Equipo de Desarrollo
    Fecha de modificacion: 28/09/2026
    """
    if id_servidor in servidores_db:
        servidores_db[id_servidor]["status"] = nuevo_estado
        return jsonify({
            "mensaje": f"Estado del servidor {id_servidor} actualizado",
            "servidor": servidores_db[id_servidor]
        })
    return jsonify({"error": "ID de servidor no encontrado"}), 404


@app.route('/api/servidores/eliminar/<id_servidor>')
def eliminar_servidor(id_servidor):
    """
    Nombre: eliminar_servidor
    Ruta: /api/servidores/eliminar/<id_servidor>
    Parametros: id_servidor (string en URL)
    Retorna: Confirmacion de la eliminacion del elemento en tiempo real
    Autor: Equipo de Desarrollo
    Fecha de modificacion: 28/09/2026
    """
    if id_servidor in servidores_db:
        eliminado = servidores_db.pop(id_servidor)
        return jsonify({
            "mensaje": f"Servidor {id_servidor} eliminado con exito",
            "datos_eliminados": eliminado
        })
    return jsonify({"error": "ID de servidor no encontrado"}), 404


if __name__ == '__main__':
    # Flask corre por defecto en HTTP (http://127.0.0.1:5000/)
    app.run(debug=True, port=5000)