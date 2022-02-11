import numpy as np
def llenarJugadores(  arregloRut, arregloNombre, arregloPeso, arregloEstatura, arregloPuesto   ):
    for i in range(3):
        rut = input("ingrese el rut: ")
        nombre =  input("ingrese el nombre: ")
        peso= float(input("ingrese el peso: "))
        estatura = float( input("ingrese la estatura: "))
        puesto =  input("ingrese el puesto (1:delantero 2:medio  3:defensa  4:arquero): ")
        arregloRut[i] = rut
        arregloNombre[i] = nombre
        arregloPeso[i] = peso
        arregloEstatura[i]=estatura
        arregloPuesto[i] = puesto
def buscarJugadores(cedula, arregloRut, arregloNombre, arregloPeso, arregloEstatura, arregloPuesto ):
    posicion=-1
    for i in range(3):
        if( arregloRut[i]==cedula):
            posicion=i
            print(f"nombre: {arregloNombre[i]}")
            break
    return  posicion    
def situacionImc(  variablepeso , variableestatura ):
    varimc= (variablepeso / (variableestatura * variableestatura) )
    resultado="sin definir"
    print(varimc)
    if(varimc<18.5):
        resultado ="bajo peso" 
    if(varimc>=18.5 and varimc<=24.9):
        resultado ="adecuado" 
    if(varimc>=25 and varimc<=29.9):
        resultado ="sobrepeso" 
    if(varimc>=30 and varimc<=34.9):
        resultado ="Obesidad grado 1" 
    if(varimc>=35 and varimc<=39.9):
        resultado ="Obesidad grado 2" 
    if(varimc>=40):
        resultado ="Obesidad grado 3" 
        return resultado
arregloRut = np.empty(3, dtype='object')
arregloNombre = np.empty(3, dtype='object')
arregloPeso = np.empty(3, dtype='float')
arregloEstatura=np.empty(3, dtype='float')
arregloPuesto = np.empty(3,dtype='int')
while(True):
    print("1.- Llenar la plantilla de jugadores")
    print("2.- Buscar jugador")
    print("3.- Mostrar Estado nutricional del jugador")
    print("4.- Salir")
    opcion = int(input("ingrese su opción: "))
    if (opcion==1):
        llenarJugadores(arregloRut, arregloNombre, arregloPeso, arregloEstatura, arregloPuesto)
    if (opcion==2):
        cedula = input("ingrese el rut del jugador que desea buscar:  ")
        numeroPosicion = buscarJugadores(cedula, arregloRut, arregloNombre, arregloPeso, arregloEstatura, arregloPuesto)
        print(f"elemento en posicion: {numeroPosicion}")
    if (opcion==3):
        cedula = input("ingrese el rut del jugador que desea mostrar su estado nutricional:  ")
        numeroPosicion = buscarJugadores(cedula, arregloRut, arregloNombre, arregloPeso, arregloEstatura, arregloPuesto)
        if(numeroPosicion>=0):
            estado = situacionImc( arregloPeso[numeroPosicion], arregloEstatura[numeroPosicion])
            print(estado)
    if (opcion==4):
        break