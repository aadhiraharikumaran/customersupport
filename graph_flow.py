from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode
from langchain_core.runnables import RunnableLambda
from langchain_core.utils.state import make_state_type
from langchain_agent import run_agent

# Define state type
State = make_state_type("State", {"message": str, "response": str})

def build_graph():
    # Create the graph
    graph = StateGraph(State)

    # Define nodes
    graph.add_node("agent", RunnableLambda(run_agent))

    # Add edges
    graph.set_entry_point("agent")
    graph.set_finish_point("agent")

    # Compile to app
    app = graph.compile()
    return app
