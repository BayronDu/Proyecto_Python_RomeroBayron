diaAhora = str(fechaActual.day)
            mesAhora = str(fechaActual.month)
            anioAhora = str(fechaActual.year)
            horaAhora = str(fechaActual.hour)
            minutosAhora = str(fechaActual.minute)
            
            dirFecha = {"fecha":diaAhora+"-"+mesAhora+"-"+anioAhora,
                        "hora": horaAhora+":"+minutosAhora}
            listaFecha = [dirFecha]
            dirGastos = {
            "monto":montoGasto, 
            "categoria":categoriaGasto,
            "descripcion":descripcionGasto,
            "fecha":listaFecha
                        }