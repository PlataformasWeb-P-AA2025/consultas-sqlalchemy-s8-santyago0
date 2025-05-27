from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

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

# Consulta 03

# Obtener todas las tareas asignadas a los siguientes estudiantes
# - Jennifer Bolton
# - Elaine Perez
# - Heather Henderson
# - Charles Harris
# En función de cada tarea, presentar el número de entregas que tiene

# Obtenemos todos los registros de Tarea y armamos el camino para poder filtrar
# las tareas asignadas a estos estudiantes mediante un or_
tareas = session.query(Tarea).join(Entrega).join(Estudiante)\
    .filter(
        or_(
            Estudiante.nombre == ("Jennifer Bolton"),
            Estudiante.nombre == ("Elaine Perez"),
            Estudiante.nombre == ("Heather Henderson"),
            Estudiante.nombre == ("Charles Harris")
            )
        ).all()

for t in tareas:
    # Presentamos el titulo de la tarea y contamos el tamaño de la lista de entregas
    # para obtener el número de entregas
    print(f"Tarea: {t.titulo} - Entregas hechas: {len(t.entregas)}")
