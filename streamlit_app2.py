import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate

st.set_page_config(page_title="Joke Generator App")
st.title('Joke Generator App')
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(topic):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  # Prompt
  template = 'Tell me a joke about ({topic}, make it funny)'
  prompt = PromptTemplate(input_variables=['topic'], template=template)
  prompt_query = prompt.format(topic=topic)
  # Run LLM model and print out response
  response = llm(prompt_query)
  return st.info(response)

with st.form('myform'):
  topic_text = st.text_input('Enter keyword:', '')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(topic_text)