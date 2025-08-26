# Guia de Início Rápido

Vamos ver como o `LLM-Guard` pode extrair dados estruturados de um simples texto.

Primeiro, certifique-se de que sua chave da API da OpenAI está configurada como uma variável de ambiente:
```bash
export OPENAI_API_KEY="sua_chave_aqui"

Agora, vamos ao código:
from llm_guard import GuardSchema
from openai import OpenAI

# 1. Defina o schema dos dados que você espera
class Usuario(GuardSchema):
    nome: str
    idade: int
    cidade: str

# 2. Inicialize o cliente da OpenAI
cliente_openai = OpenAI()

# 3. Forneça um texto não estruturado
texto_puro = "O cliente se chama Ana, ela tem 35 anos e mora no Rio de Janeiro."

# 4. Use o LLM-Guard para extrair e validar!
try:
    usuario_validado = Usuario.parse(
        texto_puro,
        llm_client=cliente_openai
    )
    print(usuario_validado)
    # Saída esperada:
    # nome='Ana' idade=35 cidade='Rio de Janeiro'

    print(f"Nome: {usuario_validado.nome}, Idade: {usuario_validado.idade}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")