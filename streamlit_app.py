import streamlit as st
from graph_flow import build_graph

# Build the LangGraph app
app = build_graph()

st.title("🧠 AI Customer Support Bot – Narayan Shiva Sansthan")

# User input
user_input = st.text_input("Ask me anything 👇", "")

if user_input:
    with st.spinner("Thinking..."):
        result = app.invoke({"message": user_input})
        st.success(result["response"])
