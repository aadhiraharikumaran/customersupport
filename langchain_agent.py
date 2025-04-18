from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI LLM with API key
llm = ChatOpenAI(
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Create prompt template
template = """You are a helpful AI assistant.
Human: {message}
AI:"""

prompt = PromptTemplate.from_template(template)

# Create the chain
chain = LLMChain(llm=llm, prompt=prompt)

def run_agent(state):
    message = state["message"]
    response = chain.invoke({"message": message})
    return {"message": message, "response": response["text"]}
