import streamlit as st
from graph_flow import build_graph

# Set up the Streamlit page configuration
st.set_page_config(page_title="AI Customer Support Assistant")

# Display the title and instructions
st.title("📞 AI Customer Support Assistant")
st.write("Ask anything about donations, receipts, volunteering, and more.")

# Build the LangGraph application
app = build_graph()

# Create a text input for user messages
user_input = st.text_input("You:", "")

# Process the user input when provided
if user_input:
    with st.spinner("Thinking..."):
        result = app.invoke({"message": user_input})
        st.success("Assistant: " + result["response"])
