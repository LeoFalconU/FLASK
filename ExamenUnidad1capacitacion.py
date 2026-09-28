# 1. Lista de IPs disponibles 
ips = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.30",
    "192.168.1.40",
    "192.168.1.50"
]

# 2. Diccionario principal con diccionarios anidados (Apuntes del 10/Sep)
red = {
    "101": {
        "device_name": "Router Principal",
        "ip": ips[0],
        "policy": "ALLOW_ALL",
        "status": "Activo"
    },
    "102": {
        "device_name": "Switch Core",
        "ip": ips[1],
        "policy": "ALLOW_ALL",
        "status": "Activo"
    },
    "103": {
        "device_name": "Servidor Web",
        "ip": ips[2],
        "policy": "REQUIRED_IP", # IP esperada: 192.168.1.30
        "status": "Activo"
    },
    "104": {
        "device_name": "AP Piso 1",
        "ip": ips[3],
        "policy": "BLOCK_IP",   # IP bloqueada: 192.168.1.40
        "status": "Inactivo"
    },
    "105": {
        "device_name": "Firewall",
        "ip": ips[4],
        "policy": "BLOCK_IP",   # IP bloqueada: 192.168.1.40
        "status": "Inactivo"
    }
}


def mostrar_dispositivos(dispositivos):

    def mostrar_dispositivos(red_dict):

    for dev_id, info in red_dict.items():
        print(f"ID: {dev_id}")
        print(f"Nombre: {info.get('device_name')}")
        print(f"IP: {info.get('ip')}")
        print(f"Política: {info.get('policy')}")
        print(f"Estado: {dispositivos['status']}")
        res = validar_politica(dispositivos)
        print(f"Resultado: {res}")
    resultado = validar_politica
        print(f"Resultado: {resultado}")
            if('ALLOW_ALL' {resultado}):
                return "Configuracion Valida"



    HAcer el examen con el codigo y tratar de reducir lineas lo mas posible