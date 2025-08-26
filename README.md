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
