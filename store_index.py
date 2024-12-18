from langchain_community.document_loaders import DirectoryLoader  # For loading documents from a directory
from langchain.document_loaders import PyPDFLoader  # For processing PDF files
from langchain.text_splitter import RecursiveCharacterTextSplitter  # For splitting text into smaller chunks
from langchain.embeddings import HuggingFaceEmbeddings  # For obtaining embeddings from a Hugging Face model
from langchain_qdrant import QdrantVectorStore  # For integrating with the Qdrant vector store

def load_and_split_pdfs(folder_path, chunk_size, chunk_overlap):
    """
    Load PDFs from a specified folder and split their content into chunks using custom separators.

    Args:
        folder_path (str): Path to the folder containing PDF files.
        chunk_size (int): Maximum size of each chunk.
        chunk_overlap (int): Overlap between consecutive chunks.

    Returns:
        list: A list of document chunks after splitting.
    """
    
    # Initialize a DirectoryLoader to load all PDF files from the given folder
    loader = DirectoryLoader(
        folder_path,        # Path to the folder containing PDF files
        glob="*.pdf",       # File pattern to match (only PDFs)
        loader_cls=PyPDFLoader  # Loader class to handle PDF files
    )
    
    # Load all the documents from the specified folder
    documents = loader.load()

    # Define a list of separators to use when splitting text
    separators = [
        "\n\n",    # Paragraph break
        "\n",      # Line break
        " ",       # Space
        ".",       # Full stop
        ",",       # Comma
        "\u200b",  # Zero-width space
        "\uff0c",  # Fullwidth comma
        "\u3001",  # Ideographic comma
        "\uff0e",  # Fullwidth full stop
        "\u3002",  # Ideographic full stop
        ""         # Empty separator as fallback
    ]

    # Create an instance of RecursiveCharacterTextSplitter with custom settings
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,         # Maximum size of each chunk
        chunk_overlap=chunk_overlap,  # Number of overlapping characters between chunks
        separators=separators         # Custom separators for splitting
    )
    
    # Use the text splitter to split the loaded documents into smaller chunks
    return text_splitter.split_documents(documents)

def download_hugging_face_embeddings():
    """
    Download and initialize Hugging Face embeddings.

    Returns:
        HuggingFaceEmbeddings: Initialized embedding model.
    """
    # Initialize the Hugging Face embeddings with the specified model
    embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')
    return embeddings
