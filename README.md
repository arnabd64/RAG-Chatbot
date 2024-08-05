# Chatbot with RAG Capabilities

## Description

This project aims to develop a **Chatbot with Retrieval-Augmented Generation (RAG) capabilities**. The chatbot is designed to provide completely private conversations by using your own documents, ensuring no data is shared with third parties. It leverages advanced technologies and tools to offer an efficient and secure chat experience.

### Key Features

1. **Completely Private Chats:** The chatbot utilizes your private documents for generating responses, ensuring complete privacy.
2. **Data Privacy:** No data is shared with third parties.
3. **LLM and Document Embedding:** Powered by Ollama, providing high-quality language model and document embeddings.
4. **Chat History Management:** Chat history is stored in a self-hosted MongoDB instance.
5. **Document Embedding Storage:** Document embeddings are stored in a self-hosted Chroma DB instance.
6. **Multi-format Support:** Supports PDF, markdown, and simple text files.

### Technologies and Packages

The following Python packages are used in this project:

```
langchain==0.2.10
langchain-community==0.2.9
langchain-text-splitters
langchain-chroma
langchain-mongodb
chromadb
pypdf
python-dotenv
```

### Deployment

To run the chatbot on your own server, use the following command:

```bash
docker compose up -d
```

This command will set up the necessary environment and start the services in detached mode.

### Conclusion

The Chatbot with RAG Capabilities is a robust solution for private and secure conversations, leveraging state-of-the-art technologies to provide an efficient and user-friendly experience.