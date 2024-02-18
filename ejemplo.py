def funcion(palabra):
    l=['a','e','i','o','u']
    contador=0
    for letra in palabra:
        if letra.lower() in l:
            contador+=1
    return contador


print(funcion('Anita washes the tub'))