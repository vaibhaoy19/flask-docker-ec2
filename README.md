# 🚀 Hello World Flask App Dockerized on AWS EC2

A **Python Flask web application** containerized with **Docker** and deployed on **AWS EC2**.  
This project demonstrates how to build, containerize, and run a simple web app in a cloud environment.

---

## 📝 Project Overview

- **Project Name:** Hello World Flask App Dockerized on AWS EC2  
- **Language:** Python 3.11 (Flask)  
- **Containerization:** Docker  
- **Cloud Hosting:** AWS EC2 (Ubuntu 22.04 LTS)  
- **Purpose:** Learn containerization, cloud deployment, and show portfolio-ready DevOps project  

---

## 🖼 Architecture Diagram

Here’s a simple flow of the project:

┌───────────────┐
│ User │
└──────┬────────┘
│ HTTP Request (Port 5000)
▼
┌───────────────┐
│ AWS EC2 │
│ Ubuntu Server │
└──────┬────────┘
│ Runs Docker Container
▼
┌───────────────┐
│ Docker │
│ Container │
│ Flask App │
└──────┬────────┘
│ Responds with "Hello, Flask in Docker on AWS EC2!"
▼
┌───────────────┐
│ Browser │
└───────────────┘

yaml
Copy code

> You can later replace this ASCII diagram with an image using:
> `![Architecture](images/architecture.png)`

---

## 📂 Project Structure

flask-app/
├── app.py # Main Flask application
├── Dockerfile # Docker instructions to build container
└── requirements.txt # Python dependencies

yaml
Copy code

---

## ⚡ Features

- Runs a simple "Hello World" Flask application  
- Dockerized for portability and easy deployment  
- Hosted on AWS EC2 for cloud demonstration  
- Exposes port 5000 for web access  

---

## 💻 Setup & Run Locally

1. Clone the repository:
```bash
git clone https://github.com/vaibhaoy19/flask-docker-ec2.git
cd flask-docker-ec2
Build the Docker image:

bash
Copy code
docker build -t flask-app .
Run the Docker container:

bash
Copy code
docker run -d -p 5000:5000 flask-app
Open in browser:

arduino
Copy code
http://localhost:5000
You should see:
Hello, Flask in Docker on AWS EC2!

🌍 Deployment on AWS EC2
Launch Ubuntu EC2 instance

Install Docker:
sudo apt update -y
sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker

Clone the GitHub repository:
git clone https://github.com/vaibhaoy19/flask-docker-ec2.git
cd flask-docker-ec2

Build & run container:
docker build -t flask-app .
docker run -d -p 5000:5000 flask-app

Open your EC2 public IP in browser:
http://<EC2-Public-IP>:5000


Copy code
http://<EC2-Public-IP>:5000
✅ Expected Out
