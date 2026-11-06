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


def listar_gastos(gastos):
    print("---LSTA DE GASTOS REGISTRADOS---")
    if not gastos:
        print("no hay gastos registrados actualmente :D")
        return
    for i, g in enumerate(gastos, 1):
         print(f"{i}. Categoria: {g['categoria']} // Monto: bs{g['monto']:.2f} // Fecha: {g['fecha']}")

#---HASTA AQUI MI TRABAJO GENTE <3  (liz btw)

#--- Aqui Empieza mi parte (Antonio)

def buscar_gastos(gastos):
    print("\n--- BUSCAR GASTOS POR CATEGORÍA ---")
    if not gastos:
        print("No hay gastos registrados para buscar.")
        return
        
    busqueda = input("Ingrese la categoría a buscar: ").strip().capitalize()
    encontrados = [g for g in gastos if g['categoria'] == busqueda]
    
    if not encontrados:
        print(f"No se encontraron gastos en la categoría '{busqueda}'.")
        return
        
    print(f"\nGastos encontrados en '{busqueda}':")
    for i, g in enumerate(encontrados, 1):
        print(f"- Monto: ${g['monto']:.2f} | Fecha: {g['fecha']}")

def modificar_gasto(gastos):
    print("\n--- MODIFICAR GASTO ---")
    if not gastos:
        print("No hay gastos para modificar.")
        return
        
    for i, g in enumerate(gastos, 1):
        print(f"{i}. Categoría: {g['categoria']} | Monto: ${g['monto']:.2f} | Fecha: {g['fecha']}")
        
    try:
        indice = int(input("Ingrese el número del gasto que desea modificar: ")) - 1
        if indice < 0 or indice >= len(gastos):
            print("❌ Error: Número de gasto fuera de rango.")
            return
    except ValueError:
        print("❌ Error: Debe ingresar un número entero válido.")
        return
        
    gasto_actual = gastos[indice]
    
    try:
        nuevo_monto = float(input(f"Nuevo monto (actual: {gasto_actual['monto']}): "))
        if nuevo_monto <= 0:
            print("❌ Error: El monto debe ser mayor a cero.")
            return
    except ValueError:
        print("❌ Error: Monto inválido.")
        return
        
    nueva_categoria = input(f"Nueva categoría (actual: {gasto_actual['categoria']}): ").strip()
    if not nueva_categoria:
        print("❌ Error: La categoría no puede estar vacía.")
        return
        
    nueva_fecha = input(f"Nueva fecha (actual: {gasto_actual['fecha']}): ").strip()
    if not nueva_fecha:
        print("❌ Error: La fecha no puede estar vacía.")
        return
        
    gastos[indice] = {
        "monto": nuevo_monto,
        "categoria": nueva_categoria.capitalize(),
        "fecha": nueva_fecha
    }
    print("✅ ¡Gasto modificado exitosamente!")

def eliminar_gasto(gastos):
    print("\n--- ELIMINAR GASTO ---")
    if not gastos:
        print("No hay gastos para eliminar.")
        return
        
    for i, g in enumerate(gastos, 1):
        print(f"{i}. Categoría: {g['categoria']} | Monto: ${g['monto']:.2f} | Fecha: {g['fecha']}")
        
    try:
        indice = int(input("Ingrese el número del gasto que desea eliminar: ")) - 1
        if indice < 0 or indice >= len(gastos):
            print("❌ Error: Número de gasto fuera de rango.")
            return
    except ValueError:
        print("❌ Error: Debe ingresar un número entero válido.")
        return
        
    eliminado = gastos.pop(indice)
    print(f"🗑️ Gasto eliminado: {eliminado['categoria']} - ${eliminado['monto']:.2f}")

    #--- Aca termina mi parte :) (Antonio)
    #--- Aqui comienza mi parte (Yoxel)
    def reporte_gastos_por_categoria(gastos)
        print("\n---REPORTE: TOTAL GASTADO POR CATEGORIA---")
        if not gastos:
            print("No hay suficientes datos para imprimir el reporte")
            return
        totales = {}
        for g in gastos
            cat = g['categoria']
            monto = g['monto']
            totales[cat] = totales.get(cat, 0.0) + monto

    print(f"{'CATEGORÍA':<20} | {'TOTAL GASTADO':<15}")
    print("-" * 38)
    for cat, total in totales.items():
        print(f"{cat:<20} | ${total:<14.2f}")
    print("-" * 38)
#---Aqui termina mi parte Yoxel
                            
