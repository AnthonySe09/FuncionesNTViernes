def crearListaEstudiantes(cantidadEstudiantes):
    estudiantes = []
    for i in range (cantidadEstudiantes):
        estudiante={}
        estudiante["id"]=input("id: ")
        estudiante["nombres"]=input("escriba su nombre: ")
        estudiante["documentos"]=input("escriba su documento: ")
        estudiante["correo"]=input("correo: ")
        estudiante["telefono"]=input("telefono: ")
        estudiante["promedio"]=input("promedio: ")
        estudiante["semestre"]=input("semestre: ")
        estudiante["esBecado"]=input("tienes beca: ")
        estudiantes.append(estudiante)
    return estudiantes

#invocando la funcion
resultado=crearListaEstudiantes(2)
print(resultado)