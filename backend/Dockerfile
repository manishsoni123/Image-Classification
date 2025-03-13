# Use official Python image
FROM python:3.13.1

# Set the working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install  --timeout=100 --retries=10 --no-cache-dir --no-deps --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -r requirements.txt


COPY . .

# Expose FastAPI port
EXPOSE 8090

# Run FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8090"]
