# src/llm_guard/main.py

import json
import re
from typing import Type, TypeVar

from pydantic import BaseModel, ValidationError

# Define um tipo genérico para que o type hinting funcione bem
T = TypeVar("T", bound="GuardSchema")

class ParseError(Exception):
    """Exceção customizada para erros durante o parsing da saída do LLM."""
    pass

class GuardSchema(BaseModel):
    """
    Classe base que herda de pydantic.BaseModel e adiciona o método .parse().
    """

    @classmethod
    def parse(cls: Type[T], text: str) -> T:
        """
        Analisa uma string de texto (potencialmente de um LLM), extrai
        um bloco de JSON e o valida contra o schema da classe.

        Args:
            text: A string de texto a ser analisada.

        Returns:
            Uma instância da classe preenchida com os dados validados.

        Raises:
            ParseError: Se o JSON não for encontrado ou for inválido.
        """
        # 1. Tenta encontrar um bloco de JSON na string
        # A regex busca por um texto que começa com '{' ou '[' e termina com '}' ou ']'
        # O padrão `re.DOTALL` permite que '.' corresponda a quebras de linha.
        match = re.search(r"\{.*\}|\[.*\]", text, re.DOTALL)

        if not match:
            raise ParseError("Nenhum bloco de JSON encontrado no texto fornecido.")

        json_string = match.group(0)

        # 2. Tenta validar o JSON encontrado com o Pydantic
        try:
            # cls.model_validate_json() é o método moderno do Pydantic v2
            return cls.model_validate_json(json_string)
        except ValidationError as e:
            # Se o Pydantic falhar, levantamos nossa própria exceção
            raise ParseError(f"O JSON extraído é inválido: {e}") from e
        except json.JSONDecodeError as e:
            # Se a string não for nem mesmo um JSON válido
            raise ParseError(f"Falha ao decodificar o JSON: {e}") from e