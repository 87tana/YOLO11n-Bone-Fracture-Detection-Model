# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /frontend

# Copy the frontend code
COPY ./frontend /frontend

# Install dependencies
RUN pip install -r requirements.txt

# Expose the Streamlit port
EXPOSE 8501

# Command to run Streamlit
CMD ["streamlit", "run", "streamlit_bonefracture.py", "--server.port", "8501", "--server.address", "0.0.0.0"]

