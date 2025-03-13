# Image Classification Project

![Image Classification](https://img.shields.io/badge/Machine%20Learning-Image%20Classification-brightgreen)

## 🚀 Overview


https://github.com/user-attachments/assets/f6f42802-4183-449e-aa27-40441cbe6b2e


This project is an end-to-end Image Classification system using a custom **ResNet-18** model. It includes **FastAPI** for the backend, **Streamlit** for the frontend, and is containerized using **Docker**.

### 📌 GitHub Repository: [Project Repository](https://github.com/manishsoni123/Image-Classification)
### 🐳 Docker Images:
- **Backend (FastAPI):** `docker pull ms241/backend:latest`
- **Frontend (Streamlit):** `docker pull ms241/frontend:latest`

### 📁 Model Files:
- **Stored in `model/` folder**: `.pkl` and `.pth` model files.

### 🔑 API Authentication:
- **Default Credentials:**
  - **Username:** `admin`
  - **Password:** `password123`

🚨 **Note:** The backend service must be running on port **8090** before accessing the Streamlit UI.

---
## 📂 Project Structure
```
image-classification-project/
│── backend/               # FastAPI Backend
│── frontend/              # Streamlit Frontend
│── model/                 # Trained model files
│── docker-compose.yml     # Docker Compose file
│── EDA_training_evaluation.ipynb # Data Preprocessing & Training
```

### 🔍 Dataset: **CIFAR-10** (60,000 images, 10 classes)

### 🛠 Data Preprocessing
✅ Resized images, normalized pixels, and applied augmentation.  
✅ Converted images to PyTorch tensors.  
✅ Split dataset into **train, validation, and test sets**.  

### 🧠 Model Training
✅ Used **ResNet-18** CNN model (PyTorch).  
✅ Applied **early stopping** and **learning rate scheduling**.  
✅ Evaluated using **Accuracy, Precision, Recall, and Confusion Matrix**.  

### 🚀 Model Deployment
✅ **Backend:** FastAPI-based REST API with authentication.  
✅ **Endpoints:**
- `/health-check` → API health check.
- `/predict` → Upload image for classification.
✅ **Frontend:** Streamlit UI for user interaction.  
✅ **Dockerized Deployment:** Backend & frontend containerized using Docker.  

---
## 🏃 Running Instructions
### 🔹 Running Without Docker (Manual Execution)
1. Clone the repository:  
   ```bash
   git clone https://github.com/manishsoni123/Image-Classification.git
   ```
2. **Backend (FastAPI) Setup:**  
   ```bash
   cd backend
   python -m venv env  # Create virtual environment
   source env/bin/activate  # (Linux) Activate environment
   env\Scripts\activate  # (Windows) Activate environment
   pip install -r requirements.txt  # Install dependencies
   uvicorn app:app --host 0.0.0.0 --port 8090  # Start FastAPI
   ```
3. **Frontend (Streamlit) Setup:**  
   ```bash
   cd frontend
   pip install -r requirements.txt  # Install dependencies
   streamlit run app.py --server.port=8501 --server.address=0.0.0.0
   ```
4. **Access URLs:**  
   - **Backend:** `http://localhost:8090`
   - **Frontend:** `http://localhost:8501`

---
### 🔹 Running With Docker (Containerized Execution)
1. Clone the repository:  
   ```bash
   git clone https://github.com/manishsoni123/Image-Classification.git
   ```
2. **Run the application with Docker Compose:**  
   ```bash
   docker-compose up --build
   ```
3. **Alternative (Use Pre-Built Images from Docker Hub):**  
   ```bash
   docker pull ms241/backend:latest
   docker pull ms241/frontend:latest
   docker-compose up
   ```
4. **Access URLs:**  
   - **Backend:** `http://localhost:8090/health-check`
   - **Frontend:** `http://localhost:8501`

---
## 🔐 Authentication
- **Default Credentials:** `admin/password123`
- Can be modified using environment variables `API_USERNAME` and `API_PASSWORD`.

---
## 🎯 Bonus Features Implemented
✅ **Basic logging & error handling**  
✅ **Streamlit UI for user-friendly interaction**  
✅ **Dockerized deployment for smooth execution**  

---
## 🔮 Future Enhancements
🔹 Deploy on **AWS, GCP, Azure, or Render**.  
🔹 Implement **Grad-CAM or SHAP** for model explainability.  
🔹 Optimize model for **real-time inference**.  
🔹 Add **JWT authentication** for better security.  

---
## 📌 Conclusion
This project successfully demonstrates a **complete ML pipeline**, from **data preprocessing & model training** to **API deployment & frontend integration**. 🚀

