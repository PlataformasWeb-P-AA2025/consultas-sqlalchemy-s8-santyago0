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

# Consulta 02

# Todos los departamentos que tengan notas de entregas menores o iguales a 0.3.
# En función de los departamentos, presentar el nombre del departamento y el
# número de cursos que tiene cada departamento

# Obtenemos todos los regitros de Departamento, hacemos el camino para poder filtrar
# las calificaciones para que sean menores o iguales a 0.3
departamentos = session.query(Departamento).join(Curso).join(Tarea).join(Entrega)\
    .filter(Entrega.calificacion <= 0.3).all()

for d in departamentos:
    # Presentamos el nombre de los departamentos y de la lista de objetos de los cursos
    # obtenemos el tamaño para saber cuantos cursos hay en cada departamento
    print(f"Departamento: {d.nombre} - Número de Cursos: {len(d.cursos)}")
