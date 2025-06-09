import logging
from logging.handlers import RotatingFileHandler
import os
from app import create_app

# Cria a aplicação Flask a partir da fábrica definida em app/__init__.py
app = create_app()

# Configuração de logging
if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)

app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Aplicação iniciada.')

# Tratamento global de erros (opcional)
@app.errorhandler(500)
def internal_error(error):
    app.logger.error('Erro interno do servidor: %s', error)
    return "Erro interno do servidor", 500

@app.errorhandler(404)
def not_found_error(error):
    app.logger.warning('Página não encontrada: %s', error)
    return "Página não encontrada", 404

# Exposição explícita do app para o servidor WSGI
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
