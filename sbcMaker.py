from itertools import product
from collections import Counter
import tkinter as tk

def crearListaDeMedias(listaMedias, listaRangos, valoracionSBC, tipo):
    
    resultado = []
    rangoCompleto = []
    i = 0
    
    rangoCompleto.append(listaRangos[0])

    if len(listaRangos) > 1:
        c = listaRangos[1] - listaRangos[0]
        
        while i <= c - 1:
            rangoCompleto.append(rangoCompleto[i] + 1)
            i += 1
    
    else:
        rangoCompleto.append(listaRangos[0])

    for combo in product(rangoCompleto, repeat = 11 - len(listaMedias)):
        if checkLista(combo, listaMedias, valoracionSBC, tipo) == True:
            resultado.append(list(combo))
    
    i = 0
    while i <= len(resultado) - 1:  
        for media in listaMedias:
            (resultado[i]).append(media)
        i += 1

    solucionesUnicas = []

    for lista in resultado:
        eliminarRepeticiones(lista)
        if lista not in solucionesUnicas:
            solucionesUnicas.append(lista)

    return solucionesUnicas


def checkLista(combo, listaMedias, valoracion, tipo):
  
    suma = 0
    i = 0
    listaNueva = []
    while i <= len(listaMedias) - 1:
        suma = suma + listaMedias[i]
        i += 1
    i = 0
    while i <= len(combo) - 1:
        suma = suma + combo[i]
        i += 1
    
    if tipo == 'Flexible':
        if suma >= valoracion*11 - 3 and suma < valoracion*11 + 5:
            return True
        else:
            return False
    else:
        if suma >= valoracion*11 - 3 and suma <= valoracion*11:
            return True
        else:
            return False

def eliminarRepeticiones(listaMediasNueva):

    #  for i in range(len(listaMediasNueva)):
    #     for j in range(0, len(listaMediasNueva) - i - 1):
    #         if listaMediasNueva[j] > listaMediasNueva[j+1]:
    #             listaMediasNueva[j], listaMediasNueva[j+1] = listaMediasNueva[j+1], listaMediasNueva[j]

    listaMediasNueva.sort()
    return listaMediasNueva


def validarMedias(listaMedias, casillaError):
    
    checkeo = 1
    listaMediasNueva = []

    try:
        for media in listaMedias:
            listaMediasNueva.append(int(media))

        i = 0
        while i < len(listaMediasNueva):
            if listaMediasNueva[i] <= 44 or listaMediasNueva[i] > 99:
                checkeo = 0
            i += 1
    except ValueError:
        casillaError['text'] = ' Ingrese media/s'
        casillaError['fg'] = 'red'
        return False

    if checkeo == 0:
        casillaError['text'] = ' Media/s invalida/s'
        casillaError['fg'] = 'red'
        return False
    
    casillaError['text'] = ' ✓'
    casillaError['fg'] = '#5fad5e'
    return True

def validarValoracion(valoracion, casillaError):
    checkeo = 1
    try:
        valoracion = int(valoracion)
    except ValueError:
        casillaError['text'] = ' Ingrese valoracion'
        casillaError['fg'] = 'red'
        return False
    
    if valoracion <= 45 or valoracion > 99:
        checkeo = 0

    if checkeo == 0:
        casillaError['text'] = ' Valoracion invalida'
        casillaError['fg'] = 'red'
        return False

    casillaError['text'] = ' ✓'
    casillaError['fg'] = '#5fad5e'
    return True

def validarRango(rango, casillaError, valoracion):
    checkeo = 1
    try:
        valoracion = int(valoracion)
    except ValueError:
        return False
    try:
        if len(rango) != 1:
            rango[0] = int(rango[0])
            rango[1] = int(rango[1])
            if rango[0] >= rango[1]:
                checkeo = 0
            if rango[0] <= 44:
                checkeo = 0
            if rango[1] > 99:
                checkeo = 0  
            if (rango[1] - rango[0]) > 5:
                checkeo = 2
        else:
            rango[0] = int(rango[0])
            if rango[0] <= 44 or rango[0] > 99:
                checkeo = 0
    except ValueError:
        casillaError['text'] = ' Ingrese rango'
        casillaError['fg'] = 'red'
        return False

    if checkeo == 0:
        casillaError['text'] = ' Rango invalido'
        casillaError['fg'] = 'red'
        return False

    if checkeo == 2:
        casillaError['text'] = ' Exceso de rango'
        casillaError['fg'] = 'red'
        return False

    casillaError['text'] = ' ✓'
    casillaError['fg'] = '#5fad5e'
    return True

def validarTipo(tipo, casillaError):

    if tipo == 'Preciso' or tipo == 'Flexible':
        casillaError['text'] = ' ✓'
        casillaError['fg'] = '#5fad5e'
        return True
    else:
        casillaError['text'] = ' Falta tipo'
        casillaError['fg'] = 'red'
        return False

def imprimirResultados(listaMedias,valoracion,rango,tipo):
        
        listaMediasNueva = []
        for media in listaMedias:
            listaMediasNueva.append(int(media))
        
        if len(rango) != 1:
            rango[0] = int(rango[0])
            rango[1] = int(rango[1])
        else:
            rango[0] = int(rango[0])

        listaSoluciones = []    
        listaSoluciones = crearListaDeMedias(listaMediasNueva, rango , int(valoracion),tipo)

        root = tk.Tk()
        root.title('Resultados (' + tipo + ')')
        scrollbar = tk.Scrollbar(root)
        scrollbar.pack( side = tk.RIGHT, fill = tk.Y )

        if len(listaSoluciones) > 1:
            texto = "Se encontraron " + str(len(listaSoluciones)) + " soluciones:"
        elif len(listaSoluciones) == 1:
            texto = "Se encontro " + str(len(listaSoluciones)) +  " solucion:"
        else:
            texto = "No se encontraron soluciones"

        titulo = tk.Label(root, text= texto, anchor='w', bg = '#2c62b8', fg = 'white')
        titulo.pack(side=tk.TOP, fill=tk.X)

        i = 0
        cell = tk.Listbox(root, yscrollcommand = scrollbar.set, bg = '#afb9c9', width = 50)
        while i <= len(listaSoluciones) - 1:
            linea = dict(Counter(listaSoluciones[i]))
            linea = str(linea).replace("{","|").replace("}", "|").replace(",","| |").replace(":"," x").replace('x ','x')
            cell.insert(tk.END, '[+] ' + str(linea))
            i+=1

        cell.pack(side=tk.LEFT, fill=tk.X)
        scrollbar.config( command = cell.yview )
        


def validarResultados(datos,tipo):
    listaDatos = []
    for dato in datos:
        info  = dato[1].get()
        listaDatos.append(info)
    
    tipoDeBusqueda = tipo[0][0].get()

    listaMedias = validarMedias(listaDatos[0].split(','),datos[0][2])
    valoracion = validarValoracion(listaDatos[1], datos[1][2])
    rango = validarRango(listaDatos[2].split('-'), datos[2][2], listaDatos[1])
    tipo = validarTipo(tipoDeBusqueda, tipo[0][1])

    if listaMedias and valoracion and rango and tipo:
        listaMedias = listaDatos[0].split(',')
        valoracion = listaDatos[1]
        rango = listaDatos[2].split('-')
        tipo = tipoDeBusqueda
        
        imprimirResultados(listaMedias, valoracion, rango, tipo)