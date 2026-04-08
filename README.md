# Pet Name Generator (Streamlit + LangChain + Ollama)

A small app that generates pet names based on animal type and color.

## Features

- Streamlit UI for quick input
- LangChain prompt templating
- Local LLM inference with Ollama

## Tech Stack

- Python 3.10+
- Streamlit
- LangChain
- Ollama

## Project Structure

- main.py: Streamlit app UI
- langchain_helper.py: Prompt + model logic
- requirements.txt: Python dependencies

## Prerequisites

1. Install Ollama from the official website.
2. Pull the model used by the app:
   ollama pull llama3.2:3b

## Setup

1. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt


## Run

Start the Streamlit app:

streamlit run main.py

## Notes

- The app expects Ollama to be running locally.
- If you get module import errors, verify your virtual environment is activated.
- If you get connection errors from Ollama, run: ollama serve

## License

MIT (see LICENSE)
