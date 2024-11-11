# Guía de Instalación y Creación de un Entorno Virtual en Python

## 1. Instalación de Python

1. **Descargar Python:**
   - Ve al sitio oficial de Python: [https://www.python.org/downloads/](https://www.python.org/downloads/).
   - Descarga la versión más reciente de Python para tu sistema operativo.

2. **Instalar Python:**
   - **Windows:** Ejecuta el instalador y asegúrate de marcar la casilla que dice `Add Python to PATH`, luego sigue las instrucciones.
   - **MacOS:** Descarga el archivo `.pkg` e instálalo siguiendo las instrucciones.
   - **Linux:** Python suele estar preinstalado. Si no lo tienes, abre una terminal y escribe:
     ```bash
     sudo apt update
     sudo apt install python3
     ```

3. **Verificar la Instalación:**
   - Abre una terminal (o el símbolo del sistema en Windows) y escribe:
     ```bash
     python --version
     ```
   - Si aparece la versión de Python, la instalación fue exitosa.

## 2. Crear un Entorno Virtual

Un entorno virtual permite instalar paquetes específicos para un proyecto sin afectar otros proyectos.

1. **Abrir la Terminal:**
   - Navega a la carpeta donde quieres crear tu entorno virtual.

2. **Crear el Entorno Virtual:**
   - Ejecuta el siguiente comando, reemplazando `mi_entorno` con el nombre que prefieras para tu entorno:
     ```bash
     python -m venv mi_entorno
     ```

3. **Activar el Entorno Virtual:**
   - **Windows:**
     ```bash
     mi_entorno\Scripts\activate
     ```
   - **MacOS/Linux:**
     ```bash
     source mi_entorno/bin/activate
     ```

   Al activar el entorno, verás el nombre del entorno en el terminal, lo cual indica que está activo.

4. **Desactivar el Entorno Virtual:**
   - Cuando hayas terminado, puedes desactivar el entorno con:
     ```bash
     deactivate
     ```

## 3. Instalación de Paquetes en el Entorno Virtual

Con el entorno virtual activado, puedes instalar paquetes usando `pip`, y estos quedarán aislados para tu proyecto.

```bash
    pip install nombre_paquete
```

## 4. Verificar los Paquetes Instalados
Para listar los paquetes instalados en el entorno, utiliza:
```bash
pip list
```
## 5. Guardar Dependencias en un Archivo
Para exportar las dependencias a un archivo requirements.txt, usa:

```bash
pip freeze > requirements.txt
```
Este archivo contiene los paquetes y versiones exactas, lo que facilita replicar el entorno en otros equipos.

## 6. Instalar Dependencias desde requirements.txt
Si quieres replicar el entorno en otro equipo, puedes instalar las dependencias del archivo requirements.txt con:

```bash
pip install -r requirements.txt
```