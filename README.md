\# 🛡️ py-llm-shield



\*\*Robust validation and intelligent extraction of Large Language Model (LLM) outputs with the simplicity of Pydantic.\*\*



`py-llm-shield` is a Python library designed to make interactions with LLMs more reliable and structured. Leveraging the power of Pydantic classes, it ensures that the output of an LLM conforms to a predefined data schema, even if the original response is unstructured text or malformed JSON.



Say goodbye to manual inference and complex handling of broken JSON!



\## ✨ Main Features



\* \*\*Robust Validation:\*\* Define the expected data structure using Pydantic classes.

\* \*\*Automatic Repair:\*\* Automatically fixes JSONs with syntax or structure errors.

\* \*\*Smart Extraction:\*\* Extracts structured data from plain text, following its schema. \* \*\*Configurable:\*\* Allows you to choose the AI ​​model and parameters for repair and extraction operations (e.g., GPT-4o, temperature).

\* \*\*Detailed Error Handling:\*\* Specific exceptions (`ExtractionError`, `RepairError`) for precise control.



\## 🚀 Installation



The easiest way to install `py-llm-shield` is through `pip`:



```bash

pip install py-llm-shield

# Intelligent Features (OpenAI)
To use the repair and extraction features that rely on an LLM (like OpenAI's), you'll need to install the optional dependencies and have a valid API key.

pip install "py-llm-shield[openai]"

Make sure to set your OpenAI API key as an environment variable:

export OPENAI_API_KEY="your_api_key_here"

📚 Quick Start Guide
See how easy it is to extract structured data from plain text using py-llm-shield:
from py_llm_shield import GuardSchema
from openai import OpenAI

# 1. Define the schema for the data you expect
class Person(GuardSchema):
name: str
age: int
city: str

# 2. Initialize the OpenAI client
# (Make sure OPENAI_API_KEY is configured in the environment)
openai_client = OpenAI()

# 3. Provide unstructured text or malformed JSON
example_text = "The client's name is Ana Silva, she is 35 years old, and lives in Rio de Janeiro."
broken_json = '{"name": "Bruno", "age": "twenty-two", "city": "São Paulo",' # Extra comma and incorrect type

# 4. Use py-llm-shield to extract and validate! try:
print("--- Extracting from plain text ---")
ana = Person.parse(
example_text,
llm_client=openai_client,
llm_config={"model": "gpt-4o", "temperature": 0.2} # Example configuration
)
print(ana)
# Expected output: Person(name='Ana Silva', age=35, city='Rio de Janeiro')

print("\n--- Repairing broken JSON ---")
bruno = Person.parse(
broken_json,
llm_client=openai_client
)
print(bruno)
# Expected output: Person(name='Bruno', age=22, city='São Paulo')

except Exception as e:
print(f"An error occurred: {e}")

⚠️ Error Handling
py-llm-shield provides specific exceptions for more refined error handling:

from py_llm_shield import GuardSchema, ExtractionError, RepairError
from openai import OpenAI
# ... (openai_client initialized) ...

class Product(GuardSchema):
id: str
name: str

# Example of extraction failure
impossible_text = "This text does not contain product information."
try:
Product.parse(impossible_text, llm_client=openai_client)
except ExtractionError as e:
print(f"Extraction failed: {e}")

# Example of repair failure (LLM returns invalid JSON even after repair)
json_irrecoverable = '{"id": "123", "name": "Item", "extra": {}' # LLM was unable to repair
try:
Product.parse(impossible_json, llm_client=openai_client)
except RepairError as e:
print(f"Repair failed: {e}")

🤝 Contribution
Contributions are welcome! If you found a bug or have a suggestion for improvement, please open an issue on GitHub.

📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.

Developed by Giovanni Lemos Barcelos


# 🛡️ py-llm-shield



\*\*Validação robusta e extração inteligente de saídas de Large Language Models (LLMs) com a simplicidade do Pydantic.\*\*



`py-llm-shield` é uma biblioteca Python projetada para tornar as interações com LLMs mais confiáveis e estruturadas. Utilizando o poder das classes Pydantic, ela garante que a saída de um LLM se ajuste a um esquema de dados predefinido, mesmo que a resposta original seja um texto não estruturado ou um JSON malformado.



Diga adeus à inferência manual e ao tratamento complexo de JSONs quebrados!



\## ✨ Principais Funcionalidades



\* \*\*Validação Robusta:\*\* Defina a estrutura de dados esperada usando classes Pydantic.

\* \*\*Reparo Automático:\*\* Corrige automaticamente JSONs com erros de sintaxe ou estrutura.

\* \*\*Extração Inteligente:\*\* Extrai dados estruturados a partir de texto puro, seguindo seu esquema.

\* \*\*Configurável:\*\* Permite que você escolha o modelo de IA e os parâmetros para as operações de reparo e extração (e.g., GPT-4o, temperatura).

\* \*\*Tratamento de Erros Detalhado:\*\* Exceções específicas (`ExtractionError`, `RepairError`) para um controle preciso.



\## 🚀 Instalação



A maneira mais fácil de instalar `py-llm-shield` é através do `pip`:



```bash

pip install py-llm-shield

# Funcionalidades Inteligentes (OpenAI)
Para usar as funcionalidades de reparo e extração que dependem de um LLM (como os da OpenAI), você precisará instalar as dependências opcionais e ter uma chave de API válida.

pip install "py-llm-shield[openai]"

Certifique-se de configurar sua chave de API da OpenAI como uma variável de ambiente:

export OPENAI_API_KEY="sua_chave_da_api_aqui"

📚 Guia de Início Rápido
Veja como é fácil extrair dados estruturados de um texto simples usando py-llm-shield:

from py_llm_shield import GuardSchema
from openai import OpenAI

# 1. Defina o schema dos dados que você espera
class Pessoa(GuardSchema):
    nome: str
    idade: int
    cidade: str

# 2. Inicialize o cliente da OpenAI
# (Certifique-se de que OPENAI_API_KEY esteja configurada no ambiente)
cliente_openai = OpenAI()

# 3. Forneça um texto não estruturado ou um JSON malformado
texto_exemplo = "O cliente se chama Ana Silva, tem 35 anos e reside no Rio de Janeiro."
json_quebrado = '{"nome": "Bruno", "idade": "vinte e dois", "cidade": "São Paulo",' # Vírgula extra e tipo errado

# 4. Use py-llm-shield para extrair e validar!
try:
    print("--- Extraindo de texto puro ---")
    ana = Pessoa.parse(
        texto_exemplo,
        llm_client=cliente_openai,
        llm_config={"model": "gpt-4o", "temperature": 0.2} # Exemplo de configuração
    )
    print(ana)
    # Saída esperada: Pessoa(nome='Ana Silva', idade=35, cidade='Rio de Janeiro')

    print("\n--- Reparando JSON quebrado ---")
    bruno = Pessoa.parse(
        json_quebrado,
        llm_client=cliente_openai
    )
    print(bruno)
    # Saída esperada: Pessoa(nome='Bruno', idade=22, cidade='São Paulo')

except Exception as e:
    print(f"Ocorreu um erro: {e}")

⚠️ Tratamento de Erros
py-llm-shield fornece exceções específicas para um tratamento de erros mais refinado:

from py_llm_shield import GuardSchema, ExtractionError, RepairError
from openai import OpenAI
# ... (cliente_openai inicializado) ...

class Produto(GuardSchema):
    id: str
    nome: str

# Exemplo de falha na extração
texto_impossivel = "Este texto não contém informações de produto."
try:
    Produto.parse(texto_impossivel, llm_client=cliente_openai)
except ExtractionError as e:
    print(f"Falha na extração: {e}")

# Exemplo de falha no reparo (LLM retorna JSON inválido mesmo após reparo)
json_irrecuperavel = '{"id": "123", "nome": "Item", "extra": {}' # LLM não conseguiu corrigir
try:
    Produto.parse(json_irrecuperavel, llm_client=cliente_openai)
except RepairError as e:
    print(f"Falha no reparo: {e}")

🤝 Contribuição
Contribuições são bem-vindas! Se você encontrou um bug ou tem uma sugestão de melhoria, por favor, abra uma issue no GitHub.

📄 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

Desenvolvido por Giovanni Lemos Barcelos
