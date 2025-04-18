import streamlit as st
from graph_flow import build_graph
from dotenv import load_dotenv

# Load your OpenAI API key from .env
load_dotenv()

# Build the LangGraph app
app = build_graph()

st.set_page_config(page_title="🧠 AI Support Assistant", page_icon="💬")
st.title("🧠 AI Customer Support Assistant")
st.markdown("Type your message below to get help on billing, tech issues, or general queries.")

# Session state to hold chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Input form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Ask about payments, receipts, UTR issues, or tech problems...")
    submit = st.form_submit_button("Send")

# On submit, invoke the graph
if submit and user_input:
    result = app.invoke({"message": user_input, "response": ""})
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", result["response"]))

# Display chat history
for speaker, msg in st.session_state.history:
    st.markdown(f"**{speaker}:** {msg}")
