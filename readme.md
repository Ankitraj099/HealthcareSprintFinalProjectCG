# Intelligent Healthcare AI System

# Enterprise AI-Powered Healthcare Platform

An enterprise-grade AI healthcare platform integrating:

- Machine Learning
- Multi-Agent AI
- Retrieval-Augmented Generation (RAG)
- Cloud Deployment
- Docker Containerization
- Azure Services
- CI/CD Automation

# Project Overview

The Intelligent Healthcare AI System is designed to:

  Predict diabetes risk using Machine Learning  
  Store and manage patient healthcare records  
  Provide AI-powered healthcare assistance  
  Enable document-based medical AI chat using RAG  
  Generate healthcare analytics and insights  
  Deploy seamlessly using Docker + Azure + GitHub Actions  

This project demonstrates a complete enterprise AI architecture using modern cloud-native technologies.

---

# Complete System Architecture

                    ┌─────────────────────┐
                    │      USER/API       │
                    └─────────┬───────────┘
                              │
                              ▼
                  ┌────────────────────────┐
                  │      FASTAPI SERVER    │
                  └─────────┬──────────────┘
                            │
        ┌───────────────────┼────────────────────┐
        │                   │                    │
        ▼                   ▼                    ▼

 ┌──────────────┐   ┌────────────────┐   ┌────────────────┐
 │ ML MODEL     │   │ MULTI AGENT AI │   │ RAG SYSTEM     │
 │ Prediction   │   │ Healthcare AI  │   │ Medical Docs   │
 └──────┬───────┘   └──────┬─────────┘   └────────┬───────┘
        │                  │                      │
        ▼                  ▼                      ▼

 ┌──────────────┐   ┌───────────────┐    ┌────────────────┐
 │ Azure Blob   │   │ Azure OpenAI  │    │ Vector Database│
 │ Storage      │   │ LLM           │    │ Embeddings     │
 └──────────────┘   └───────────────┘    └────────────────┘

                            │
                            ▼

                   ┌────────────────┐
                   │ MongoDB Atlas  │
                   │ Patient Records│
                   └────────────────┘


# Deployment Architecture


Developer
   ↓
GitHub Repository
   ↓
GitHub Actions CI/CD
   ↓
Docker Image Build
   ↓
Docker Hub
   ↓
Azure App Service
   ↓
FastAPI Container
   ↓
Live Healthcare APIs


# Technology Stack

 Technology -- Purpose 

 FastAPI - Backend API Framework 
 Python - Core Development 
 Scikit-learn - Machine Learning 
 MongoDB Atlas - NoSQL Database 
 Azure Blob Storage - Cloud Storage 
 Azure OpenAI - LLM Integration 
 Docker - Containerization 
 GitHub Actions - CI/CD 
 HuggingFace - Embeddings 
 FAISS - Vector Search 
 Joblib - ML Model Serialization 


# Project Structure

HealthcareSprintFinalProjectCG/
│
├── api/
│   ├── app.py
│   └── routes/
│       ├── prediction.py
│       ├── patient.py
│       ├── rag_chat.py
│       ├── analytics.py
│       └── agent_chat.py
│
├── agents/
│   ├── healthcare_agent.py
│   ├── analytics_agent.py
│   ├── medical_rag_agent.py
│   └── orchestrator_agent.py
│
├── rag/
│   ├── retriever.py
│   ├── vector_store.py
│   └── embeddings.py
│
├── src/
│   └── models/
│       ├── diabetes_model.pkl
│       ├── scaler.pkl
│       ├── gender_encoder.pkl
│       └── smoking_encoder.pkl
│
├── database/
│   └── mongodb.py
│
├── utils/
│   └── azure_blob.py
│
├── deployment/
│   └── Dockerfile
│
├── .github/
│   └── workflows/
│       └── azure-deploy.yml
│
├── requirements.txt
├── README.md
└── .env


# API Workflows

# Health Check API

## Endpoint

GET /health

## Purpose

Checks whether the backend service is running successfully.

## Workflow

Client Request
      ↓
FastAPI Route
      ↓
Health Validation
      ↓
JSON Response


# Diabetes Prediction API

## Endpoint

POST /predict

## Complete Workflow

Patient Data
      ↓
Request Validation
      ↓
Feature Encoding
      ↓
Feature Scaling
      ↓
ML Model Prediction
      ↓
Prediction Logging
      ↓
Azure Blob Storage
      ↓
Response to User

## Input Example

 json
{
  "gender": "Male",
  "age": 45,
  "hypertension": 1,
  "heart_disease": 0,
  "smoking_history": "former",
  "bmi": 31.5,
  "HbA1c_level": 7.2,
  "blood_glucose_level": 180
}

## Internal Processing

### Step 1 — Encoding
Categorical values are converted into numerical form using:
- LabelEncoder
- Gender Encoder
- Smoking History Encoder

### Step 2 — Scaling
Features normalized using:
- StandardScaler

### Step 3 — Prediction
ML model predicts:
- Diabetic
- Non-Diabetic

### Step 4 — Cloud Logging
Prediction stored inside Azure Blob Storage.

# 3️⃣ Add Patient API

## Endpoint

POST /add-patient

## Workflow

Client Request
      ↓
Pydantic Validation
      ↓
MongoDB Insert
      ↓
Patient Record Stored
      ↓
Success Response

# Patient History API

## Endpoint

GET /patient-history

## Workflow

Request
    ↓
MongoDB Query
    ↓
Fetch Patient Records
    ↓
JSON Response

# Multi-Agent AI System

# What is Agentic AI?

Instead of using one AI model for everything, the system uses multiple specialized AI agents.

Each agent performs a dedicated healthcare task.


# Multi-Agent Workflow Diagram

                     USER QUERY
                          │
                          ▼
               ┌──────────────────┐
               │ ORCHESTRATOR AI  │
               └────────┬─────────┘
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼

┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ Symptom Agent  │ │ RAG Agent      │ │ Analytics Agent│
│ Disease Logic  │ │ Medical Search │ │ Data Insights  │
└────────┬───────┘ └────────┬───────┘ └────────┬───────┘
         │                  │                  │
         └──────────────────┼──────────────────┘
                            │
                            ▼
                 ┌────────────────────┐
                 │ Final AI Response  │
                 └────────────────────┘


# Available Agents

 Agent - Responsibility 

 Medical RAG Agent - Medical knowledge retrieval 
 Analytics Agent - Healthcare analytics 
 Symptom Agent - Disease reasoning 
 Recommendation Agent - Healthcare recommendations 
 Orchestrator Agent - Agent coordination 


# Agent Chat API

## Endpoint

POST /agent-chat

## Workflow

User Query
      ↓
Orchestrator Agent
      ↓
Agent Selection
      ↓
AI Reasoning
      ↓
Aggregated Response
      ↓
Final Output


# RAG (Retrieval-Augmented Generation)

# What is RAG?

RAG is an advanced AI architecture where the AI retrieves relevant information from documents before generating a response.

This reduces hallucination and improves factual accuracy.


# RAG Architecture Diagram

                  USER QUESTION
                        │
                        ▼
            ┌────────────────────┐
            │ Embedding Creation │
            └─────────┬──────────┘
                      │
                      ▼
            ┌────────────────────┐
            │ Vector Database    │
            │ (FAISS Search)     │
            └─────────┬──────────┘
                      │
          Relevant Medical Chunks
                      │
                      ▼
            ┌────────────────────┐
            │ Azure OpenAI LLM   │
            └─────────┬──────────┘
                      │
                      ▼
             AI Medical Response


# RAG Workflow

User Question
      ↓
Embedding Generation
      ↓
Vector Similarity Search
      ↓
Relevant Medical Chunks Retrieved
      ↓
Context Sent to LLM
      ↓
Grounded AI Response


# Internal RAG Components

 Component - Purpose 

 HuggingFace Embeddings - Convert text into vectors 
 FAISS Vector Store - Similarity search 
 Medical Documents - Knowledge source 
  Azure OpenAI - Final answer generation 


# Document Assistant Agent

## Endpoint

POST /Document Assistant Agent

## Workflow

Medical Question
      ↓
Embedding Generation
      ↓
Document Retrieval
      ↓
Relevant Context Extraction
      ↓
Azure OpenAI Response
      ↓
Medical AI Answer

# Analytics Agent

## Endpoint

POST /analytics-agent

## Workflow

Prediction History
      ↓
Azure Blob Storage
      ↓
Analytics Processing
      ↓
AI Analysis
      ↓
Healthcare Insights


# Power BI Integration

The system supports Power BI integration using prediction datasets stored in Azure Blob Storage.

Possible dashboards:
- Prediction trends
- Risk distribution
- Patient demographics
- Healthcare analytics


# Docker Containerization

The application is fully containerized using Docker.

Benefits:
- Consistent deployment
- Scalable infrastructure
- Environment portability
- Cloud-native architecture


# CI/CD Pipeline

GitHub Actions automatically:

1. Detects code changes
2. Builds Docker image
3. Pushes updated image
4. Deploys to Azure App Service


# CI/CD Workflow Diagram

Developer Push Code
          │
          ▼
┌─────────────────────┐
│ GitHub Repository   │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ GitHub Actions      │
│ CI/CD Pipeline      │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Docker Image Build  │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Docker Hub Push     │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Azure App Service   │
└─────────┬───────────┘
          │
          ▼
     Live Deployment


#  Azure Services Used

 Azure Service - Purpose 

 Azure App Service - Application hosting 
 Azure Blob Storage - Prediction storage 
 Azure OpenAI - AI model integration 
 Azure Container Support - Docker deployment 


# Security Features

- Environment variables for secrets
- Cloud-based API keys
- Secure Azure deployment
- MongoDB Atlas authentication
- Docker container isolation


# Enterprise-Level Features

  Machine Learning Deployment  
  RAG Architecture  
  Multi-Agent AI  
  Cloud-Native Deployment  
  Docker Containerization  
  CI/CD Automation  
  Azure Integration  
  NoSQL Database  
  AI Analytics  
  REST APIs  


# Future Enhancements

- Real-time patient monitoring
- Voice-based healthcare assistant
- Medical image analysis
- Advanced analytics dashboard
- Multi-language support 
