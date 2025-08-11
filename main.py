from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL").strip()
SUPABASE_KEY = os.getenv("SUPABASE_KEY").strip()

print("URL:", repr(SUPABASE_URL))
print("KEY:", repr(SUPABASE_KEY))

# Cria o cliente
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Faz a consulta na tabela 'contatos'
response = supabase.table("Contatos").select("*").execute()

# Imprime o resultado
print("Contatos retornados:", response.data)
