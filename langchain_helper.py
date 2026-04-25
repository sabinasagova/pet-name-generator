from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2:3b",
    temperature=0.1
)

prompt_template = PromptTemplate(
    input_variables=["animal_type", "pet_color"],
    template="What is a good name for a {pet_color} {animal_type}?"
)

chain = prompt_template | llm

def generate_pet_name(animal_type: str, pet_color: str) -> dict[str, str]:
    name = chain.invoke({"animal_type": animal_type.strip(), "pet_color": pet_color.strip()})
    return {"pet_name": name.strip()}
