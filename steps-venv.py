# entorno virtual es solo en python
#
#python --version
#pip --version

# BUSCAR INSTALAR PIP SI NO ESTA INSTALADO
# COMPROBAR VENV O INSTALAR VENV

#pipp list
#pip freeze

#python -m venv nombre-proyecto

# python -m  :  m de modulo


# ACTIVAR ENTORNO VIRTUAL

# venv - Scripts - ./activate
# Scripts - ./deactivate

# Inicializar git

# git init

# crea el repositorio vacio
# si no esta instalado git, instalar desde la pagina oficiAL

# INSTALAR FLASK

# pip install flask

# instalar - base de datos

# pip install Flask-MySQL

# instalar DB con credenciales

# pip install cryptography


# volcar dependencias en un txt para compartir en un repositorio
# y las personas que descarguen el repo, sepan que necesitan tener
# instalado

# el comando para crear el txt con dependencias es:
# pip freeze > requirements.txt

# puede tener otro nombre, por convencion es requirements.txt


# comando para instalar las dependencias hechas anteriormente

# pip install -r requirements.txt


# CREAR un Readme

# README.md



# agregar los archivos al repo

# git add .

# comprobar usuario y mail
# git config user.email    
# git config user.name

# definir usuario y mail

# git config --local user.email "mail@mail.com"
# git config --local user.name "fulano"


# realizar commit

# git commit -m "inicio del proyecto"


# crear repositorio nuevo en github
# opcion de repositorio existente

"""
…or push an existing repository from the command line
git remote add origin https://github.com/nian23sat/sistema-empleados.git
git branch -M main
git push -u origin main
"""

# si el ultimo comando lanza error debido a otra cuenta de git
# reconfigurar credenciales

# git config credential.username "usuario"

# se le pedira autenticar el usuario pidiendo password


# AGREGAR GIT IGNORE
# .GITIGNORE

# git push
# envia los commits a github


# Crear rama de trabajo para NO trabajar sobre main
# que es la rama principal y suele ser de produccion

# git switch -c develop

# crear otra rama mas
# git switch -c 01-instancia-flask


