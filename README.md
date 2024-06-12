# Gnosis GPT

Gnosis GPT is a chatbot that allows you to upload files and chat with them using ChatGPT or Anthropic.

This was a commissioned prototype we developed in early 2023.  The goal was to briefly explore the business potential of RAG (Retrieval Augmented Generation) and private GPT's and the flexibility of being able to toggle between several LLM's and prompting styles.  Basic chatgpt wrappers were being showered with VC money at the time.

As OpenAI released new features like built-in RAG, memory, system prompts, and custom GPT's this project and many like it became non-viable business ideas.

However this was a great way to get intimate with the hot new hotness at the time - vector databases, langchain, as well as pushing the boundaries of streamlit (we started out with gradio).

## Project Stack

- Langchain - simplifies RAG, built-in document loaders like txt, pdf, etc, and provides prompt templates
- Chroma DB - free fast local vector store for RAG, great for proof of concepts
- Streamlit - easily create simple web interfaces in python

## Getting Started

These instructions will get you up and running locally.

### Prerequisites

Make sure you have the following installed before continuing:

- Python 3.10 or higher
- Pip
- Virtualenv


### Installing

- Clone the repository

```bash
git clone git@github.com:esoteric_git/gnosis-gpt.git && cd gnosis-gpt
```

- Create a virtual environment

```bash
virtualenv .venv
```

- Activate the virtual environment

```bash
source .venv/bin/activate
```

- Install the dependencies

```bash
pip install -r requirements.txt
```

- Add your credentials to secrets file

- Run the app

```bash
streamlit run main.py
```
