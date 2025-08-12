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

