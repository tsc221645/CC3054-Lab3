'''
Universidad del Valle de Guatemala 
Facultad de Ingenieria
Organizacion de Computadoras y Assembler
Eric Barrera
Ana Laura Tschen
22/02/2023
'''

#Ingreso de Numeros hexadecimal ----------------------------------------------------
def HextoDecimal():

    n_hexa = str(input("Ingrese el numero hexadecimal: "))

    numbers = list(n_hexa)
    numbers.reverse()
    val2 = 0
    hex_dict = {"0": 0,"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "A":10, "B": 11, "C": 12, "D": 13, "E":14, "F": 15} 

    for i in range(3):
        if numbers[i] in hex_dict:
            val1 = hex_dict[numbers[i]] * (16**(i))
            val2 = val2 + val1
    print("\n El numero ", n_hexa," es igual ", val2, " en decimal.\n")

#Ingreso de numeros decimal ------------------------------------------------------------------
def decimalToHex():

    #diccionario 
    hex_dict = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7",
     8:"8", 9:"9" , 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F" } 

    n_dec = int(input("Ingrese el numero en decimal: "))
    pos = []
    final_hex = []
    b1 = 16**2
    b2 = 16
    b3 = 1

    if n_dec >= 256:
        p1 = int(n_dec / b1)
        pos.append(p1)
        p2 = int((n_dec - (p1*b1))/b2)
        pos.append(p2)
        p3 = int(((n_dec-(p1*b1))-(p2*b2)))
        pos.append(p3)
    elif n_dec < 256 and n_dec >= 16:
        p2 = int(n_dec/b2)
        pos.append(0)
        pos.append(p2)
        p3 = int((n_dec - (b2*p2)))
        pos.append(p3)
    elif n_dec <= 15:
        for i in range(2):
            pos.append(0)
        pos.append(n_dec)
    for i in range(3):
        if pos[i] in hex_dict:
            final_hex.append(hex_dict[pos[i]])
    print("\nEl numero ", n_dec, "es igual a ",(''.join(final_hex)), " en hexadecimal\n")

#-------------------------------------------------------------------------------------------------------------
def menu():
    print("---------------------------------------\n"
          "       CONVERTIDOR  HEX <-> DEC     \n"
          "---------------------------------------")
    opcion = 0
    while opcion != 1 or opcion != 2:
        opcion = int(input("ingrese la opcion que desea:\n"
        "1. Hex -> Dec\n"
        "2. Dec -> Hex\n"
        "Opcion: "))
        if opcion == 1:
            HextoDecimal()
        elif opcion == 2:
            decimalToHex()
menu()