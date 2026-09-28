ips = ['10.0.0.10','10.0.0.20','10.0.0.30','10.0.0.40','10.0.0.50']

serv ={
    "101":{
        "ip": ips[0],
        "name": "SERV-red",
        "policy": "ONLINE_ONLY",
        "status": "Activo"
    },
    "102":{
        "ip": ips[1],
        "name": "SERV-blue",
        "policy": "ONLINE_ONLY",
        "status": "Inactivo"
    },
    "103":{
        "ip": ips[2],
        "name": "SERV-green",
        "policy": "RESTRICTED_NAME",
        "status": "Activo"
    },
    "104":{
        "ip": ips[3],
        "name": "SERV-yellow",
        "policy": "REQUIRED_STATUS",
        "status": "Activo"
    },
    "105":{
        "ip": ips[4],
        "name": "SERV-white",
        "policy": "REQUIRED_STATUS",
        "status": "nulo"
    }
}

#print(serv)

"""
si es online only y esta inactivo = X
si es online only y esta activo = /
si es restricted name y es el verde = X
si es restricted name y el nombre es cualquier otro = /
si es required status y el estatus es activo = /
si es required estatus y el estatos es nulo = X
"""

def validar_politica(servidor):
    politica = servidor.get("policy")
    ip =servidor.get("ips")
    nombre =servidor.get("name")
    estatus = servidor.get("status")


    if politica == "ONLINE_ONLY" and estatus == "Activo":
        return "Configuracion valida"
    elif politica =="RESTRICTED_NAME":
        if nombre == "SERV-green":
            return "Configuracion invalida (Nombre Bloqueado)"
        return "Configuracion valida"
    elif politica == "REQUIRED_STATUS":
        if estatus =="Activo":
            return "Configuracion valida"
        return "Configuracion invalida (Status nulo)"
    else:
        return "Configuracion invalida"
#switch case (revisar)

#validar_politica(serv)

"""
ID:101
nombre: serv-nombre
ip: 000.000.00.00
politica: policy
status: active/inactive
"""

def mostrar_servidores(serv_dict):
    for serv_id, info in serv_dict.items():
        print(f"ID: {serv_id}")
        print(f"Nombre:{info.get('name')}")
        print(f"IP:{info.get('ip')}")
        print(f"Politica: {info.get('policy')}")
        print(f"Estado: {info.get('status')}")
        resultado= validar_politica(info)
        print(f"Resultado: {resultado}")
        print(f"      ")

#mostrar_servidores(serv)


def generar_resumen(serv_dict):
    activos =0
    inactivos= 0
    validos = 0
    invalidos =0
    for info in serv_dict.values():
            if info.get("status") == "Activo":
                activos +=1
            else:
                inactivos += 1
            res = validar_politica
            #if validar_politica() == "Configuracion valida":
            if res == "Configuracion valida":
                validos += 1
            else:
                invalidos += 1
    print("++Resumen de Servidroes++")
    print(f"Dispositivos activas:{activos}")
    print(f"Dispositivos inactivas:{inactivos}")
    print(f"Configuraciones validas: {validos}")
    print(f"Configuraciones invalidas:{invalidos}")



mostrar_servidores(serv)
generar_resumen(serv)




