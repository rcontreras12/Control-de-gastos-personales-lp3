def registrar_gasto(gastos):
    print("---REGISTRE UN NUEVO GASTO---")
    try:
        monto = float(input("ingrese el monto del gasto (puros bs plz): "))
        if monto <= 0:
            print("mi pana eso no es un gasto, i mean, el num debe ser mayor a cero plz")
            return
    except ValueError :
        print("bebe... numeros plz")
        return

    categoria = input("ingrese la categoria del gasto (vease: comida, transporte, servicios): ").strip()
    if not categoria:
        print("esto no puede quedar vacio")
        return

    fecha = input("ingrese la fecha del gasto (DD/MM/AAAA): ").strip()
    if not fecha:
        print("la fecha no puede quedar vacia")
        return

    nuevo_gasto = {
        "monto": monto,
        "categoria": categoria.capitalize(),
        "fecha": fecha
        }

    gastos.append(nuevo_gasto)
    print("Gasto registrado con exito!! :D ")

# {}  [] no le paren a esto, este teclado no tienes estos signos

def listar_gastos(gastos):
    print("---LSTA DE GASTOS REGISTRADOS---")
    if not gastos:
        print("no hay gastos registrados actualmente :D")
        return
    for i, g in enumerate(gastos, 1):
         print(f"{i}. Categoria: {g['categoria']} // Monto: bs{g['monto']:.2f} // Fecha: {g['fecha']}")

#---HASTA AQUI ME TRABAJO GENTE <3  (liz btw)
