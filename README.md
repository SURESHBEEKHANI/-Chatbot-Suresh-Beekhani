# Chatbot-Suresh-Beekhani


## Overview
This project is a chatbot application built using Flask, LangChain, and Qdrant. The chatbot leverages advanced machine learning models to provide intelligent responses to user queries. It integrates with Hugging Face for embeddings and uses a custom prompt configuration for chat interactions.

## Prerequisites
- Python 3.8+
- Flask
- LangChain
- Qdrant
- Hugging Face
- Docker (optional for containerization)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Chatbot-Suresh-Beekhani.git
   cd Chatbot-Suresh-Beekhani

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

qdrant_api_key=your_qdrant_api_key
groq_API_KEY=your_groq_api_key

python app.py

Chatbot-Suresh-Beekhani/
│
├── app.py                  # Main application file
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
├── static/                 # Static files (CSS, JS, images)
│   ├── styles.css
│   └── script.js
├── templates/              # HTML templates
│   └── index.html
├── src/                    # Source files
│   ├── helper.py
│   ├── prompt.py
│   └── __pycache__/
└── README.md               # Project documentation

Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details. ```


