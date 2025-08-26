# src/llm_guard/main.py (VERSÃO COM CONFIGURAÇÃO)

import json
import re
from typing import Any, Type, TypeVar, Dict

from pydantic import BaseModel, ValidationError

# Adicionado Dict ao import
T = TypeVar("T", bound="GuardSchema")

class ParseError(Exception):
    """Exceção customizada para erros durante o parsing da saída do LLM."""
    pass

class GuardSchema(BaseModel):
    """
    Classe base que herda de pydantic.BaseModel e adiciona o método .parse().
    """

    @classmethod
    def parse(cls: Type[T], text: str, llm_client: Any = None, llm_config: Dict[str, Any] = None) -> T:
        # --- MUDANÇA 1: Adicionado o argumento 'llm_config' na assinatura acima ---

        # --- MUDANÇA 2: Lógica para mesclar configurações ---
        default_config = {"model": "gpt-3.5-turbo", "temperature": 0.0}
        if llm_config:
            # Sobrescreve os padrões com a configuração do usuário
            default_config.update(llm_config)
        final_config = default_config
        
        match = re.search(r"\{.*\}|\[.*\]", text, re.DOTALL)
        
        if not match:
            if not llm_client:
                raise ParseError("Nenhum bloco de JSON encontrado e nenhum cliente LLM foi fornecido para extração.")
            
            try:
                extraction_prompt = f"""
Extraia as informações do texto original para preencher um objeto JSON.
O esquema JSON necessário é:
{cls.model_json_schema()}

Texto Original:
"{text}"

Responda APENAS com o objeto JSON válido.
"""
                # --- MUDANÇA 3: Usando a configuração final na chamada da API ---
                response = llm_client.chat.completions.create(
                    messages=[{"role": "user", "content": extraction_prompt}],
                    **final_config
                )
                json_string_from_extraction = response.choices[0].message.content
                return cls.model_validate_json(json_string_from_extraction)
            except Exception as e:
                raise ParseError(f"Falha ao extrair e validar a partir do texto: {e}") from e

        json_string = match.group(0)

        try:
            return cls.model_validate_json(json_string)
        except (ValidationError, json.JSONDecodeError):
            if not llm_client:
                raise ParseError("Falha ao validar o JSON e nenhum cliente LLM foi fornecido para reparo.")

            try:
                repair_prompt = f"""O JSON a seguir está quebrado ou malformado. Por favor, corrija a sintaxe e retorne APENAS o JSON corrigido, sem nenhum texto adicional.

JSON Quebrado:
{json_string}"""
                # --- MUDANÇA 4: Usando a configuração final na chamada da API ---
                response = llm_client.chat.completions.create(
                    messages=[{"role": "user", "content": repair_prompt}],
                    **final_config
                )
                repaired_json_string = response.choices[0].message.content
                return cls.model_validate_json(repaired_json_string)
            except Exception as e:
                raise ParseError(f"Falha ao reparar e validar o JSON: {e}") from e