from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

model = ChatOpenAI(
    model="arcee-ai/trinity-large-preview:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

template = PromptTemplate(
    template="Give me details about {topic} in brief",
    input_variables=["topic"]
)

prompt = template.invoke({"topic": "RAG"})

response = model.invoke(prompt)

print(response)
print(response.content)