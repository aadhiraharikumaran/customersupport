from langgraph.graph import StateGraph, define_state_type
from langchain_core.runnables import RunnableLambda
from langchain_agent import run_agent

# Define state schema using define_state_type
state = define_state_type({"message": str, "response": str})

def build_graph():
    graph = StateGraph(state)

    # Add your agent node
    graph.add_node("agent", RunnableLambda(run_agent))

    # Set entry and finish points
    graph.set_entry_point("agent")
    graph.set_finish_point("agent")

    return graph.compile()
