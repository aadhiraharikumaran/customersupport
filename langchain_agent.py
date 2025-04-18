import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# Load your environment variables from .env
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=os.getenv("OPENAI_API_KEY")  # Optional if already set in env
)

# Prompt
prompt = ChatPromptTemplate.from_template("You are a helpful customer support assistant. Answer the user's query.\n\nUser: {message}")

# Final chain
chain = prompt | llm | StrOutputParser()

def run_agent(message: str) -> str:
    response = chain.invoke({"message": message})
    return response
