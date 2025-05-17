# Base image oficial de python
FROM python:3.11-slim

# Seteamos directorio de trabajo
WORKDIR /usr/src/app

# Copiamos requirements
COPY requirements.txt ./

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la app
COPY app ./app
COPY tests ./tests

# Comando por defecto para correr la app
CMD ["python", "app/main.py"]
