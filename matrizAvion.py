def mortrarAsientos(lista):
	print("\n\tASIENTOS\n")
	aux =" "
	for i in range(1,len(lista)+1):
		aux = aux + str(lista[i-1])+ "  "
		if(i%6==0):
			print(aux)
			print()
			aux = " "
		if(i%31==0):
			print("-----------------------")
	print()	

def comprarAsiento(asientos, usuarios):
	nombrePasajero = input("Ingrese su nombre: ")
	rutPasajero = input("Ingrese su rut sin guion ni digito verificador: ")
	telefonoPasajero = input("Ingrese su telefono: ")
	bancoPasajero = input("Ingrese su banco: ")
	opcion = int(input("Que asiento desea: "))
	while(opcion>42 or opcion<=0):
		print("\nIngrese un asiento valido")
		opcion = int(input("Que asiento desea: "))
	#calculo de costo de reserva
	costo = 0
	if(opcion<=30):
		costo = 789000
		if(bancoPasajero=="bancoDuoc"):
			costo = costo-((costo/100)*15)
	else:
		costo = 240000
		if(bancoPasajero=="bancoDuoc"):
			costo = costo-((costo/100)*15)
			
	if(rutPasajero in usuarios[0][opcion-1]):
		print("Ya esta registrado dentro del avion")
	else:
		contador = 0
		for i in asientos:
			if(opcion==i):
				print("\nSe ha comprado el asiento",opcion,"por un valor de $",costo,"\n")
				asientos[i-1]="X"
				usuarios[0][i-1] = nombrePasajero
				usuarios[1][i-1] = rutPasajero
				usuarios[2][i-1] = telefonoPasajero
				usuarios[3][i-1] = bancoPasajero
				usuarios[4][i-1] = costo
				return True
				break
			else:
				contador=contador+1
				
	if(contador==len(asientos)):
		print("\nError!: El asiento esta utilizado\n")
		return False
		
def anularVuelo(asientos, usuarios):
	rut = input("Ingrese su rut: ")
	opcion = int(input("Ingrese su asiento: "))
	if(rut not in usuarios[0]):
		print("\nError!: Usted no esta registrado dentro del avionaaa\n")
	else:
		if(asientos[opcion-1]=="X" and usuarios[0][opcion-1]!=opcion): #el rut y el asiento calzan
			print("\nSe ha anulado la reserva para el asiento",opcion,"para el usuario",usuarios[1][opcion-1])
			asientos[opcion-1] = opcion  #borrar los datos de la matriz asientos
			usuarios[opcion-1] = opcion  #borrar los datos de la matriz usuario
		else:
			print("\nError!: los datos ingresados no estan registrados dentro del avion\n")

def mostrarUsuariosAsientos(asientos,usuarios):
	for i in range(1,len(asientos)+1):
		if(usuarios[0][i-1]!=" "):
			print("El asiento:",i,"esta utilizado por:","[",usuarios[0][i-1],"RUT:",usuarios[1][i-1],"Telefono:",usuarios[2][i-1],"Banco:",usuarios[3][i-1],"] el cual pago",usuarios[4][i-1],"por el")
		else:
			print("El asiento:",asientos[i-1],"no esta siendo utilizado")
	print()
	
def modificarPasajero(asientos,usuarios):
	rut = input("Ingrese su rut: ")
	asiento = int(input("Donde esta sentado: "))
	
	if(usuarios[1][asiento-1] == rut):
		if(asientos[asiento-1]=="X"):# el usuario esta registrado dentro del avion
			print("Que datos desea modificar?")
			print("1. Nombre pasajero")
			print("2. Telefono pasajero")
			escoge = int(input("Opcion: "))
			while(escoge<0 or escoge>2):
				print("Escoja una eleccion valida")
				print("1. Nombre pasajero")
				print("2. Telefono pasajero")
				escoge = int(input("Opcion: "))
			if(escoge==1):
				nuevo_nombre= input("Ingrese su nuevo nombre: ")
				usuarios[0][asiento-1] = nuevo_nombre
			elif(escoge==2):
				nuevo_numero = input("Ingrese su nuevo numero" )
				usuarios[2][asiento-1] = nuevo_numero
	else:
		print("\nErrror!: Usted no esta registrado dentro del avion\n")

				#nombres					rut							telefono                       banco
usuarios = [[" " for k in range(1,43)],[" " for k in range(1,43)], [" " for k in range(1,43)], [" " for k in range(1,43)],[" " for k in range(1,43)]]	
asientos = [i for i in range(1,43)]


while(True):
	print("1. Ver asientos disponibles\n")
	print("2. Comprar asiento\n")
	print("3. Anular vuelo\n")
	print("4. Modificar datos de pasajero\n")
	print("5. Mostrar datos de los pasajeros (opcion adicional)\n")
	print("6. Salir")
	opcion = int(input("Opcion: "))
	if(opcion==1):
		mortrarAsientos(asientos)
	elif(opcion==2):
		print("\n\tCOMPRAR ASIENTO")
		comprarAsiento(asientos, usuarios)

	elif(opcion==3):
		print("\n\tANULAR PASAJE")
		anularVuelo(asientos, usuarios)
	elif(opcion==4):
		print("\n\tMODIFICAR DATOS DE USUARIO")
		modificarPasajero(asientos,usuarios)
	elif(opcion==5):
		mostrarUsuariosAsientos(asientos,usuarios)
	if(opcion>=6):
		print("Bye")
		break