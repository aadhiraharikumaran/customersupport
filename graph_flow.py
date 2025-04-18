from typing import TypedDict
from langgraph.graph import StateGraph
from langchain_agent import run_agent

# ✅ Define the expected input/output structure
class GraphState(TypedDict):
    message: str
    response: str

# ✅ Fallback node still returns a dictionary
def fallback_node(state: GraphState) -> GraphState:
    return {"response": "Sorry, I couldn’t process your request. Please try again later."}

# ✅ Build graph with state schema
def build_graph():
    graph = StateGraph(GraphState)  # <-- 🔥 this line fixes the error

    # Add nodes
    graph.add_node("agent", run_agent)
    graph.add_node("fallback", fallback_node)

    # Set entry and finish points
    graph.set_entry_point("agent")
    graph.set_finish_point("agent")  # or fallback

    return graph.compile()
