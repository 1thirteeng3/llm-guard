# Bem-vindo ao LLM-Guard

**LLM-Guard** é uma biblioteca Python projetada para tornar as interações com Modelos de Linguagem Grandes (LLMs) mais robustas, confiáveis e estruturadas.

Usando o poder e a simplicidade do Pydantic, o `LLM-Guard` permite que você defina esquemas de dados e garanta que a saída de um LLM se ajuste a esses esquemas, mesmo que a saída seja um texto não estruturado ou um JSON malformado.

### Principais Funcionalidades

* ✅ **Validação Robusta:** Defina a estrutura de dados esperada usando classes Pydantic.
* 🛠️ **Reparo Automático:** Corrige automaticamente JSONs com erros de sintaxe.
* 🔎 **Extração Inteligente:** Extrai dados estruturados a partir de texto puro.
* ⚙️ **Configurável:** Permite que você escolha o modelo de IA e os parâmetros para as operações de reparo e extração.