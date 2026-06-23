# Deployment Guide

## 1. Local Setup

Clone the repository:

```bash
git clone <repository_url>
cd Acko-AI-Platform
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 2. AWS EC2 Setup

Launch an Ubuntu EC2 instance and configure the security group.

Open ports:

* 22 (SSH)
* 5000 (Flask Application)
* 8501 (Streamlit Dashboard)

Connect to EC2 using SSH.

---

## 3. PostgreSQL (AWS RDS)

Create an AWS RDS PostgreSQL instance.

Update database configuration with:

* Host
* Database Name
* Username
* Password
* Port

Ensure the EC2 security group is allowed to access RDS.

---

## 4. AWS S3 Configuration

Create an S3 bucket for:

* Claim Images
* Claim Documents
* Model Artifacts

Configure AWS credentials on EC2.

---

## 5. Running the Flask Application

```bash
python app/app.py
```

Application URL:

```text
http://<EC2-Public-IP>:5000
```

---

## 6. Running the Streamlit Dashboard

```bash
streamlit run dashboard/dashboard.py --server.port 8501 --server.address 0.0.0.0
```

Dashboard URL:

```text
http://<EC2-Public-IP>:8501
```

---

## 7. Architecture

Frontend → Flask / Streamlit

Backend → Python, LangChain, Gemini, ML Models

Database → PostgreSQL (AWS RDS)

Storage → AWS S3

Deployment → AWS EC2
