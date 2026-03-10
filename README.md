# LangChain Learning Repository

A structured collection of **LangChain experiments, examples, and mini-projects** created while learning how to build **LLM-powered applications**.

This repository documents my journey of understanding **prompt engineering, LLM integration, chains, agents, and Retrieval Augmented Generation (RAG)** using LangChain.

---

# 📌 Objectives

The goals of this repository are:

* Learn how to integrate **LLMs into real applications**
* Understand **LangChain architecture and abstractions**
* Build practical **GenAI backend components**
* Experiment with **RAG pipelines**
* Develop reusable **AI service patterns**

---

# 🧠 Topics Covered

This repository contains implementations and experiments related to:

* LangChain basics
* Prompt Templates
* LLM integrations (OpenAI / OpenRouter)
* Chains and Pipelines
* Output Parsing
* Tools and Agents
* Document Loaders
* Text Splitters
* Embeddings
* Vector Databases
* Retrieval Augmented Generation (RAG)

---

# 📂 Repository Structure

```
langchain-learning/
│
├── basics/
│   ├── simple_llm_call.py
│   ├── prompt_templates.py
│   └── chain_pipeline.py
│
├── integrations/
│   ├── openrouter_test.py
│   └── model_configuration.py
│
├── rag/
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── rag_pipeline.py
│
├── agents/
│   └── simple_agent.py
│
├── projects/
│   ├── chatbot_project/
│   └── rag_qa_system/
│
├── .env.example
└── requirements.txt
```

---

# ⚙️ Setup

## 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/langchain-learning.git
cd langchain-learning
```

---

## 2️⃣ Create virtual environment

```
python -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Environment variables

Create a `.env` file and add your API key.

Example:

```
OPENROUTER_API_KEY=your_api_key_here
```

---

# 🚀 Example Usage

Example: simple LangChain prompt + model pipeline.

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

model = ChatOpenAI(
    model="arcee-ai/trinity-large-preview:free",
    base_url="https://openrouter.ai/api/v1",
)

template = PromptTemplate(
    template="Explain {topic} in simple terms",
    input_variables=["topic"]
)

chain = template | model

response = chain.invoke({"topic": "RAG"})

print(response.content)
```

---

# 🧩 Projects

Some mini projects included in this repository:

### AI Chatbot

A basic chatbot built using LangChain pipelines.

### RAG Question Answering System

Uses:

* document loaders
* embeddings
* vector databases
* retrievers

to answer questions from custom documents.

---

# 🛠 Technologies Used

* Python
* LangChain
* OpenRouter
* OpenAI-compatible APIs
* Vector Databases
* Embedding Models

---

# 📚 Learning Resources

Some useful resources used while learning:

* LangChain Documentation
* FreeCodeCamp GenAI Course
* CampusX GenAI Playlist
* OpenRouter Documentation

---

# 🎯 Future Improvements

Planned additions:

* Advanced RAG pipelines
* LangGraph workflows
* Agentic AI systems
* Multi-tool agents
* Production-ready AI APIs

---

# 📜 License

This repository is created for **educational purposes** and experimentation with LangChain and LLM technologies.
