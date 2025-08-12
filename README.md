# Projeto para estágio na B2BFlow

Este projeto está conectado ao Supabase e envia mensagens com Z-API.

## Como configurar:
### Supabase:
1. Vá ao Site da SupaBase(https://supabase.com/)

2. Crie uma conta gratuitamente

3. Logo após crie um projeto com o nome "Contatos", depois adicione três colunas              id/nome/numero(Geralmente o id cria sozinho)

4. Depois preeecha 3 linhas com nome e telefone de três pessoas(Atenção!!!! O numero do telefone tem que ser nesse formato 5511912345678 (55 = codigo brasil, 11 = DDD + Numero)

5. Vá em configurações do projeto -> Configurações da API -> Copie e cole e o codigo URL do projeto no arquivo .env no seu devido lugar.

6. Ainda em configurações do projeto -> Chaves de API -> Copie e cole a chave do anon public no arquivo .env no seu devido lugar.


### Z-API:
1. Crie uma conta gratuitamente no site da Z-API(https://app.z-api.io/)
2. Crie uma instância Nome da instância, o mais essencial será o API instânce e o API-TOKEN, é só pegar os dois codigo e colocados no arquivo .env cada um no seu lugar
   

### No seu VsCode:

1. Crie um arquivo ".env" com as variáveis e preecha com as informações que foram copiadas anteriormente:
```bash
SUPABASE_URL=seu_url_aqui
SUPABASE_KEY=sua_key_aqui
ZAPI_TOKEN=seu_token_zapi_aqui
ZAPI_INSTANCE_ID=seu_id_de_instancia_zapi
```

2. Instale as dependências:
```bash
pip install supabase python-dotenv requests
```

3. Crie o arquivo "main.py" com o código para consultar contatos:
```bash
# Importar as bibliotecas necessarias:
from supabase import create_client
import os
from dotenv import load_dotenv
import requests

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# Pega os arquivos necessarios no env e tira os espaços
SUPABASE_URL = os.getenv("SUPABASE_URL").strip()
SUPABASE_KEY = os.getenv("SUPABASE_KEY").strip()

# Cria um cliente para acessar o banco Supabase usando URL e chave
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Pega os arquivos necessarios no env e tira os espaços
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN").strip()
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID").strip()

# URL base para enviar mensagens via Z-API, formatada com o ID da instância e token
ZAPI_URL = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/send-text"

# Função que envia a mensagem
def enviar_mensagem(telefone, nome):

    payload = {
        "phone": telefone,
        "message": f"Olá {nome}, tudo bem com você?"
    }

    headers = {
        "Content-Type": "application/json",
        "Client-Token": ZAPI_TOKEN
    }

    response = requests.post(ZAPI_URL, json=payload, headers=headers)

    # Imprime status e resposta para debug
    print("Status code:", response.status_code)
    print("Response text:", response.text)

    # Se o status for 200 (OK), confirma o envio da mensagem
    if response.status_code == 200:
        print(f"Mensagem enviada para {nome} ({telefone})")
    else:
        print(f"Erro ao enviar para {nome} ({telefone})")

def main():
    # Consulta a tabela "Contatos" no Supabase e pega todos os registros
    response = supabase.table("Contatos").select("*").execute()

    # Se conseguir dados, imprime para confirmação
    if response.data:
        print("Contatos retornados:", response.data)
        # Percorre até 3 contatos para enviar mensagens
        for contato in response.data[:3]:
            enviar_mensagem(contato['telefone'], contato['nome'])
    else:
        print("Nenhum contato encontrado no banco.")

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
