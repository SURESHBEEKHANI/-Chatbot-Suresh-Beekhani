from langchain_community.document_loaders import DirectoryLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore

def load_and_split_pdfs(folder_path, chunk_size, chunk_overlap):
    """Load PDFs from folder and split into chunks with custom separators."""
    
    # Load PDF files from the folder
    loader = DirectoryLoader(folder_path, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    # Define custom separators for splitting text
    separators = [
        "\n\n",  # Paragraph break
        "\n",    # Line break
        " ",     # Space
        ".",     # Full stop
        ",",     # Comma
        "\u200b",  # Zero-width space
        "\uff0c",  # Fullwidth comma
        "\u3001",  # Ideographic comma
        "\uff0e",  # Fullwidth full stop
        "\u3002",  # Ideographic full stop
        ""        # Empty separator
    ]

    # Create a text splitter with the given chunk size, overlap, and separators
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap,
        separators=separators
    )
    
    # Split the documents into smaller chunks
    return text_splitter.split_documents(documents)

#Download the Embeddings from Hugging Face
def download_hugging_face_embeddings():
    embeddings=HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')
    return embeddings
