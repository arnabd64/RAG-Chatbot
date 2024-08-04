#!/bin/bash

# Start Ollama in the background.
ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Retrieving model llama2..."
ollama pull llama2
echo "🟢 Done llama2!"
echo "🔴 Retrieving model all-minilm..."
ollama pull all-minilm
echo "🟢 Done all-minilm!"


# Wait for Ollama process to finish.
wait $pid