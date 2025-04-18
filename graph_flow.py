from langgraph.graph import StateGraph
from langchain_agent import run_agent

# Fallback node returns dict
def fallback_node(state):
    return {"response": "Sorry, I couldn’t process your request. Please try again later."}

def build_graph():
    graph = StateGraph()

    # Add nodes
    graph.add_node("agent", run_agent)
    graph.add_node("fallback", fallback_node)

    # Set edges and flow
    graph.set_entry_point("agent")
    graph.set_finish_point("agent")  # or "fallback" if you want

    return graph.compile()
