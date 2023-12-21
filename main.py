import os
import streamlit as st  
from langchain import OpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain


import google.generativeai as genai 
from IPython.display import Markdown

# os.environ['GOOGLE_API_KEY'] = 'AIzaSyBVt_LVFB7ble_8oKoyHQNYoQd7LGQkwg8'

# genai.configure(api_key= os.environ['GOOGLE_API_KEY'])

# model = genai.GenerativeModel('gemini-pro')

# os.environ['OPENAI_API_KEY'] = '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'

def generate_response(txt):
    llm = OpenAI(temperature = 0, openai_api_key = openai_api_key)

    text_splitter = CharacterTextSplitter()
    
    texts = text_splitter.split_text(txt)

    docs = [Document(page_content=t) for t in texts]

    chain = load_summarize_chain(llm, chain_type= 'map_reduce')

    return chain.run(docs)

st.set_page_config(page_title= 'Text Summarization', page_icon="🦜")

st.title('Text Summarization')

#Text input
txt_input = st.text_area('Enter your text', '', height= 200)

result = []

with st.form('summarize-form', clear_on_submit=True):
    openai_api_key = st.text_input('OpenAI API Key', type= 'password', disabled= not txt_input  )
    
    submitted = st.form_submit_button('Submit')

    if submitted and openai_api_key.startswith('sk-'):
        with st.spinner("Calculating..."):
            response = generate_response(txt_input)
            result.append(response)
            del openai_api_key

if len(result):
    st.info(response)










































# response = model.generate_content('List 5 planets each with interesting facts')

# Markdown(response.text)

# import streamlit as st
# from langchain import LangChain
# from gemini import Gemini
# from rag import RAG

# # Load the RAG model
# rag = RAG()
# rag.load("path/to/rag_model")

# # Load the Gemini model
# gemini = Gemini()
# gemini.load("path/to/gemini_model")

# # Load the text file containing the input text
# with open("path/to/input_text.txt", "r") as f:
#     input_text = f.read()

# # Use the RAG model to generate a response from the input text
# rag_response = rag.generate(input_text)

# # Use the Gemini model to generate a chatbot response from the RAG response
# gemini_response = gemini.generate(rag_response)

# # Display the chatbot response in the Streamlit app
# st.write(gemini_response)import streamlit as st
# from langchain import LangChain
# from gemini import Gemini
# from rag import RAG

# # Load the RAG model
# rag = RAG()
# rag.load("path/to/rag_model")

# # Load the Gemini model
# gemini = Gemini()
# gemini.load("path/to/gemini_model")

# # Load the text file containing the input text
# with open("path/to/input_text.txt", "r") as f:
#     input_text = f.read()

# # Use the RAG model to generate a response from the input text
# rag_response = rag.generate(input_text)

# # Use the Gemini model to generate a chatbot response from the RAG response
# gemini_response = gemini.generate(rag_response)

# # Display the chatbot response in the Streamlit app
# st.write(gemini_response)
