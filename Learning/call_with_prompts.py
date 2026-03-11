from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()

llm = ChatOpenAI(
    model="arcee-ai/trinity-large-preview:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

template= PromptTemplate(
    template="hi whats up tell me the best books as a begineer i should read to understand business mindset and finances",
)

response = llm.invoke(template.invoke({}))
print(template)
print(response.content)