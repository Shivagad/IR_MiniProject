import streamlit as st
from transformers import pipeline
import PyPDF2
import docx
import time

# Load summarization model
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

# Function to read PDF
def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    return " ".join(page.extract_text() for page in reader.pages)

# Function to read Word document
def read_docx(file):
    doc = docx.Document(file)
    return " ".join(para.text for para in doc.paragraphs)

# Summarization function with progress bar
def summarize_text(text):
    max_chunk = 1000  # model token limit
    sentences = text.split('. ')
    summary_text = ""
    chunk = ""
    
    progress = st.progress(0)
    total_sentences = len(sentences)
    
    for i, sentence in enumerate(sentences):
        if len(chunk.split()) + len(sentence.split()) < max_chunk:
            chunk += sentence + ". "
        else:
            summary_text += summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text'] + " "
            chunk = sentence + ". "
        progress.progress((i+1)/total_sentences)
        time.sleep(0.01)  # just to show progress bar smoothly
    
    if chunk:
        summary_text += summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    
    progress.progress(1.0)
    return summary_text

# Streamlit Interface
st.title("📄 Hugging Face Document Summarizer")
st.write("Enter text or upload a document (txt, pdf, docx) to get the summary.")

# Option 1: Text input
text_input = st.text_area("Enter text here", height=200)
if st.button("Summarize Text"):
    if text_input.strip():
        summary = summarize_text(text_input)
        st.subheader("Summary:")
        st.write(summary)
        
        # Download button
        st.download_button(
            label="📥 Download Summary as TXT",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )
    else:
        st.warning("Please enter some text.")

# Option 2: File upload
uploaded_file = st.file_uploader("Upload a document", type=['txt','pdf','docx'])
if uploaded_file is not None:
    file_text = ""
    if uploaded_file.type == "text/plain":
        file_text = uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        file_text = read_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        file_text = read_docx(uploaded_file)
    
    if st.button("Summarize File"):
        if file_text.strip():
            summary = summarize_text(file_text)
            st.subheader("Summary:")
            st.write(summary)
            
            # Download button
            st.download_button(
                label="📥 Download Summary as TXT",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )
        else:
            st.warning("Could not read the uploaded file.")
