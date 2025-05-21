from datetime import datetime

linea = 45

def recorrerFecha(listaGastos,rango):
    for i in range(len(listaGastos[rango]["fecha"])):
            print("Dia: ",listaGastos[rango]["fecha"][i]["dia"])
            print("Hora: ",listaGastos[rango]["fecha"][i]["hora"])
    return listaGastos[rango]["fecha"]

def mostrarTodos (listaGastos):
    for i in range (len(listaGastos)):
                print(f"="*linea)
                print(f"Gasto # {i+1}".center(linea))
                print(f"="*linea)
                print("Monto:", str(listaGastos[i]["monto"]))
                print("Categoria:",listaGastos[i]["categoria"])
                print("Descripción:",listaGastos[i]["descripcion"])           
                listaFecha = recorrerFecha (listaGastos,i)
                

def mostrarUna(listaGastos, categoriaMayus):
    cont = 1
    total = 0
    for i in range (len(listaGastos)):
                if(listaGastos[i]["categoria"] == categoriaMayus):
                    print(f"="*linea)
                    print(f"Gastos por categoría {categoriaMayus} {cont}".center(linea))
                    print(f"="*linea)            
                    print(f'Monto: {listaGastos[i]["monto"]}')
                    print(f'Categoria: {listaGastos[i]["categoria"]}')
                    print(f'Descripción: {listaGastos[i]["descripcion"]}')
                    listaFecha = recorrerFecha (listaGastos,i)
                    total = total + listaGastos[i]["monto"]
                    cont +=1
    if(cont == 1):
        print("La categoria: ",categoriaMayus.upper(),"  que ha ingresado no existe. Valide las opciones e intentelo nuevamente")
    return total


def mostrarConFechas(listaGastos,fechaInicial,fechaFinal):
        for i in range(len(listaGastos)):
                convertirFecha = datetime.strptime(listaGastos[i]["fecha"][0]["dia"],"%d-%m-%Y").date()
                if(fechaInicial <= convertirFecha <= fechaFinal):
                    print(f"="*linea)
                    print(f"Gastos por fecha".center(linea))
                    print(f"="*linea)
                    print(f"Monto: {listaGastos[i]['monto']}".center(linea))
                    print(f"Categoria: {listaGastos[i]['categoria']}".center(linea))
                    print(f"Descripcion: {listaGastos[i]['descripcion']}".center(linea))
                    listaFecha = recorrerFecha (listaGastos,i)

def calcularDiario(listaGastos,diaFormat):
            totalDiario = 0
            for i in range(len(listaGastos)):
                convertirFecha = datetime.strptime(listaGastos[i]["fecha"][0]["dia"], "%d-%m-%Y").date()
                if(diaFormat == convertirFecha):
                    totalDiario = totalDiario + listaGastos[i]["monto"]
            return totalDiario

def calcularSemanal(listaGastos,fechaLimite):
            totalSemanal = 0
            for i in range(len(listaGastos)):
                convertirFecha = datetime.strptime(listaGastos[i]["fecha"][0]["dia"], "%d-%m-%Y").date()
                if(fechaLimite <= convertirFecha):
                    totalSemanal = totalSemanal + listaGastos[i]["monto"]
            print(str("Desde "+str(fechaLimite)).center(linea))
            print(str(str(totalSemanal)).center(linea))
            print(f"="*linea)

def calcularMes (listaGastos,mes):
            totalMes = 0
            for i in range(len(listaGastos)):
                convertirFecha = datetime.strptime(listaGastos[i]["fecha"][0]["dia"], "%d-%m-%Y").month
                if (convertirFecha == (mes-1)):
                    totalMes = totalMes + listaGastos[i]["monto"]
            print(str("Para el mes: "+str(mes-1)).center(linea))
            print(str(str(totalMes)+"").center(linea))
            print(f"="*linea)

def calcularCat(listaGastos,categoria,diaActualFormat):
    total = 0
    for i in range(len(listaGastos)):
            if (categoria == listaGastos[i]["categoria"] and listaGastos[i]["fecha"][0]["dia"] == diaActualFormat):
                total = total + listaGastos[i]["monto"]
    print(f"El total de la categoria {categoria} es de: ${total}")
    return total


def obtenerCat(listaGastos):
    categorias = []
    for i in range(len(listaGastos)):
          categoria = listaGastos[i]["categoria"]
          if categoria not in categorias:
            categorias.append(categoria) 
    return categorias

def sumarCatDiario(listaGastos,diaActual):
        for i in range(len(listaGastos)):
            if(listaGastos[i]["fecha"][0]["dia"] == diaActual):
                print(f'{listaGastos[i]["categoria"]}'.capitalize())
            for q in range(len(listaGastos)):
                    if listaGastos[q] == listaGastos[i] and listaGastos[q]["fecha"][0]["dia"] == diaActual:
                        print(f'-Descripción: {listaGastos[q]["descripcion"]} | Monto: ${listaGastos[q]["monto"]} | Hora: {listaGastos[q]["fecha"][0]["hora"]}')
                        print(f"-"*linea)
        print("-"*linea)       
        categoriaL = obtenerCat(listaGastos) #se utiliza para recorrer la lista y dar los gastos por categoria
        for i in range (len(categoriaL)):
            calcularCat(listaGastos,categoriaL[i],diaActual)


def sumarCatMes(listaGastos,mes): #sin definir
        for i in range(len(listaGastos)):
            if(listaGastos[i]["fecha"][0]["dia"] == diaActual):
                print(f'{listaGastos[i]["categoria"]}'.capitalize())
            for q in range(len(listaGastos)):
                    if listaGastos[q] == listaGastos[i] and listaGastos[q]["fecha"][0]["dia"] == diaActual:
                        print(f'-Descripción: {listaGastos[q]["descripcion"]} | Monto: ${listaGastos[q]["monto"]} | Hora: {listaGastos[q]["fecha"][0]["hora"]}')
                        print(f"-"*linea)
        print("-"*linea)       
        categoriaL = obtenerCat(listaGastos) #se utiliza para recorrer la lista y dar los gastos por categoria
        for i in range (len(categoriaL)):
            calcularCat(listaGastos,categoriaL[i],diaActual)
