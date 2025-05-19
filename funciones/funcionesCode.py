def mostrarTodos (listaGastos):
    for i in range (len(listaGastos)):
           
                print("=============================================")
                print("                Gasto #",i+1," ============")
                print("=============================================")            
                print("Monto:", str(listaGastos[i]["monto"]))
                print("Categoria:",listaGastos[i]["categoria"])
                print("Descripción:",listaGastos[i]["descripcion"])
                print("Fecha",(listaGastos[i]["fecha"]))
                print("=============================================")

def mostrarUna(listaGastos, categoriaMayus):
    for i in range (len(listaGastos)):
                if(listaGastos[i]["categoria"] == categoriaMayus):
                    print("=============================================")
                    print("    Gastos por categoría",categoriaMayus, str(cont))
                    print("=============================================")            
                    print("Monto:", str(listaGastos[i]["monto"]))
                    print("Categoria:",listaGastos[i]["categoria"])
                    print("Descripción:",listaGastos[i]["descripcion"])
                    print("Fecha",(listaGastos[i]["fecha"]))
                    cont +=1