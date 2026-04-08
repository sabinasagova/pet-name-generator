from langchain_ollama import OllamaLLM, ChatOllama
from langchain_core.prompts import PromptTemplate


# We can keep OllamaLLM for the simple text chain
llm = OllamaLLM(
    model="llama3.2:3b",
    temperature=0.1
)

prompt_template = PromptTemplate(
    input_variables=["animal_type", "pet_color"],
    template="What is a good name for a {pet_color} {animal_type}?"
)

chain = prompt_template | llm

def generate_pet_name(animal_type, pet_color):
    name = chain.invoke({"animal_type": animal_type, "pet_color": pet_color})
    return {"pet_name": name.strip()}

def langchain_agent():
    # Keep this local and network-independent for reliable execution.
    agent_llm = ChatOllama(model="llama3.2:3b", temperature=0.1)

    result = agent_llm.invoke(
        "What is the average lifespan of a cat, and how does it compare to the average lifespan of a dog?"
    )

    print(result.content)

if __name__ == "__main__":
    langchain_agent()
    # print(generate_pet_name("cat", "orange"))
    #print(generate_pet_name("dog", "brown"))