from langchain_community.chat_models import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from billing import billing_lookup
from tech_support import troubleshoot_issue
import os

llm = ChatOpenAI(
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

tools = [
    Tool(name="Billing Lookup", func=billing_lookup, description="Use for billing-related queries."),
    Tool(name="Tech Support", func=troubleshoot_issue, description="Use for technical issues.")
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

def run_agent(input_text):
    return agent.run(input_text)
