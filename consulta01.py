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

entregas = session.query(Entrega).join(Tarea).join(Curso).join(Departamento).filter(Departamento.nombre == "Arte")

print("Consulta 01")

for e in entregas:
    print(f"Tarea: {e.tarea.titulo}\n" +
          f"Hecha por: {e.estudiante.nombre}\n" +
          f"Calificación: {e.calificacion}\n" +
          f"Instructor: {e.tarea.curso.instructor.nombre}\n" +
          f"Departamento: {e.tarea.curso.departamento.nombre}\n" +
          "--------------------------------------------------------")
