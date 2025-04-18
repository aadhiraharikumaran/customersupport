from langgraph.graph import StateGraph
from typing import TypedDict
from langchain_core.runnables import RunnableLambda
from langchain_agent import run_agent

# Define the state schema using TypedDict
class State(TypedDict):
    message: str
    response: str

def build_graph():
    # Initialize the StateGraph with the State schema
    graph = StateGraph(State)

    # Add the agent node
    graph.add_node("agent", RunnableLambda(run_agent))

    # Set the entry and finish points
    graph.set_entry_point("agent")
    graph.set_finish_point("agent")

    return graph.compile()
