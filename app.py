import streamlit as st
import os
from together import Together
import re
import json
import google.generativeai as genai

# Add API Keys before running
genaiAPI = "AIzaSyCiVJZmXhOOc-SrwKx4KH6JXONvFEhMbnA"
client = Together(api_key='e669705bf878b77a559f5dd9515caeb848ad23d245bcf532f458ff5f9d52a030')

# Summarize paragraphs using the Google Generative AI API
def summarize_paragraphs(paragraphs, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
    prompt = f"Summarize the following text: {paragraphs}"
    response = model.generate_content(prompt)
    summary = response.text.split("\n")[0].strip()
    return summary

# Function to get the last paragraph and its number
def get_last_paragraph_and_summary(data):
    paragraphs = data.strip().split('\n')
    last_paragraph = paragraphs[-1] if paragraphs else ""
    previous_paragraphs = paragraphs[:-1] if len(paragraphs) > 1 else []
    summary = summarize_paragraphs(previous_paragraphs, genaiAPI)
    paragraph_number = len(paragraphs)
    return summary, last_paragraph, paragraph_number

# Function to create analysis prompt
def create_prompt(summary, last_paragraph, paragraph_number, book_type, book_title):
    return f"""
    I am writing a {book_type} and This is paragraph {paragraph_number}. The title in my mind is {book_title}.
    Here is a summary of the previous paragraphs: {summary}
    Analyse the last paragraph and give me ways to improve: {last_paragraph}.
    After analysing, give a json output for :
    'Overall interest' [A floating value out of 10],
    Vivid Rating [A floating value out of 10],
    Build up: [Strong, Weak, Average],
    Irregularities: [if any],
    References: [Some reference book titles and authors],
    Summary : (summary of the paragraph),
    Suggestions: ,
    Strengths,
    Weaknesses.
    """

# Function to request analysis and suggestions from the model
def analyze_paragraph(prompt):
    stream = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-70B-Instruct-Turbo",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
    return response

# Function to convert analysis response to JSON
def jsonResponse(response, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
    prompt = f"Make this {response} as a json with keys 'Overall interest','Vivid Rating','Build up','Irregularities','References' (Dont use any special characters here),'Summary','Suggestions','Strengths','Weaknesses'"
    response = model.generate_content(prompt)
    jsonTry = response.text
    return jsonTry

# Initialize the app
def main():
    st.title("Novel Writing App")

    book_title = st.text_input("Book Title")
    book_type = st.text_input("Book Type")
    novel_text = st.text_area("Write your novel here...", height=300, key="novel_text")

    if st.button("Analyze Paragraph"):
        if book_title and book_type and novel_text:
            summary, last_paragraph, paragraph_number = get_last_paragraph_and_summary(novel_text)
            prompt = create_prompt(summary, last_paragraph, paragraph_number, book_type, book_title)
            response = analyze_paragraph(prompt)
            jsonRaw = jsonResponse(response, genaiAPI)
            jsonRaw = jsonRaw.replace("\n", "").replace("  ", "").replace("json", "").replace("`", "")
            jsonData = json.loads(jsonRaw)

            st.subheader("Analysis Result")
            st.json(jsonData)
        else:
            st.error("Please fill in all fields to analyze your paragraph.")

    st.subheader("Current Content")
    st.write(f"**Title**: {book_title}")
    st.write(f"**Type**: {book_type}")
    st.write("**Content**:")
    st.write(novel_text)

# Run the app
if __name__ == "__main__":
    main()
