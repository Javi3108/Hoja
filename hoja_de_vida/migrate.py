import os
import django
from django.core.management import call_command

# Establece el entorno de configuración
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hojavida_project.settings")
django.setup()

# Ejecuta las migraciones
call_command('migrate')
