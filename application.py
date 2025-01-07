import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

api_key = "AIzaSyA_6_Fsk9oW6Hc1CYPxafgy2d7awXjT0GQ"

# Initialize the ChatGoogleGenerativeAI model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.6,
    api_key=api_key
)

prompt = PromptTemplate(
    input_variables=["code_snippet", "code_language"],
    template=(
                """ 
        You are an intelligent assistant. Here is the programming language and code:
    
        Programming Language: {code_language}
        Code Snippet:
        {code_snippet}
    
        Based on the above data, answer the following questions:
    
        1. Provide the strengths of the code.
        2. Identify any weaknesses or potential improvements.
        3. Suggest an improved version of the code.
    
        If the provided code doesn't match the specified language ({code_language}), respond with: 
        "The given code does not match the specified language: {code_language}."
        """
        )
)

chain = LLMChain(llm=llm, prompt=prompt)

st.set_page_config(page_title="Code Mentor", layout="centered")

st.title("Code Mentor 🧑‍🏫🧑‍💻")

st.sidebar.title("")
# Language selection in sidebar
language = st.sidebar.selectbox("Pick a programming language",
                                ("Python", "JavaScript", "Java", "C++", "Ruby", "Go", "Swift", "C#"))

# Code input in sidebar
code_input = st.sidebar.text_area("Enter your code:", height=300)

# Add submit button
submit_button = st.sidebar.button("Submit")
# import json
# When the submit button is clicked
if submit_button:
    if code_input:  # Ensure there's code to analyze
        # Display the entered code in the main area
        st.write("You entered the following code:")
        st.code(code_input, language=language)

        # Run the LangChain model to analyze and improve the code
        response = chain.run(code_snippet=code_input, code_language=language)
        # Display the analysis response clearly with formatting
        st.write("### Code Analysis and Improvement:")

        # Display the response clearly using Markdown
        response = response.split("3. Suggest an improved version of the code.")  # Split to separate sections
        content = response[0].strip()
        # Display strengths and weaknesses in Markdown format
        st.markdown(content)
        # If you want to show the full response in a scrollable box:
        st.text_area("Full Response", value=response, height=300, max_chars=None, key="full_response", disabled=True)

else:

    st.warning("Please enter some code before submitting.")
