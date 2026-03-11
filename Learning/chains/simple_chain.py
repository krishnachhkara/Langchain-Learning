from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

prompt = PromptTemplate(
    template="give me 7 excersises which will help me to train my self and build a body like {person} at home without equipment",
    input_variables=["person"]
)

llm = ChatOpenAI(
    model="arcee-ai/trinity-large-preview:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({"person":"Son Goku"})

print(result)

chain.get_graph().print_ascii()#used to draw graph of architecture/working of the chain