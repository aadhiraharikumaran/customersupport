from langgraph.graph import StateGraph
from langchain_agent import run_agent

# Define a fallback node (optional but helpful)
def fallback_node(state):
    return {"response": "Sorry, I couldn't process your request. Please try again or ask a different question."}

# Build LangGraph flow
def build_graph():
    graph = StateGraph()

    # Add nodes
    graph.add_node("agent", run_agent)
    graph.add_node("fallback", fallback_node)

    # Define edges (simple one-step interaction)
    graph.set_entry_point("agent")
    graph.set_finish_point("agent")

    return graph.compile()
