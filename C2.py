week=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
out=[]
for i,day in enumerate (week):
    #print(i,day)
    if(day=='Sabado' or day=='Domingo'): 
        out.append(i)
print(out)

print([week.index('Sabado'),week.index('Domingo')])