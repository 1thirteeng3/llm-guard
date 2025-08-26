# Quick Start Guide

Let's see how `py-llm-shield` can extract structured data from simple text.

First, make sure your OpenAI API key is set as an environment variable:
```bash
export OPENAI_API_KEY="your_key_here"
Now, let's get to the code:

from py_llm_shield import GuardSchema
from openai import OpenAI

# 1. Define the schema of the data you expect
class User(GuardSchema):
name: str
age: int
city: str

# 2. Initialize the OpenAI client
openai_client = OpenAI()

# 3. Provide unstructured text
pure_text = "The client's name is Ana, she is 35 years old and lives in Rio de Janeiro."

# 4. Use py-llm-shield to extract and validate! try:
validated_user = User.parse(
plain_text,
llm_client = client_openai
)
print(validated_user)
# Expected output:
# name = 'Ana' age = 35 city = 'Rio de Janeiro'

print(f"Name: {validated_user.name}, Age: {validated_user.age}")

except Exception as e:
print(f"An error occurred: {e}")