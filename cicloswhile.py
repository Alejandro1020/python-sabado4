observador=100

print('Menu')
print('0.SALIR')
print('1.SALUDAR')
print('2.DESPEDIR')

while observador !=0:
    observador=int(input('Digite una opcion'))
    if observador==0:
        break
    elif observador==1:
        print('Buenos dias')
    elif observador==2:
        print('Hasta luego')  
    else:
        print('Digite una opcion correcta')      

    
else:
    print('termino')    



