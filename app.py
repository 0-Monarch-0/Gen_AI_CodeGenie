import streamlit as st
import time
from CodeModel import generate_code

st.set_page_config(page_title="CodeGenie", page_icon="🧠")

st.title("🧠 CodeGenie: AI-Powered Code Generator")
st.markdown("Turn your ideas into code using an AI code model!")

# Prompt input
prompt = st.text_area("🔤 Enter your code prompt:", height=200, placeholder="e.g. Write a Python function to check for prime numbers")

# Generate button
if st.button("🚀 Generate Code"):
    if prompt.strip() == "":
        st.warning("⚠️ Please enter a valid prompt.")
    else:
        with st.spinner("Generating code... please wait"):
            output, start, end = generate_code(prompt)
            st.success(f"✅ Code generated in {end - start:.2f} seconds")
            st.code(output, language="python")
