import streamlit as st
from graph_flow import build_graph

st.title("🧠 AI Customer Support Assistant")

# Build the graph app
app = build_graph()

# Get user input
user_input = st.text_input("Enter your message:")

# Handle user input
if user_input:
    result = app.invoke({"message": user_input, "response": ""})
    st.markdown("**Response:**")
    st.write(result["response"])
