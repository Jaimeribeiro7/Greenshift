# Painel de Comissões - iGreen Energy

## Como implantar gratuitamente no Render

### 1. Crie um banco de dados PostgreSQL gratuito
- Acesse: https://dashboard.render.com
- Clique em "New +" > "PostgreSQL"
- Escolha um nome, mantenha o plano gratuito
- Copie a `Internal Database URL` para usar como variável de ambiente

---

### 2. Suba o projeto no GitHub

Inclua todos os arquivos do projeto Django, incluindo:
- `Procfile`
- `requirements.txt`
- `start.sh`

---

### 3. Crie um Web Service no Render
- Clique em "New +" > "Web Service"
- Conecte com o repositório GitHub
- Selecione:
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `./start.sh`
- Configure as variáveis de ambiente:

| Chave         | Valor                            |
|---------------|----------------------------------|
| `DATABASE_URL`| (URL do PostgreSQL do Render)    |
| `DEBUG`       | `False`                          |
| `SECRET_KEY`  | Use: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |

---

### 4. Acesse o app
- Após o deploy, o Render fornecerá a URL pública
- Use `/admin` para acessar o painel administrativo
