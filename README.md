# PruebaTecnica

Este es un proyecto de prueba técnica que utiliza FastAPI para crear una API web para administrar alumnos, maestros y materias. A continuación, se detallan los pasos para ejecutar el programa:

Requisitos
Python 3.x
FastAPI
Uvicorn

Instalación
1.-Descarga e instala Python desde el sitio web oficial: Python.org.
2.-Crea una carpeta en la ubicación deseada para tu entorno de desarrollo.
3.-Abre una terminal o línea de comandos y navega hasta la carpeta creada utilizando el comando cd ruta_de_la_carpeta.
4.-Crea un entorno virtual ejecutando los siguientes comandos (comandos para Windows):

  python -m venv mi_entorno
  mi_entorno\Scripts\activate.bat

5.-Instala FastAPI y Uvicorn ejecutando los siguientes comandos:

  pip install fastapi
  pip install uvicorn
  
Ejecución
6.-Asegúrate de estar en la carpeta del proyecto donde se encuentra el archivo main.py.
7.-Ejecuta el siguiente comando para iniciar el servidor:

uvicorn main:app --reload

8.-Una vez que el servidor esté en funcionamiento, deberías ver una dirección IP en la terminal, generalmente http://127.0.0.1:8000.
9.-Abre tu navegador web y accede a la dirección IP proporcionada, por ejemplo: http://127.0.0.1:8000.

Ahora puedes interactuar con la API utilizando las rutas y métodos disponibles.
