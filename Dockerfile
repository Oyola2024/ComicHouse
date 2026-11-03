# Imagen oficial ligera de Python
FROM python:3.11-slim

# Evitar búferes de salida y archivos .pyc
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Directorio de trabajo
WORKDIR /app

# Instalar uv en el sistema
RUN pip install --no-cache-dir uv

# Copiar archivos de configuración de dependencias
COPY pyproject.toml uv.lock ./

# Instalar las dependencias exactas con uv
RUN uv sync --frozen --no-cache

# Copiar todo el código del proyecto (incluyendo src)
COPY . .

# Exponer el puerto de Django
EXPOSE 8000

# Ejecutar migraciones e iniciar el servidor indicando la ruta correcta a src/manage.py
CMD ["uv", "run", "python", "src/manage.py", "runserver", "0.0.0.0:8000"]