import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

# Prompt template...
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{question}")
])


# Streamlet framework...
st.title('Simple GenAI app with Ollama')
input_text = st.text_input('What question do you have?')

# Ollama model
@st.cache_resource
def load_model():
    return OllamaLLM(model="gemma:2b")  

model = load_model()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

if input_text:
    response = chain.invoke({'question': input_text})
    st.write(response)