import os
from dotenv import load_dotenv
from supabase import create_client
import requests

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def enviar_mensagem(telefone, nome):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/send-text"
    payload = {
        "phone": telefone,
        "message": f"Olá {nome}, tudo bem com você?"
    }
    headers = {
        "Client-Token": ZAPI_TOKEN,
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")
        if response.status_code == 200:
            print(f"Mensagem enviada para {nome} ({telefone})")
        else:
            print(f"Erro ao enviar mensagem para {nome} ({telefone})")
    except Exception as e:
        print(f"Erro de requisição para {nome}: {e}")

def main():
    response = supabase.table("Contatos").select("*").limit(3).execute()
    contatos = response.data or []
    for contato in contatos:
        telefone = contato.get('telefone')
        nome = contato.get('nome')
        if telefone and nome:
            enviar_mensagem(telefone, nome)
        else:
            print(f"Contato inválido: {contato}")

if __name__ == "__main__":
    main()
