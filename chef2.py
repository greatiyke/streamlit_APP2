import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate

st.set_page_config(page_title="A Chef App")
st.title('A Chef App')
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(cuisine, dietary_preference, allergy, ingredient_1, ingredient_2,ingredient_3, wine):
    llm = OpenAI(temperature=1.0, openai_api_key=openai_api_key)
    # Prompt
    template = f"""I am a Chef.  I need to create {cuisine} \n
recipes for customers who want {dietary_preference} meals. \n
However, don't include recipes that use ingredients with the customer's {allergy} allergy. \n
I have {ingredient_1}, \n
{ingredient_2}, \n
and {ingredient_3} \n
in my kitchen and other ingredients. \n
The customer's wine preference is {wine} \n
Please provide some for meal recommendations.
For each recommendation include preparation instructions,
time to prepare
and the recipe title at the begining of the response.
Then include the wine paring for each recommendation.
At the end of the recommendation provide the calories associated with the meal
and the nutritional facts.
"""
    prompt = PromptTemplate(input_variables=['cuisine', 'dietary_preference','allergy', 'ingredient_1', 'ingredient_2', 'ingredient_3', 'wine' ], template=template)
    prompt_query = prompt.format(cuisine=cuisine, dietary_preference=dietary_preference, allergy=allergy, ingredient_1=ingredient_1, ingredient_2=ingredient_2, ingredient_3=ingredient_3, wine=wine)
    # Run LLM model and print out response
    response = llm(prompt_query)
    return st.info(response)
with st.form('myform'):
    cuisine = st.selectbox(
    "What cuisine do you desire?",
    ("American", "Chinese", "French", "Indian", "Italian", "Japanese", "Mexican", "Turkish", "Nigerian"),
    index=None,
    placeholder="Select your desired cuisine."
    )

    dietary_preference = st.selectbox(
    "Do you have any dietary preferences?",
    ("Diabetese", "Glueten free", "Halal", "Keto", "Kosher", "Lactose Intolerance", "Paleo", "Vegan", "Vegetarian", "None"),
    index=None,
    placeholder="Select your desired dietary preference."
    )

    allergy = st.text_input(
    "Enter your food allergy:  \n\n", key="allergy", value="peanuts"
    )

    ingredient_1 = st.text_input(
    "Enter your first ingredient:  \n\n", key="ingredient_1", value="ahi tuna"
    )

    ingredient_2 = st.text_input(
    "Enter your second ingredient:  \n\n", key="ingredient_2", value="chicken breast"
    )

    ingredient_3 = st.text_input(
    "Enter your third ingredient:  \n\n", key="ingredient_3", value="tofu"
    )
    wine = st.radio (
    "What wine do you prefer?\n\n", ["Red", "White", "None"], key="wine", horizontal=True
    )
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(cuisine, dietary_preference, allergy, ingredient_1, ingredient_2, ingredient_3, wine)

