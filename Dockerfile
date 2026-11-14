FROM python:3.14      # Start from a Python 3.14 environment

WORKDIR /app          # Create/use /app as the working directory

COPY . .              # Copy repository files into the container

RUN pip install pytest # Install pytest inside the container

CMD CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]  # Run run.py when the container starts
