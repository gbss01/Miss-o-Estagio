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
pip install supabase python-dotenv requests
```

4. Crie o arquivo main.py com o código para consultar contatos:
```bash
from supabase import create_client
import os
from dotenv import load_dotenv
import requests

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL").strip()
SUPABASE_KEY = os.getenv("SUPABASE_KEY").strip()
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN").strip()
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID").strip()

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def enviar_mensagem(telefone, nome):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/send-text"
    payload = {
        "phone": telefone,
        "message": f"Olá {nome}, tudo bem com você?"
    }
    headers = {
        "Content-Type": "application/json",
        "Client-Token": ZAPI_TOKEN
    }
    response = requests.post(url, json=payload, headers=headers)
    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")
    if response.status_code == 200:
        print(f"Mensagem enviada para {nome} ({telefone})")
    else:
        print(f"Erro ao enviar para {nome} ({telefone})")

def main():
    response = supabase.table("Contatos").select("*").limit(3).execute()
    contatos = response.data or []
    print("Contatos retornados:", contatos)
    for contato in contatos:
        enviar_mensagem(contato['telefone'], contato['nome'])

if __name__ == "__main__":
    main()
```



## Como Rodar:

1. Entre no terminal (CMD)
2. Entre na pasta do projeto
3. Logo que entrar na pasta do projeto pelo CMD digite:
```bash
python main.py
```




## Observações sobre a integração com Z-API:

Implementei a integração com a API do Z-API seguindo a documentação oficial, usando o token e o ID da instância para enviar mensagens personalizadas.

Nos testes, encontrei dificuldades na entrega das mensagens, que podem estar relacionadas a limitações do serviço ou configurações da instância.

Apesar disso, o código está pronto para buscar os contatos no Supabase e enviar as mensagens conforme o desafio pede.

Usei algumas referências e apoio para garantir que o código estivesse bem estruturado e funcional.

Se precisarem, posso ajudar a melhorar ou esclarecer qualquer ponto dessa integração.
