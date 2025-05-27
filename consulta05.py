from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_, func # se importa el operador and

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

# Consulta 05

# En una consulta, obtener todos los cursos. Realizar un ciclo repetitivo
# para obtener en cada iteración las entregas por cada curso (con otra consulta),
# y presentar el promedio de calificaciones de las entregas

# Obtenemos todos los registros de Curso
cursos = session.query(Curso).all()

for c in cursos:
    entregas = session.query(func.avg(Entrega.calificacion)).join(Tarea).join(Curso)\
        .filter(Curso.titulo == c.titulo).all()
    
    print(f"Curso: {c.titulo} - Promedio de las entregas: {entregas}")
