import os
import sys

from django.core.wsgi import get_wsgi_application

# Adiciona o diretório base ao path do sistema (opcional mas recomendado)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Define o módulo de configurações padrão do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GREENSHIFT.settings')

# Obtém a aplicação WSGI
application = get_wsgi_application()
