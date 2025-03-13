import os
from fastapi import FastAPI, File, UploadFile, Depends, HTTPException, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import torch
import torchvision.transforms as transforms
import pickle
from PIL import Image
import uvicorn

# Initialize FastAPI
app = FastAPI()

# Basic Authentication Setup
security = HTTPBasic()

# Fetch credentials from environment variables (or default values)
VALID_USERNAME = os.getenv("API_USERNAME", "admin")
VALID_PASSWORD = os.getenv("API_PASSWORD", "password123")

def authenticate(credentials: HTTPBasicCredentials = Security(security)):
    """Basic authentication for API access"""
    if credentials.username != VALID_USERNAME or credentials.password != VALID_PASSWORD:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid credentials")
    return credentials.username

# Load the model from the specified environment variable path
MODEL_PATH = os.getenv("MODEL_PATH", "custom_resnet18.pkl")

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    model.eval()
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Define CIFAR-10 class labels
classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Define image transformations (same as training)
transform = transforms.Compose([
    transforms.Resize((128, 128)),  # Resize image
    transforms.ToTensor(),  # Convert to PyTorch tensor
    transforms.Normalize(mean=[0.4914, 0.4822, 0.4465], std=[0.247, 0.2435, 0.261])  # Normalize
])

@app.get('/health-check')
async def health_check():
    """Check API health status"""
    return {"message": "API is healthy"}

@app.post("/predict")
async def predict(file: UploadFile = File(...), username: str = Depends(authenticate)):
    """
    Upload an image and get the predicted CIFAR-10 class.
    Requires Basic Authentication.
    """
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded. Check logs.")

    try:
        # Read and process the image
        image = Image.open(file.file).convert("RGB")  # Convert to RGB
        input_tensor = transform(image).unsqueeze(0)  # Apply transformations & add batch dim

        # Perform inference
        with torch.no_grad():
            output = model(input_tensor)

        # Get the predicted class
        _, predicted_class = torch.max(output, 1)
        predicted_label = classes[predicted_class.item()]

        return {"filename": file.filename, "predicted_class": predicted_label}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
