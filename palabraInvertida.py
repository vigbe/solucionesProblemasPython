print("""   Bienvenido a una nueva clase de lenguaje
            Hoy aprenderemos los palindromos y cuando una
            palabra lo es, ingrese los datos solicitados para enteder esto""")
palabra = input("ingrese una palabra:")
palabra_invertida = palabra[::-1]
print(f"su palabra al reves se escribe: {palabra_invertida}")

if(palabra==palabra_invertida):
    print("su palabra es un palindromo")
else:
    print("lamentablemente su palabra no es un palindromo")

total_caracteres = len(palabra)
print(f"Tambien es bueno que sepa que su palabra contenia: {total_caracteres} letras")    