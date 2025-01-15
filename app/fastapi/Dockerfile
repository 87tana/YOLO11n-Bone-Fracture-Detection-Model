# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the app code and model
COPY ./app /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Command to run FastAPI
CMD ["uvicorn", "fastapi_bonefracture:app", "--host", "0.0.0.0", "--port", "8000"]

