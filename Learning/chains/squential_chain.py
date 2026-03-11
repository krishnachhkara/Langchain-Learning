# using multiple prompts and calling model twice
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a detailed report on the {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="summarize the following {text} in 5 points",
    input_variables=['text']
)

llm = ChatOpenAI(
    model="arcee-ai/trinity-large-preview:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

parser = StrOutputParser()

chain = prompt1 | llm | parser| prompt2 | llm | parser

result = chain.invoke({"topic": "Time Management"})

print(result)

chain.get_graph().print_ascii()