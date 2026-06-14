# 🚀 Acko Insurance AI & Analytics Platform

## Overview

Acko Insurance AI Platform is an end-to-end AI-powered insurance solution that combines:

* AI Chatbot (RAG)
* Premium Prediction Engine
* Claim Prediction Engine
* Damage Image Analysis using Gemini Vision
* PostgreSQL Data Storage
* Streamlit Management Dashboard
* AI Manager Assistant

The platform simulates real-world insurance workflows including quote generation, claim processing, business analytics, and intelligent customer support.

---

## Features

### 1. AI Insurance Chatbot

* RAG-based chatbot
* Answers questions from insurance policy documents
* Uses ChromaDB vector database
* Powered by Groq LLM

### 2. Premium Prediction Engine

Predicts insurance premium for:

* Bike Insurance
* Car Insurance
* Health Insurance

### Model Performance

| Model          | R² Score |
| -------------- | -------- |
| Bike Premium   | 0.9826   |
| Car Premium    | 0.9880   |
| Health Premium | 0.9073   |

---

### 3. Claim Prediction Engine

Predicts:

* Claim Amount
* Claim Approval Probability

#### Bike Claim Models

* Claim Amount R²: 0.8379
* Approval Accuracy: 90.92%

#### Car Claim Models

* Claim Amount R²: 0.8571
* Approval Accuracy: 90.78%

---

### 4. Damage Analysis AI

Uses Gemini Vision to analyze uploaded vehicle damage images.

Provides:

* Damage Type
* Affected Parts
* Severity Level
* Severity Score

---

### 5. PostgreSQL Integration

Stores:

* Quotations
* Claims
* Chat Logs

---

### 6. Streamlit Dashboard

Provides:

* Total Quotations
* Total Claims
* Chatbot Usage Statistics
* Business KPIs
* Interactive Analytics

---

### 7. Manager AI Assistant

Allows managers to ask business questions such as:

* Total quotations generated
* Total claims submitted
* Average claim amount
* Manual review claims

---

## Technology Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Flask
* Streamlit

### Machine Learning

* Scikit-learn
* Random Forest

### Generative AI

* Groq LLM
* Google Gemini Vision

### Vector Database

* ChromaDB

### Embeddings

* HuggingFace Sentence Transformers

### Database

* PostgreSQL
* SQLAlchemy

---

## Project Structure

```text
app/
claim_ai/
dashboard/
database/
manager_ai/
ml_model/
rag_chatbot/
data/
```

---

## Installation

```bash
git clone <repository-url>

cd Acko-AI-Platform

pip install -r requirements.txt
```

---

## Run Flask Application

```bash
python app/app.py
```

---

## Run Dashboard

```bash
streamlit run dashboard/dashboard.py
```

---


