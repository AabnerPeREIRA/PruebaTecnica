from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Alumno(BaseModel):
    id: int
    nombre: str
    apellido: str

alumnos = [
    Alumno(id=1, nombre="Jesus", apellido="Armando"),
    Alumno(id=2, nombre="Jose", apellido="Gonzalez"),
    Alumno(id=3, nombre="Juan", apellido="Escutia"),
    Alumno(id=4, nombre="Rocio", apellido="Martinez"),
    Alumno(id=5, nombre="Pedro", apellido="Pascal")
]

@app.get("/")
def index():
    """Saludo"""
    mensaje = ""
    return mensaje

@app.get("/Alumnos")
def obtener_todos_alumnos():

    return alumnos

@app.get("/Alumnos/Ver_alumno{id}")
def obtener_un_alumno(id: int):
    for alumno in alumnos:
        if alumno.id == id:
            return alumno

    return {"mensaje": "Alumno no encontrado"}

@app.post("/Alumnos/Insertar_alumno")
def insertar_alumno(nuevo_alumno: Alumno):

    nuevo_id = max(alumno.id for alumno in alumnos) + 1
    nuevo_alumno.id = nuevo_id


    alumnos.append(nuevo_alumno)

    return {"mensaje": "Alumno insertado correctamente"}

@app.put("/Alumnos/Actualizar_alumno{id}")
def actualizar_alumno(id: int, datos_alumno: Alumno):
    for alumno in alumnos:
        if alumno.id == id:
            alumno.nombre = datos_alumno.nombre
            alumno.apellido = datos_alumno.apellido
            return {"mensaje": "Alumno actualizado correctamente"}

    return {"mensaje": "Alumno no encontrado"}

@app.delete("/Alumnos/Eliminar_alumno/{id}")
def eliminar_alumno(id: int):
    for alumno in alumnos:
        if alumno.id == id:
            alumnos.remove(alumno)
            return {"mensaje": "Alumno eliminado correctamente"}

    return {"mensaje": "Alumno no encontrado"}

#------------------------Maestros--------------------------

class Maestro(BaseModel):
    id: int
    nombre: str
    apellido: str
    materia: str


maestros = [
    Maestro(id=1, nombre="Jesus", apellido="Armando", materia="Español"),
    Maestro(id=2, nombre="Jose", apellido="Gonzalez", materia="Matematicas"),
    Maestro(id=3, nombre="Juan", apellido="Escutia", materia="Geografia"),
    Maestro(id=4, nombre="Rocio", apellido="Martinez", materia="Historia"),
    Maestro(id=5, nombre="Pedro", apellido="Pascal", materia="Programacion")
]


@app.get("/Maestros")
def obtener_todos_maestros():
    """Obtener todos los maestros"""
    return maestros


@app.get("/Maestros/Ver_maestro/{id}")
def obtener_un_maestro(id: int):
    for maestro in maestros:
        if maestro.id == id:
            return maestro

    return {"mensaje": "Maestro no encontrado"}


@app.post("/Maestros/Insertar_maestro")
def insertar_maestro(nuevo_maestro: Maestro):
 
    nuevo_id = max(maestro.id for maestro in maestros) + 1
    nuevo_maestro.id = nuevo_id

    maestros.append(nuevo_maestro)

    return {"mensaje": "Maestro insertado correctamente"}


@app.put("/Maestros/Actualizar_maestro/{id}")
def actualizar_maestro(id: int, datos_maestro: Maestro):
    for maestro in maestros:
        if maestro.id == id:
            maestro.nombre = datos_maestro.nombre
            maestro.apellido = datos_maestro.apellido
            maestro.materia = datos_maestro.materia
            return {"mensaje": "Maestro actualizado correctamente"}

    return {"mensaje": "Maestro no encontrado"}


@app.delete("/Maestros/Eliminar_maestro/{id}")
def eliminar_maestro(id: int):
    for maestro in maestros:
        if maestro.id == id:
            maestros.remove(maestro)
            return {"mensaje": "Maestro eliminado correctamente"}

    return {"mensaje": "Maestro no encontrado"}

#------------------------Maestros--------------------------

class Materias(BaseModel):
    id: int
    nombre_Materia: str
    Maestro: str
    Cant_Alumos_Inscritos: int

materias = [
    Materias(id=1, nombre_materia="Matemáticas", maestro="Juan Pérez", cant_alumnos_inscritos=30),
    Materias(id=2, nombre_materia="Historia", maestro="María Gómez", cant_alumnos_inscritos=25),
    Materias(id=3, nombre_materia="Ciencias", maestro="Pedro Rodríguez", cant_alumnos_inscritos=28),
]


@app.get("/materias")
def obtener_todas_materias():
    """Obtener todas las materias"""
    return materias


@app.get("/materias/{id}")
def obtener_materia_por_id(id: int):
    for materia in materias:
        if materia.id == id:
            return materia

    return {"mensaje": "Materia no encontrada"}


@app.post("/materias")
def agregar_materia(materia: Materias):
    materias.append(materia)
    return {"mensaje": "Materia agregada correctamente"}


@app.put("/materias/{id}")
def actualizar_materia(id: int, nueva_materia: Materias):
    for materia in materias:
        if materia.id == id:
            materia.nombre_materia = nueva_materia.nombre_materia
            materia.maestro = nueva_materia.maestro
            materia.cant_alumnos_inscritos = nueva_materia.cant_alumnos_inscritos
            return {"mensaje": "Materia actualizada correctamente"}

    return {"mensaje": "Materia no encontrada"}


@app.delete("/materias/{id}")
def eliminar_materia(id: int):
    for materia in materias:
        if materia.id == id:
            materias.remove(materia)
            return {"mensaje": "Materia eliminada correctamente"}

    return {"mensaje": "Materia no encontrada"}