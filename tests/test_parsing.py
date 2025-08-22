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
    with pytest.raises(ParseError, match="O JSON extraído é inválido"):
        UserInfo.parse(text)