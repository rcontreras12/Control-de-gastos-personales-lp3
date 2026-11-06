from persistencia import cargar_datos, guardar_datos 
from logica import (
    registrar_gasto,
    listar_gastos,
    buscar_gastos,
    modificar_gastos,
    eliminar_gasto,
    reporte_gastos_por_categoria
)

def mostrar_menu():
    print("\n============================")
    print(" CONTROL DE GASTOS PERSONALES ")
    print(" =============================")
    print("1. Registrar nuevo gasto")
    print("2. Listar todos los gastos")
    print("3. Buscar gastos por categoria")
    print("4. Modificar un gasto")
    print("5. Eliminar un gasto")
    print("6. Total gastadopor categoria")
    print("7. Salir")

def main():
    gastos = cargar_datos()

    while True:
        mostrar_menu()
        try:
            opcion = int(input("\n Seleccione una Opcion (1-7): "))
        except ValueError:
                print("Error: Por Favor ingrese un numero valido entre 1 y 7.")
                continue

        if opcion == 1:
                registrar_gasto(gastos)
                guardar_datos (gastos)
        elif opcion == 2:
                listar_gastos(gastos)
        elif opcion == 3:
                buscar_gastos(gastos)
        elif opcion == 4:
                modificar_gastos(gastos)
                guardar_datos(gastos)
        elif opcion == 5:
                eliminar_gasto(gastos)
                guardar_datos(gastos)
        elif opcion == 6:
                reporte_gastos_por_categoria(gastos)
        elif opcion == 7:
                print("\nGracias por usar el sistema!! Saliendo...")
                break 
        else:
                print("Opcion invalida. Por favor elija un numero del 1 al 7.")

if __name__== "__main__":
    main()
