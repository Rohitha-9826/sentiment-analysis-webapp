import streamlit as st
import requests

st.title("💬 Sentiment Analysis App using Hugging Face")

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
API_TOKEN = "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"  # Replace with your actual token from Hugging Face

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def query(text):
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    
    if response.status_code == 200:
        try:
            return response.json()
        except:
            return None
    else:
        st.error(f"Error {response.status_code}: {response.text}")
        return None

user_input = st.text_area("Enter text to analyze:")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            result = query(user_input)
            if result:
                label = result[0]['label']
                score = result[0]['score']
                st.success("✅ Analysis Complete")
                st.write(f"**Sentiment:** `{label}`")
                st.write(f"**Confidence:** `{score:.2f}`")
            else:
                st.error("❌ Could not decode the response.")
