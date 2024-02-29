import tkinter as tk
from sbcMaker import *
from tkinter import ttk

campos = 'Medias (Ej: 83,84)', 'Valoracion SBC', 'Rango (Ej: 83-86)'

def crearCampos(ventana, campos):

    datos = []
    for campo in campos:

        #Creo una fila
        fila = tk.Frame(ventana, bg = '#afb9c9')
        fila.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        #Creo el campo segun la fila
        textoCampo = tk.Label(fila, width=15, text=campo, anchor='w', bg = '#afb9c9')
        textoCampo.pack(side=tk.LEFT)

        #Creo el campo error segun la fila
        textoError = tk.Label(fila, width=15, text='', anchor='w', bg = '#afb9c9')
        textoError.pack(side=tk.RIGHT)

        #Creo el input segun la fila
        inputCampo = tk.Entry(fila, bg = '#e3e3e3')
        inputCampo.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

        datos.append((campo, inputCampo, textoError))

    return datos

def iniciarApp():
    #Creacion de ventana
    ventana = tk.Tk()
    ventana.title("SBCMaker 2.0")
    ventana.configure(background='#afb9c9')

    #Creo el campo segun la fila
    # titulo = tk.Label(ventana, width=15, text='SBCMaker', anchor='w', bg = '#2c62b8', fg = 'white')
    # titulo.pack(side=tk.TOP, fill=tk.X)

    #Creacion de campos de texto 
    ents = crearCampos(ventana, campos)
    #ventana.bind('<Return>', (lambda event, e=ents: validarResultados(e)))
    
    #Creacion de la fila de la selection box
    fila = tk.Frame(ventana, bg = '#afb9c9')
    fila.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    textoCampo = tk.Label(fila, width=15, text='Tipo de busqueda', anchor='w', bg = '#afb9c9')
    textoCampo.pack(side=tk.LEFT)
    tipoDeBusqueda = ttk.Combobox(fila,width=18, values = ['Flexible' , 'Preciso'])
    tipoDeBusqueda.pack(side=tk.LEFT)
    textoError = tk.Label(fila, width=15, text='', anchor='w', bg = '#afb9c9')
    textoError.pack(side=tk.LEFT)
    datosTipo = []
    datosTipo.append((tipoDeBusqueda, textoError))

    #Advertencia
    advertencia = tk.Label(ventana, text='Un rango grande puede demorar la ejecucion del programa.',bg = 'grey', fg = 'white')
    advertencia.pack(fill=tk.X)

    #Creacion de botones 
    botonConfirmar = tk.Button(ventana, fg = 'white' ,bg = '#2c62b8', text='Confirmar', command=(lambda e=ents: validarResultados(e, datosTipo)))
    botonConfirmar.pack(side=tk.LEFT, padx=5, pady=5)
    botonSalir = tk.Button(ventana, bg = '#b1c9f0', text='Salir', command=ventana.quit)
    botonSalir.pack(side=tk.LEFT, padx=5, pady=5)

    ventana.mainloop()

iniciarApp()