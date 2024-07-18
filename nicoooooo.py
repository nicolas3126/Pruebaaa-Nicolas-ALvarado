import random
def generar_sueldos():
    sueldos=[]
    for _ in range(10):
        sueldo = random.randint(300000,2500000)
        sueldos.append(sueldo)
    return sueldos
def total(sueldos):
    total= sum(sueldos)
    return total
def calcular(sueldos):
    descuentos=[]
    sueldos_netos=[]
    for sueldo in sueldos:
        descuento = sueldo * 0.19
        sueldo_neto = sueldo - descuento
        descuentos.append(descuento)
        sueldos_netos.append(sueldo_neto)
    return descuentos, sueldos_netos
def menu():
    trabajadores = {"Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"}
    sueldos=generar_sueldos()
    descuentos, sueldos_netos=calcular(sueldos)
    total_sueldos = total(sueldos)

    
    while True:
        print("____________MENU___________")
        print("(1) -ver sueldos aleatorios")
        print("(2) -ver decuentos")
        print("(3) -ver sueldos netos")
        print("(4) -ver sueldo total de todos los trabajadores")
        print("(5) -ver empleados)")
        print("(6) -Salir del programa")
        print("___________________________")
        ops1=input("Selecciona una opcion: ")
        print("___________________________")
        if ops1=="1":
            print("\nsueldo de los trabajadores")
            for i in range(10):
                print(f"trabajador {i+1}: dinero:{sueldos[i]}")
        elif ops1=="2":
            print("\ndescuentos aplicados: ")
            for i in range(10):
                print(f"\n trabajador {i+1} descuento 7% salud + descuento AFP 12% {descuentos[i]:.2f}" )            
        elif ops1=="3":
           print("\n sueldos netos de los trabajadores : ")
           for i in range(10):
               print(f"trabajador {i+1} total: {sueldos_netos[i]:.2f}")
        elif ops1=="4":
            print(f"\nsueldo total de los trabajadores: {total_sueldos}")
        elif ops1=="5":
            print(trabajadores)         
        elif ops1=="6":
            print("Finalizando Programa...")
            print("Desarrollado por Nicolas Alvarado")
            print("rut 22.000.802-9")
            break
        else:
            print("seleccione una opcion valida")
if __name__=="__main__":
    menu()
