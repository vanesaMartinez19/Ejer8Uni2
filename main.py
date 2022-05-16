from ClaseConjunto import Conjunto


def Menu():
    op = 0
    while (op != 4):
        print("ingrese numero")
        print("1-La unión de dos conjuntos")
        print("2-La diferencia de dos conjuntos")
        print("3-Verificar si dos conjuntos son iguales")
        print("4-Salir")
        op = int(input(""))
        if (op == 1):
            print(" la suma de A: y B: es {}",suma)

        elif (op == 2):
            print(" la resta de A: y B: es {}",resta)

        elif (op == 3):
            print(" igualdad de conjuntos entre B y C {} ",igual)




if __name__ == '__main__':

    A = Conjunto(2,3,4,5)
    B = Conjunto(9,6,8)
    C = Conjunto(6,8,9)


    suma = A + B
    resta = A - B
    igual = A == C
    Menu()
