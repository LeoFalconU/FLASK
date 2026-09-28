"""
d1={
    ip:'172.0.01',
    d_name:'PC#1',
    policy:'Avoid .2, .3.5',
    status:True
},
"""

"""
d1={
    key:value,
    key:value,
    key:value
}
"""
"""
    IPs:
    Device_names:
    Policies:
    Status:
"""

#d1.get(ip)=172....
#values
#items
#update

network_config_2 = {
    "0001": {
        "ip": "192.168.0.1",
        "device": "Switch",
        "policy": "Deny All",
        "status": False,
        "lista": [1,4,6,0,8]
    },
    "0002": {
        "ip": "192.168.0.1",
        "device": "Firewall",
        "policy": "Avoid .2 .3 .4",
        "status": True
    },
    "0003": {
        "ip": "192.168.0.3",
        "device": "Router",
        "policy": "Allow All",
        "status": True
    },
    "0004": {
        "ip": "192.168.0.4",
        "device": "Load Balancer",
        "policy": "Round Robin",
        "status": True
    },
    "0005": {
        "ip": "192.168.0.5",
        "device": "Access Point",
        "policy": "Guest Network Only",
        "status": False
    }
}


print(network_config_2.get("0001"))
#imprime toda la lista

a = [1,2,3, [7.8,1]]
print(a[3])
print(a[3][1])
#imprimir contenido de una lista dentro de otra lista


print (network_config_2.get("0001").get("lista")[2]) #imprime el 6 dentro de la lista del dicionario
#Todo este codigo puede segmentarse para mandar a imprimir una linea mas corta:
contenido = network_config_2.get("0001") 
listaA = contenido.get("lista")
num = listaA[2]
print(num)

print(listaA)

yaEnUso=a.pop(3)
print(yaEnUso)

network_config_2['0006'] = {
    "ip": 1
}
print(network_config_2)

"""
Necesito hace 10 ips
ips:[10ips]
nombres de los dispositivos
dev_names:[10 nombres]
policies: [...]

router:
    policies: .2, .3 .5 , not allowed
    encendido:true



dentro del flujo yo noecesito ver un dicionario
que cada dsipotivio este identificado de forma diferente
dentro de las politicas va asignar ip de acuerdo a la politica (si no puede usar .2 y .6 ejemplo)

tomar los valores para evaluar junto con las politicas
quiero mi primer dispositivo (un router, ejemplo) 
0001:{
    ip:162.168.0.2,
    nombre:router,
    encendido:false
    }

cambiar  los valores requeridos
hacer print de los valores solicitados, 
"""


"""
network_config_2 = {
    "0001": {
        "ip": "192.168.0.1",
        "device": "Switch",
        "policy": ["Ro", "Not Allowed", [0.2, 0.3, 0.5]]
        "status": False,
        "lista": [1,4,6,0,8]
    },}
"""



