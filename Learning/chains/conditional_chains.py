#literal is used for fixed constant values ->
"""Instead of saying:

"this variable is a string"

you say:

"this variable can only be these exact strings."""

#Since the output of the llm is not constant it can varry like one word or a sentence and we want consistent output so we will use pydantic parser for validation and formatting.
#Runnable Branch is used to do conditional chaining it requires a condition(using lambda func) and if true then the chain which should execute. also a default chain if no condition matches.
#runnable lambda is used to convert lambda function into a runnable to run it like a chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from langchain_core.runnables import RunnableBranch,RunnableLambda
from typing import Literal
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="arcee-ai/trinity-large-preview:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
class Feedback(BaseModel):
    sentiment: Literal ["positive",'negative'] = Field(description="give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)   
parser1 = StrOutputParser()

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative \n. {feedback} \n {format_instructions}",
    input_variables=['feedback'],
    partial_variables={"format_instructions":parser2.get_format_instructions()}
)

classifier_chain = prompt1 | llm | parser2

#print(classifier_chain.invoke({"feedback":"this smartphone is terriblily awesome "}).sentiment)

prompt2= PromptTemplate(
    template="write an appropriate response for the following positive feedback.{feedback}",
    input_variables=['feedback']
)

prompt3= PromptTemplate(
    template="write an appropriate response for the following negative feedback.{feedback}",
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "positive",prompt2|llm|parser1),
    (lambda x:x.sentiment == "negative",prompt3|llm|parser1),#takes tuple
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({"feedback":"the smartphone is of blue color  "})
print(result)
chain.get_graph().print_ascii()
