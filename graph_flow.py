from langgraph.graph import StateGraph, END
from langchain_agent import run_agent

def classify_intent(state):
    msg = state["message"].lower()
    if "bill" in msg or "payment" in msg or "utr" in msg:
        return "billing_node"
    elif "error" in msg or "issue" in msg or "not working" in msg:
        return "tech_node"
    else:
        return "fallback_node"

def billing_node(state):
    return {"response": run_agent(state["message"])}

def tech_node(state):
    return {"response": run_agent(state["message"])}

def fallback_node(state):
    return {"response": "Sorry, I couldn't understand your request. Please rephrase."}

def build_graph():
    graph = StateGraph()
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
