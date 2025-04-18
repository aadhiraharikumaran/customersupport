from langgraph.graph import StateGraph, StateType
from langchain_core.runnables import RunnableLambda
from langchain_agent import run_agent

# Define the state type as a dictionary
state = {"message": str, "response": str}

def build_graph():
    graph = StateGraph(StateType(state))

    # Add nodes
    graph.add_node("agent", RunnableLambda(run_agent))

    # Set flow
    graph.set_entry_point("agent")
    graph.set_finish_point("agent")

    return graph.compile()
