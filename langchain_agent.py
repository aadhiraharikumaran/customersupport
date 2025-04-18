import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load API key from .env
load_dotenv()

# 🔍 Optional debug (you can remove after testing)
print("🔑 OpenAI API Key Loaded:", os.getenv("OPENAI_API_KEY"))

# Initialize the OpenAI Chat model
llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Output parser to return string results
parser = StrOutputParser()

# Prompt template
prompt = ChatPromptTemplate.from_template("""
You are Ananya, a helpful customer support assistant.

The user query is:
{message}

Respond kindly and helpfully, addressing the concern clearly.
""")

# Define the full runnable pipeline
chain = prompt | llm | parser

# Expose a function for LangGraph to use
def run_agent(state):
    message = state["message"]
    response = chain.invoke({"message": message})
    return {"response": response}
