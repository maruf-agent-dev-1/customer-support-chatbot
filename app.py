import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from faq_data import FAQ_CONTEXT

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API key not found. Please check your .env file.")
    st.stop()

genai.configure(api_key=api_key)

# Page setup
st.set_page_config(page_title="Acme Store Support Bot", page_icon="💬")
st.title("💬 Acme Store — Customer Support")
st.caption("Ask me about shipping, returns, orders, or payments.")

# Initialize the model with system instructions
# Using "gemini-flash-latest" so it always points to the newest stable Flash model
model = genai.GenerativeModel(
    model_name="gemini-flash-latest",
    system_instruction=FAQ_CONTEXT
)

# Initialize conversation history in session state (this is the "memory")
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Type your question here...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from Gemini (chat_session remembers history automatically)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat_session.send_message(user_input)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Something went wrong: {e}")