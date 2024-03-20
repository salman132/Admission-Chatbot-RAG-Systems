# University Admission Q&A Chatbot

Welcome to our University Admission Q&A Chatbot project! This interactive chatbot is designed to assist users with questions related to university admission using Langchain and OpenAI technologies.

## Overview

Our project utilizes Langchain for natural language processing and OpenAI for generating responses to user queries. By embedding university admission-related information into a vector database hosted on Pinecone, our chatbot can efficiently retrieve relevant information and provide accurate responses to user inquiries.

## How to Use

To run the project, follow these simple steps:

1. **Create Pinecone Database**: Create your own vector database on Pinecone and obtain the API key. Ensure that the index name is set to "collegeinfo" and the dimension is 3072.

2. **Install Requirements**: Install all the necessary dependencies by executing the following command:
    ```
    pip install -r requirements.txt
    ```

3. **Configure API Keys**: Place all the required API keys in the `.env` file.

4. **Provide Data**: Place the JSON file containing university admission information in the same directory as `main.py`.

5. **Run Embedding**: Execute `main.py` to embed the data and store it in the Pinecone database.

6. **Query Data**: Use `query.py` to ask queries to the embedded data and interact with the chatbot.

## Files Overview

- **main.py**: Python script for embedding university admission data and storing it in the Pinecone database.
- **query.py**: Python script for querying the embedded data and interacting with the chatbot.
- **requirements.txt**: Text file containing a list of dependencies required for the project.
- **.env**: Configuration file for storing API keys.

## Contributors

- [Tanzir](https://github.com/DICEYCorpo/)

## Feedback

If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request. We appreciate your feedback!
