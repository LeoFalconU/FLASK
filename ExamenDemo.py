# 1. Lista de IPs disponibles (Apuntes del 03/Sep)
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

# FUNCIÓN 2: Validar la política del dispositivo
def validar_politica(dispositivo):
    politica = dispositivo.get("policy")
    ip = dispositivo.get("ip")
    
    if politica == "ALLOW_ALL":
        return "Configuración válida"
    elif politica == "BLOCK_IP":
        # Bloquea específicamente la IP 192.168.1.40
        if ip == "192.168.1.40":
            return "Configuración inválida (IP bloqueada)"
        return "Configuración válida"
    elif politica == "REQUIRED_IP":
        # Requiere exactamente la IP 192.168.1.30
        if ip == "192.168.1.30":
            return "Configuración válida"
        return "Configuración inválida (IP incorrecta)"
    else:
        return "Configuración inválida"

# FUNCIÓN 1: Mostrar los datos de los dispositivos
def mostrar_dispositivos(red_dict):
    for dev_id, info in red_dict.items():
        print(f"ID: {dev_id}")
        print(f"Nombre: {info.get('device_name')}")
        print(f"IP: {info.get('ip')}")
        print(f"Política: {info.get('policy')}")
        print(f"Estado: {info.get('status')}")
        
        # Validamos usando la Función 2
        resultado = validar_politica(info)
        print(f"Resultado: {resultado}")
        print("-" * 30)

# FUNCIÓN 3: Generar estadísticas finales de la red
def generar_resumen(red_dict):
    activos = 0
    inactivos = 0
    validos = 0
    invalidos = 0
    
    for info in red_dict.values():
        # Contador de estado
        if info.get("status") == "Activo":
            activos += 1
        else:
            inactivos += 1
            
        # Contador de validaciones
        res = validar_politica(info)
        if res == "Configuración válida":
            validos += 1
        else:
            invalidos += 1
            
    print("RESUMEN DE LA RED")
    print(f"Dispositivos Activos: {activos}")
    print(f"Dispositivos Inactivos: {inactivos}")
    print(f"Configuraciones Válidas: {validos}")
    print(f"Configuraciones Inválidas: {invalidos}")

# --- EJECUCIÓN DEL PROGRAMA ---
mostrar_dispositivos(red)
generar_resumen(red)