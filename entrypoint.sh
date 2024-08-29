#!/bin/sh

./wait-for-it.sh db:3306 --timeout=60 --strict -- echo "Database is up"


# Aplicar las migraciones
echo "Aplicando migraciones..."
python manage.py makemigrations
python manage.py migrate

# Crear superusuario solo si no existe
if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ]; then
  echo "Creando superusuario..."
  python manage.py createsuperuser --no-input
fi

# Iniciar Gunicorn
echo "Iniciando Gunicorn..."
gunicorn --bind 127.0.0.1:8000 gruposalinas.wsgi:application
