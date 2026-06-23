# Model Evaluation Report  
## Acko Insurance AI Platform

## 1. Premium Prediction Models

### Bike Premium Model
- Model Used: Random Forest Regressor
- R² Score: 0.9826
- RMSE: 1123.46
- MAE: 456.85
- Output: Predicts annual bike insurance premium
- Explainability: SHAP plot generated as `bike_premium_shap.png`

### Car Premium Model
- Model Used: Random Forest Regressor
- R² Score: 0.988
- RMSE: 9040.33
- MAE: 3475.55
- Output: Predicts annual car insurance premium
- Explainability: SHAP plot generated as `car_premium_shap.png`

### Health Premium Model
- Model Used: Random Forest Regressor
- R² Score: 0.9073
- RMSE: 32750.76
- MAE: 19202.87
- Output: Predicts annual health insurance premium
- Explainability: SHAP plot generated as `health_premium_shap.png`

---

## 2. Claim Amount Prediction Models

### Bike Claim Amount Model
- Model Used: Random Forest Regressor
- R² Score: 0.8379
- RMSE: 28846.98
- MAE: 9788.75
- Output: Predicts bike claim settlement amount

### Car Claim Amount Model
- Model Used: Random Forest Regressor
- R² Score: 0.8571
- RMSE: 402621.1
- MAE: 164104.33
- Output: Predicts car claim settlement amount

---

## 3. Claim Approval Classification Models

### Bike Claim Approval Model
- Model Used: Random Forest Classifier
- Accuracy: 91%
- Precision: 93%
- Recall: 97%
- F1 Score: 95%
- Output: Predicts bike claim approval probability

### Car Claim Approval Model
- Model Used: Random Forest Classifier
- Accuracy: 91%
- Precision: 93%
- Recall: 96%
- F1 Score: 95%
- Output: Predicts car claim approval probability

---

## 4. RAG Chatbot Evaluation

- Vector Database: ChromaDB
- Embedding Model: HuggingFace Sentence Transformers
- LLM: Google Gemini API
- Test Method: Insurance-related questions were asked from Acko policy PDFs.
- Retrieval Result: Relevant policy chunks were retrieved from ChromaDB.
- Response Quality: Answers were grounded in retrieved document context.

Example Question:
> Does bike insurance cover theft?

Expected Result:
The chatbot should retrieve bike insurance policy content and explain whether theft is covered.

---

## 5. Manager AI Assistant Evaluation

The Manager AI Assistant was tested against live AWS RDS PostgreSQL data.

Sample Questions Tested:
- How many claims are submitted?
- How many bike claims are submitted?
- How many car claims are submitted?
- What is the average payout for bike claims?
- What is the average payout for car claims?
- How many quotations did we generate?
- What is the average premium?
- What are the top chatbot questions?
- Show me recent claims

Result:
The assistant successfully queried PostgreSQL and returned correct live values.

---

## 6. Deployment Evaluation

- EC2 Flask Application: Working
- Streamlit Dashboard: Working on port 8501
- AWS RDS PostgreSQL: Connected and operational
- AWS S3: Claim images uploaded successfully
- ChromaDB: Policy document chunks indexed successfully

---

## 7. Conclusion

The Acko Insurance AI Platform successfully combines Machine Learning, Generative AI, RAG, Computer Vision, AWS Cloud, PostgreSQL, Flask, and Streamlit into an end-to-end insurance AI system.