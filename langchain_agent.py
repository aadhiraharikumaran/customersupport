import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load API Key from .env
load_dotenv()

# Initialize ChatOpenAI
llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo",  # You can use "gpt-4" if you have access
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Prompt template
prompt = ChatPromptTemplate.from_template("""
You are Ananya, a kind and helpful customer support assistant for Narayan Shiva Sansthan.

User query:
{message}

Answer in a helpful, friendly tone. If it's about donations, receipts, volunteering, or location, guide them.
""")

# Output parser
parser = StrOutputParser()

# Chain = Prompt ➝ LLM ➝ Output
chain = prompt | llm | parser

# This function will be used in the LangGraph node
def run_agent(state):
    message = state["message"]
    response = chain.invoke({"message": message})
    return {"response": response}
