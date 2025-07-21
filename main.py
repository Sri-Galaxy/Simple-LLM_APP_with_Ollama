import os
import streamlit as st
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def load_environment():
    load_dotenv()
    os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY', '')
    os.environ['LANGCHAIN_TRACING_V2'] = 'true'
    os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT', 'DefaultProject')


def build_chain():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("user", "{question}")
    ])

    model = ChatOllama(model="gemma:2b")
    parser = StrOutputParser()
    return prompt | model | parser


def render_app():
    st.set_page_config(page_title="GenAI Assistant with Ollama", layout="centered")
    st.title("🤖 GenAI Assistant")
    st.markdown("Ask anything, and get an intelligent response from a local open-source LLM.")

    user_input = st.text_input("What question do you have?")

    if user_input:
        with st.spinner("Generating response..."):
            try:
                response = chain.invoke({"question": user_input})
                st.success("Here's the response:")
                st.markdown(response)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    load_environment()
    chain = build_chain()
    render_app()
