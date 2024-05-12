
# EncryptedPDFQuery

EncryptedPDFQuery offers reading functionality alongside querying from multiple PDFs at a time. 

Whether you're analyzing reports, studying research papers, or reviewing documents with sensitive information, we've got you covered.

With our anonymization feature, rest assured that your data remains confidential while allowing you to extract valuable insights. 

Explore, search, and analyze your PDFs like never before with our intuitive and secure platform.

## How It Works
------------

The application follows these steps to respond to your questions:

1. PDF Loading: The app reads multiple PDF documents and extracts their text content.

2. Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.

3. Language Model: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.

4. Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.

5. Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.



## Demo

Insert gif or link to demo

https://abhishekwazal-encryptedpdfquery-app-h037kp.streamlit.app/
## Technologies and Libraries used

streamlit

langchain

Google Gemini

PyPDF2

langchain

Presidio Anonymizer

Faiss
