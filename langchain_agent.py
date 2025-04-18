import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load .env variables
load_dotenv()

# Load the OpenAI LLM
llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Prompt template
prompt = ChatPromptTemplate.from_template("""
You are Ananya, a kind and helpful customer support assistant for Narayan Shiva Sansthan.

User query:
{message}

Answer in a helpful, friendly tone. If it's about donations, receipts, volunteering, or location, guide them.
""")

# Chain = prompt → LLM → parser
chain = prompt | llm | StrOutputParser()

# Function for LangGraph node
def run_agent(state):
    message = state["message"]
    response = chain.invoke({"message": message})
    return {"response": response}
