# Instalación de Python, VSCode y Git

## 1. Instalar Python

### Windows
1. Ir a [python.org/downloads](https://www.python.org/downloads/)
2. Descargar Python 3.12 o superior
3. Ejecutar instalador
4. **IMPORTANTE**: Marcar "Add Python to PATH"
5. Clic en "Install Now"

Verificar instalación abriendo CMD o PowerShell:
```bash
python --version
```

### Linux
```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
```

## 2. Instalar Git

Git nos permite descargar y gestionar los materiales del curso.

### Windows

1. Ir a [git-scm.com/download/win](https://git-scm.com/download/win)
2. Descargar e instalar
3. Dejar las opciones por defecto
4. Verificar instalación abriendo **Git Bash** y ejecutar:
   ```bash
   git --version
   ```

### Linux

```bash
sudo apt update
sudo apt install git
git --version
```

## 3. Instalar Visual Studio Code

1. Ir a [code.visualstudio.com](https://code.visualstudio.com/)
2. Descargar e instalar según tu sistema operativo

## 4. Instalar Extensiones de VSCode

Abre VSCode y ve a Extensiones (Ctrl+Shift+X):

### Extensiones Esenciales

1. **Python** (Microsoft)
   - Buscar "Python"
   - Instalar la de Microsoft (ms-python.python)
   - Proporciona: autocompletado, debugging, linting

### Extensiones Opcionales (recomendadas)

- **Python Indent**: Ayuda con la indentación automática
- **Error Lens**: Muestra errores más visibles en el código

## 5. Descargar los materiales del curso

Una vez instalado Git, descarga los materiales del curso:

1. Abrir VSCode
2. Abrir Terminal (menú **Terminal** → **New Terminal** o Ctrl+Ñ)
3. Navegar a la carpeta donde quieres guardar los materiales:
   ```bash
   cd Documents
   # o la carpeta que prefieras
   ```
4. Clonar el repositorio:
   ```bash
   git clone https://github.com/DavidGasku/python_campusdigital.git
   ```
5. Entrar en la carpeta descargada:
   ```bash
   cd python_campusdigital
   ```
6. Abrir la carpeta en VSCode: **File → Open Folder** y seleccionar `python_campusdigital`

### ¿Qué acabas de hacer?

`git clone` ha descargado todos los materiales del curso a tu ordenador:
- Ejercicios de Python
- Ejemplos de código
- Documentación en Markdown

Ahora puedes trabajar con todos estos archivos en VSCode.

## 6. Probar que todo funciona

### Visualizar archivos Markdown

1. En VSCode, abre cualquier archivo `.md` del repositorio
2. Para ver el archivo formateado, presiona `Ctrl+Shift+V` (o `Cmd+Shift+V` en Mac)
3. VSCode incluye soporte nativo para Markdown, no necesitas extensiones adicionales

### Ejecutar tu primer programa Python

1. En VSCode, navega a la carpeta de ejercicios
2. Abre el archivo `ejercicios.py` (o crea uno nuevo `prueba.py`)
3. Escribe:
   ```python
   print("¡Hola, mundo!")
   print("Mi primer programa en Python")
   ```
4. Guardar (Ctrl+S)
5. Clic derecho en el archivo → "Run Python File in Terminal"
6. Deberías ver la salida en la terminal

¡Felicidades! Ya tienes todo configurado para el curso.

## Resumen de lo instalado

**Python** - El lenguaje de programación
**Git** - Para descargar y actualizar materiales
**VSCode** - El editor de código (con soporte nativo para Markdown)
**Extensión Python** - Soporte para Python en VSCode
**Repositorio del curso** - Todos los materiales descargados

## Actualizar los materiales del curso

Si el profesor actualiza los materiales, puedes descargar los cambios:

1. Abrir terminal en VSCode
2. Asegurarte de estar en la carpeta `python_campusdigital`:
   ```bash
   cd python_campusdigital
   ```
3. Descargar las actualizaciones:
   ```bash
   git pull
   ```

Esto actualizará tu copia local con los nuevos materiales.

## Problemas comunes

### Python no se encuentra
- Reiniciar el ordenador después de instalar Python
- En Windows: verificar que está en PATH (reinstalar marcando la casilla)

### Git no funciona
- Asegurarse de usar **Git Bash** en Windows
- Verificar que git está instalado: `git --version`

### No se puede clonar el repositorio
- Verificar conexión a internet
- Copiar y pegar exactamente la URL: `https://github.com/DavidGasku/python_campusdigital.git`

### VSCode no ejecuta Python
- Instalar la extensión de Python
- Recargar VSCode (Ctrl+Shift+P → "Reload Window")
- Verificar que Python está instalado: `python --version` en la terminal
