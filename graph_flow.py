from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_agent import run_agent

# ✅ Define your state schema using TypedDict
class AgentState(TypedDict):
    message: str
    response: str

# ✅ Intent classification logic
def classify_intent(state: AgentState) -> str:
    msg = state["message"].lower()
    if "bill" in msg or "payment" in msg or "utr" in msg:
        return "billing_node"
    elif "error" in msg or "issue" in msg or "not working" in msg:
        return "tech_node"
    else:
        return "fallback_node"

# ✅ Action nodes
def billing_node(state: AgentState) -> AgentState:
    return {"message": state["message"], "response": run_agent(state["message"])}

def tech_node(state: AgentState) -> AgentState:
    return {"message": state["message"], "response": run_agent(state["message"])}

def fallback_node(state: AgentState) -> AgentState:
    return {"message": state["message"], "response": "Sorry, I couldn't understand your request. Please rephrase."}

# ✅ Build the LangGraph state machine
def build_graph():
    graph = StateGraph(AgentState)  # 👈 This is the proper way now
    graph.set_entry_point("classify")

    graph.add_node("classify", classify_intent)
    graph.add_node("billing_node", billing_node)
    graph.add_node("tech_node", tech_node)
    graph.add_node("fallback_node", fallback_node)

    graph.add_edge("classify", "billing_node")
    graph.add_edge("classify", "tech_node")
    graph.add_edge("classify", "fallback_node")

    graph.add_edge("billing_node", END)
    graph.add_edge("tech_node", END)
    graph.add_edge("fallback_node", END)

    return graph.compile()
