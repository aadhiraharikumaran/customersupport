import streamlit as st
from graph_flow import build_graph

st.set_page_config(page_title="AI Customer Support Assistant")

st.title("📞 AI Customer Support Assistant")
st.write("Ask anything about donations, receipts, volunteering, and more.")

# Build LangGraph app
app = build_graph()

# Chat input
user_input = st.text_input("You:", "")

if user_input:
    with st.spinner("Thinking..."):
        result = app.invoke({"message": user_input})
        st.success("Assistant: " + result["response"])
