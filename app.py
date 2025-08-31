import streamlit as st
from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
groq_api_key = st.secrets["GROQ_API_KEY"] 
# Streamlit Page Config
st.set_page_config(page_title="Health and Fitness Chatbot", page_icon="💪")
st.header("💪 Health & Fitness Chatbot")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize memory
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="chat_history", input_key="user_question")

# Initialize LLM
llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.3-70b-versatile")

# Define prompt template with memory
template = """
You are a fitness and health assistant.
You only answer questions related to health, medicine, fitness, diet, and gym.
Try to answer as short as possible.
If the question is unrelated, respond with: \"Sorry, I\'m not sure about that. I\'m designed to answer questions related to fitness and health only.\"

Here is the conversation so far:
{chat_history}

Question: {user_question}
Answer:
"""
prompt = PromptTemplate(template=template, input_variables=["chat_history", "user_question"])
chain = LLMChain(llm=llm, prompt=prompt, memory=st.session_state.memory)

# Sidebar for clear chat
with st.sidebar:
    st.header("Options")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.session_state.memory.clear()
        st.toast("Chat cleared!")

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_question = st.chat_input("Ask about fitness, health, diet, or gym...")

if user_question:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_question})

    with st.chat_message("user"):
        st.markdown(user_question)

    # Get bot response using memory
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chain.run(user_question=user_question)
        st.markdown(response)

    # Save bot response
    st.session_state.messages.append({"role": "assistant", "content": response})

st.sidebar.markdown("---")

st.sidebar.caption("-- By Aditya Naranje --")
