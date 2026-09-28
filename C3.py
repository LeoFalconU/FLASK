nums=['Uno','Dos','Tres','Cuatro','Cinco','Seis','Siete','Ocho','Nueve','Diez']
colors=['Red','Blue','Green','Yellow','Brown','White','Black','Pink','Orange','Purple']

#print(nums)
#colors.append('Cyan')
#colors.extend(['Gray','Cyan'])
#colors.insert(0,'Cyan')
#colors.insert(5,'Gray')
#colors.clear()
#colors.append('Royal Blue')
#print(colors)
#print(colors.pop(0))
#colors.sort(reverse=False)
#colors.sort(reverse=True)
#print(colors)
#colors_1=colors.copy()
#print(colors_1)


"""
for num in nums:
    output=f"[{num}, {colors[nums.index(num)]}]"
    print(output)
"""

#print([nums[0],colors[0]])

"""
for num, color in zip(nums, colors):
    print(f"[{num}, {color}]")

Al usar zip(), emparejas los elementos de ambas listas uno a uno. 
Esto elimina la necesidad de usar nums.index(num), 
lo cual no solo acorta el código, 
sino que también lo hace más rápido (el método index() 
obliga a Python a buscar el elemento desde el principio
 de la lista en cada vuelta del bucle).    
"""

"""
for i, num in enumerate(nums):
    print(f"[{num}, {colors[i]}]")

Si por alguna razón necesitaras usar la posición numérica en tu lógica
(por ejemplo, para imprimir el número de línea), 
la función enumerate() es la mejor opción. 
Te devuelve tanto el índice como el valor al mismo tiempo:
    
"""


#append(val)
#insert(index,val)
#extend(values)
#pop(index).pop()
#clear
#count(val)
#sort()
#reverse()

out=[]
nums.reverse()

for num in nums:
    mix=[num,colors[nums.index(num)]]
#   si son listas iterables

#    mix=f"{num}, {colors[nums.index(num)]}" - son texto, no listas
#   mix=f"[{num}, {colors[nums.index(num)]}]" - es texto, no listas
    out.append(mix)

print(out)

