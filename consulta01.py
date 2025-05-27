from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from clases import *

# se importa información del archivo configuracion
from config import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Consulta 01

# 1. Obtener las entregas de todos los estudiantes que pertenecen al departamento
# de Arte. En función de la entrega, presentar, nombre del tarea, nombre del
# estudiante, calificación, nombre de instructor y nombre del departamento

# Obtenemos todos los registros de Entrega y filtramos los departamentos que son de Arte
entregas = session.query(Entrega).join(Tarea).join(Curso).join(Departamento)\
    .filter(Departamento.nombre == "Arte").all()

print("Consulta 01")

for e in entregas:
    print(f"Tarea: {e.tarea.titulo}\n" + # Desde el objeto tarea de Entrega obtenemos el titulo de la tarea
        f"Hecha por: {e.estudiante.nombre}\n" + # Desde el objeto estudiante de Entrega obtenemos en nombre del estudiante
        f"Calificación: {e.calificacion}\n" + # Atributo calificacion
        f"Instructor: {e.tarea.curso.instructor.nombre}\n" + # Desde el objeto tarea de Entregas armamos el camino hacia
                                                            # el cusro (objeto de Tarea), al instructor (objeto de Curso)
                                                            # y obtenemos el nombre del instructor
        f"Departamento: {e.tarea.curso.departamento.nombre}\n" + # Desde el objeto tarea de Entregas armamos el camino hacia
                                                                # el cusro (objeto de Tarea), al departamento (objeto de Curso)
                                                                # y obtenemos el nombre del departamento
        "--------------------------------------------------------")
