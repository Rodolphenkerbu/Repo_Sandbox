# Start from a Python 3.14 environment
FROM python:3.14

# Create/use /app as the working directory
WORKDIR /app

# Copy repository files into the container
COPY . .

# Install dependencies
RUN pip install pytest fastapi uvicorn

# Start the API server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
