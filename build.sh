#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recopilar archivos estáticos
python manage.py collectstatic --no-input

# Ejecutar migraciones (IMPORTANTE)
python manage.py migrate --no-input

# Crear superusuario si no existe (opcional)
# python manage.py createsuperuser --no-input --username admin --email admin@example.com || true
# Crear/Asegurar superusuario
echo "Asegurando superusuario..."
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='admin').exists() or \
User.objects.create_superuser('admin', 'javierapo152@gmail.com', 'admin123')" \
| python manage.py shell