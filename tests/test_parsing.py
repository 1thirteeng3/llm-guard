# tests/test_parsing.py

import pytest
from llm_guard import GuardSchema, ParseError

# 1. Define um schema de teste
class UserInfo(GuardSchema):
    name: str
    age: int

# 2. Cria os casos de teste
def test_parse_com_json_limpo():
    """Testa se o parsing funciona com um JSON perfeito."""
    text = '{"name": "Alice", "age": 30}'
    user = UserInfo.parse(text)
    assert user.name == "Alice"
    assert user.age == 30

def test_parse_com_json_cercado_de_texto():
    """Testa se a biblioteca extrai o JSON corretamente de uma string maior."""
    text = "Aqui estão os dados do usuário: ```json\n{\"name\": \"Bob\", \"age\": 25}\n```. Espero que ajude!"
    user = UserInfo.parse(text)
    assert user.name == "Bob"
    assert user.age == 25

def test_falha_quando_nao_ha_json():
    """Testa se ParseError é levantado quando não há JSON."""
    text = "Não há dados aqui."
    with pytest.raises(ParseError, match="Nenhum bloco de JSON encontrado"):
        UserInfo.parse(text)

def test_falha_com_tipo_invalido():
    """Testa se ParseError é levantado para tipos de dados incorretos."""
    text = '{"name": "Charlie", "age": "vinte"}' # age deveria ser int
    # ATUALIZE A MENSAGEM ESPERADA AQUI
    with pytest.raises(ParseError, match="Falha ao validar o JSON e nenhum cliente LLM foi fornecido para reparo."):
        UserInfo.parse(text)
# Adicione esta importação no início do arquivo
from unittest.mock import Mock

def test_reparo_de_json_com_virgula_sobrando():
    """Testa se o LLM consegue corrigir um JSON com uma vírgula a mais."""
    # 1. O JSON quebrado que o LLM "real" retornaria
    texto_quebrado = '{"name": "Alice", "age": 30,}' # Vírgula extra no final

    # 2. O JSON corrigido que esperamos que o LLM de reparo nos dê
    texto_corrigido = '{"name": "Alice", "age": 30}'

    # 3. Criamos um "mock" do cliente OpenAI
    mock_client = Mock()
    
    # 4. Configuramos o mock para retornar a resposta corrigida quando for chamado
    mock_response = Mock()
    mock_response.choices = [Mock()]
    mock_response.choices[0].message = Mock()
    mock_response.choices[0].message.content = texto_corrigido
    mock_client.chat.completions.create.return_value = mock_response

    # 5. Executamos o parse com o JSON quebrado e o cliente mockado
    user = UserInfo.parse(texto_quebrado, llm_client=mock_client)

    # 6. Verificamos se o resultado está correto
    assert user.name == "Alice"
    assert user.age == 30
    # Verificamos se o método 'create' do nosso mock foi chamado uma vez
    mock_client.chat.completions.create.assert_called_once()

def test_falha_sem_llm_client_em_json_quebrado():
    """Testa se o parse falha em um JSON quebrado quando não há cliente."""
    texto_quebrado = '{"name": "Alice", "age": 30,}'
    with pytest.raises(ParseError, match="nenhum cliente LLM foi fornecido para reparo"):
        UserInfo.parse(texto_quebrado)