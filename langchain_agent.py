import os
from langchain_core.runnables import Runnable
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the ChatOpenAI model with the API key from environment variables
llm = ChatOpenAI(temperature=0)

# Define the chat prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer support assistant for a donation-based NGO."),
    ("user", "{message}")
])

# Create the processing chain
chain: Runnable = prompt | llm | StrOutputParser()

def run_agent(state):
    message = state["message"]
    response = chain.invoke({"message": message})
    return {"message": message, "response": response}
