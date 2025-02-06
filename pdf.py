import PyPDF2
import streamlit as st
from groq import Groq

# Initialize Groq client
client = Groq(
    api_key="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",
)

st.title("PDF Content Analyzer with Groq Cloud")

# Upload PDF file
uploaded_pdf = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_pdf is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_pdf)
    pdf_content = ""
    
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            pdf_content += text + "\n\n"
    
    st.subheader("Extracted Text from PDF:")
    st.markdown(f"""<div style='background-color: #f4f4f4; padding: 10px; border-radius: 5px;'>
                  <pre>{pdf_content}</pre>
                  </div>""", unsafe_allow_html=True)
    
    if st.button("Analyze PDF Content with Groq Cloud"):
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": f"""Analyze and summarize:\n\n{pdf_content}"""}],
            model="llama3-8b-8192",
        )
        analysis_result = response.choices[0].message.content
        
        # Display the formatted output
        st.subheader("Analysis Result:")
        st.markdown(f"""<div style='background-color: #e8f0fe; padding: 10px; border-radius: 5px;'>
                      <p style='white-space: pre-wrap;'>{analysis_result}</p>
                      </div>""", unsafe_allow_html=True)
