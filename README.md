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

Before running the above command, make sure to create a `.env` file with the following environment variables.

| Variable            | Description                     |
|-------------------- |-------------------------------- |
| `MONGO_USERNAME`    | MongoDB username                |
| `MONGO_PASSWORD`    | MongoDB password                |
| `MONGO_HOST`        | MongoDB host                    |
| `MONGO_PORT`        | MongoDB port                    |
| `OLLAMA_HOST`       | Ollama host                     |
| `OLLAMA_PORT`       | Ollama port                     |
| `OLLAMA_EMBED`      | Ollama embed type               |
| `OLLAMA_LLM`        | Ollama LLM model                |
| `OLLAMA_TIMEOUT`    | Ollama timeout (in seconds)     |
| `OLLAMA_KEEPALIVE`  | Ollama keep-alive duration (in seconds) |
| `CHROMA_HOST`       | Chroma DB host                  |
| `CHROMA_PORT`       | Chroma DB port                  |
| `ME_USER`           | Mongo Express username          |
| `ME_PASSWORD`       | Mongo Express password          |
| `ME_PORT`           | Mongo Express port              |


### Conclusion

The Chatbot with RAG Capabilities is a robust solution for private and secure conversations, leveraging state-of-the-art technologies to provide an efficient and user-friendly experience.