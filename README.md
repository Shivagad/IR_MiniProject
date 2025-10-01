# 📄 Hugging Face Document Summarizer

## **Project Description**

This is a web-based **Document Summarization System** built using **Streamlit** and **Hugging Face Transformers**.
The application allows users to either **enter text manually** or **upload documents** (`.txt`, `.pdf`, `.docx`) and generates a concise **summary** of the content.

The summarizer uses the **BART transformer model** (`facebook/bart-large-cnn`) for **abstractive summarization**. For long documents, it automatically splits the text into chunks to handle the model's token limits.

---

## **Features**

* Summarize **text input** directly.
* Summarize **uploaded documents** (`.txt`, `.pdf`, `.docx`).
* **Progress bar** for long documents to show summarization progress.
* **Download summary** as a `.txt` file.
* Simple and interactive **web interface** using Streamlit.
* Handles long documents by chunking text for the transformer model.

---

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/Shivagad/IR_MiniProject.git
```

2. Navigate to the project folder:

```bash
cd IR_MiniProject
```

3. Install required libraries:

```bash
pip install streamlit transformers torch PyPDF2 python-docx
```

---

## **Usage**

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Open the app in your browser.

3. **Option 1: Enter text**

   * Paste or type text in the text area.
   * Click **"Summarize Text"**.
   * View the summary and optionally download it as a `.txt` file.

4. **Option 2: Upload a document**

   * Upload a `.txt`, `.pdf`, or `.docx` file.
   * Click **"Summarize File"**.
   * View the summary and optionally download it as a `.txt` file.

---

## **Results**

Below is a screenshot of the application interface:

![App Screenshot](result.jpg)


* The summary is displayed below the input.
* Users can **download the summarized content** using the download button.
* Progress bar shows summarization for long documents.

---

## **Dependencies**

* Python 3.8 or higher
* Streamlit
* Hugging Face Transformers
* PyTorch
* PyPDF2
* python-docx

---

## **Acknowledgements**

* [Hugging Face Transformers](https://huggingface.co/transformers/)
* [Streamlit](https://streamlit.io/)
