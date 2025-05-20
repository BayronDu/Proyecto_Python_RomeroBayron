from datetime import datetime


def recorrerFecha(listaGastos,rango):
    for i in range(len(listaGastos[rango]["fecha"])):
            print("Dia: ",listaGastos[rango]["fecha"][i]["dia"])
            print("Hora: ",listaGastos[rango]["fecha"][i]["hora"])
    return listaGastos[rango]["fecha"]

def mostrarTodos (listaGastos):
    for i in range (len(listaGastos)):
                print("=============================================")
                print("                Gasto #",i+1," ============")
                print("=============================================")            
                print("Monto:", str(listaGastos[i]["monto"]))
                print("Categoria:",listaGastos[i]["categoria"])
                print("Descripción:",listaGastos[i]["descripcion"])           
                listaFecha = recorrerFecha (listaGastos,i)
                

def mostrarUna(listaGastos, categoriaMayus):
    cont = 1
    for i in range (len(listaGastos)):
                if(listaGastos[i]["categoria"] == categoriaMayus):
                    print("=============================================")
                    print("    Gastos por categoría",categoriaMayus +str(cont))
                    print("=============================================")            
                    print("Monto:", str(listaGastos[i]["monto"]))
                    print("Categoria:",listaGastos[i]["categoria"])
                    print("Descripción:",listaGastos[i]["descripcion"])
                    listaFecha = recorrerFecha (listaGastos,i)

                    cont +=1
    if(cont == 1):
        print("La categoria: ",categoriaMayus.upper(),"  que ha ingresado no existe. Valide las opciones e intentelo nuevamente")


def mostrarConFechas(listaGastos,fechaInicial,fechaFinal):
        for i in range(len(listaGastos)):
                convertirFecha = datetime.strptime(listaGastos[i]["fecha"][0]["dia"],"%d-%m-%Y").date()
                if(fechaInicial <= convertirFecha <= fechaFinal):
                    print("=============================================")
                    print("    Gastos por fecha ============")
                    print("=============================================")            
                    print("Monto:", str(listaGastos[i]["monto"]))
                    print("Categoria:",listaGastos[i]["categoria"])
                    print("Descripción:",listaGastos[i]["descripcion"])
                    listaFecha = recorrerFecha (listaGastos,i)

def calcularDiario(listaGastos):
            diaActual = datetime.now().date()
            diaActualFormat = datetime.strptime(diaActual,"%d-%m-%Y")
            for i in range(len(listaGastos)):
                convertirFecha = datetime.strptime(listaGastos[i]["fecha"][0]["dia"],"%d-%m-%Y").date()
                if(diaActualFormat == convertirFecha):
                    totalDiario = totalDiario + listaGastos[i]["monto"]
            print("=============================================")
            print("         Gastos en el día de hoy ============")
            print("======="+diaActualFormat+"===================")
                    