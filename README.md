# Projeto para estágio na B2BFlow

Este projeto está conectado ao Supabase e envia mensagens com Z-API.

## Como configurar:

1. Crie uma tabela **"Contatos"** no Supabase com três colunas: `id`, `nome`, `telefone`.

2. Crie um arquivo `.env` com as variáveis:
SUPABASE_URL=seu_url_aqui
SUPABASE_KEY=sua_key_aqui
ZAPI_TOKEN=seu_token_zapi_aqui
ZAPI_INSTANCE_ID=seu_id_de_instancia_zapi


3. Instale as dependências:

```bash
pip install supabase
pip install python-dotenv
pip install requests
```

4. Criar um arquivo main.py:
```bash
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL").strip()
SUPABASE_KEY = os.getenv("SUPABASE_KEY").strip()

# Cria o cliente
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Faz a consulta na tabela 'contatos'
response = supabase.table("Contatos").select("*").execute()

# Imprime o resultado
print("Contatos retornados:", response.data)
```
##Como Rodar:
