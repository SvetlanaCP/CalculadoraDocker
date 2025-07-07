# Calculadora Flask Dockerizada

Este proyecto es una calculadora web que realiza operaciones básicas (suma, resta, multiplicación y división) con una interfaz moderna y colorida. El backend está desarrollado en Python usando Flask y el frontend en HTML/CSS/JavaScript. Todo el proyecto está contenerizado usando Docker y automatizado con GitHub Actions.

## Estructura del proyecto

- `app.py`: Aplicación principal de Flask (backend).
- `requirements.txt`: Dependencias de Python necesarias.
- `Dockerfile`: Archivo para construir la imagen Docker.
- `templates/index.html`: Interfaz web de la calculadora.
- `static/style.css`: Estilos CSS de la calculadora.
- `.github/workflows/docker-image.yml`: Pipeline de CI/CD con GitHub Actions.

## Funcionamiento básico

1. El usuario accede a la calculadora web.
2. Al realizar una operación, el frontend envía los datos al backend Flask usando AJAX.
3. Flask procesa la operación y devuelve el resultado al frontend.
4. El resultado se muestra en pantalla.

## Cómo ejecutar el proyecto

### Opción 1: Usando Docker (recomendado)

1. Clona el repositorio:
   ```sh
   git clone https://github.com/SvetlanaCP/CalculadoraDocker.git
   cd CalculadoraDocker
   ```
2. Construye la imagen Docker:
   ```sh
   docker build -t mi-flask-app .
   ```
3. Ejecuta el contenedor:
   ```sh
   docker run -p 5000:5000 mi-flask-app
   ```
4. Abre tu navegador en [http://localhost:5000/](http://localhost:5000/)

### Opción 2: Ejecutar localmente (sin Docker)

1. Crea un entorno virtual e instala dependencias:
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # En Windows
   pip install -r requirements.txt
   ```
2. Ejecuta la app:
   ```sh
   python app.py
   ```
3. Abre tu navegador en [http://localhost:5000/](http://localhost:5000/)

## CI/CD

- El proyecto incluye un pipeline de GitHub Actions que:
  - Construye la imagen Docker.
  - Ejecuta pruebas automáticas (si existen).
  - Sube la imagen a Docker Hub automáticamente.

## Autor
- Proyecto realizado por SvetlanaCP 