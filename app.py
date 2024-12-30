from flask import Flask, render_template, jsonify, request  # Import Flask for web server and rendering templates
# Import the function to download HuggingFace embeddings
from langchain_qdrant import QdrantVectorStore
from src.helper import get_google_embeddings
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain  # Import chain to link document retrieval and model for Q&A tasks
from langchain.chains.combine_documents import create_stuff_documents_chain  # Import document processing chain for Q&A
from langchain_core.prompts import ChatPromptTemplate  # Import class to handle prompt templates for chat
from src.prompt import *  # Import custom prompt configurations from a local module
import os  # Import os module to interact with environment variables
from dotenv import load_dotenv  # Import dotenv to load environment variables from a .env file

# Initialize Flask web application
app = Flask(__name__)  # Create a Flask app instance to handle web requests

# Load environment variables from the .env file
load_dotenv()  # Load environment variables from a .env file to manage sensitive data like API keys

# Retrieve environment variables

# Retrieve API keys from environment variables
qdrant_api_key = os.environ.get('QDRANT_API_KEY')
groq_api_key = os.environ.get('GROQ_API_KEY')
google_api_key = os.environ.get('GOOGLE_API_KEY')

# Qdrant service URL and collection name
qdrant_url = "https://e92b3638-9cd8-43e3-9c5d-a049f560fab2.us-east4-0.gcp.cloud.qdrant.io"
collection_name = "skchatbot"
# Ensure API keys are set in the environment
os.environ["groq_API_KEY"] = groq_API_KEY
os.environ["qdrant_api_key"] = qdrant_api_key
os.environ["google_api_key"] = google_api_key

# Download embeddings from Hugging Face
embeddings =  get_google_embeddings()

# Initialize Qdrant vector store
qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name=collection_name,
    url=qdrant_url,
    api_key=qdrant_api_key
)

# Create a retriever for document search
retriever = qdrant.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Initialize the language model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=groq_API_KEY,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# Create a document processing chain that uses the Groq model and defined prompt
question_answer_chain = create_stuff_documents_chain(llm, prompt)

# Create a retrieval chain that links document retrieval with the Q&A chain
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Route to render the homepage (chat interface)
@app.route("/")
def index():
    return render_template('index.html')  # Render the index.html template for the homepage, showing the chat interface

# Route to handle chat messages
@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]  # Retrieve the message from the user input form via HTTP POST request
    input = msg  # Assign the message to the input variable
    print(input)  # Print the user's input to the console for debugging purposes
    response = rag_chain.invoke({"input": msg})  # Process the input message through the retrieval and Q&A chain
    print("Response: ", response["answer"])  # Print the generated response to the console for debugging
    return str(response["answer"])  # Return the response as a string to be displayed in the chat interface

# Run the Flask web server on the specified host and port
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)  # Start the app on all network interfaces at port 8080 for development
