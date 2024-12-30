from langchain_google_genai import GoogleGenerativeAIEmbeddings
def get_google_embeddings():
    """Download and return the Google Generative AI embeddings."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return embeddings

