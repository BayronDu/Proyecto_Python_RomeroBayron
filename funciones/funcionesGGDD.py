import json

def abrirJSON():
    dicFinal=[]
    with open("./data/datos.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./data/datos.json",'w') as outFile:
        json.dump(dic,outFile)

def guardarReporteEnJSON(reporteDiario, nombre_archivo="reporte_gastos_diario.json"):
    with open(nombre_archivo, "w") as file:
        json.dump(reporteDiario, file, indent=4)
    print(f"Reporte guardado en el archivo {nombre_archivo}")