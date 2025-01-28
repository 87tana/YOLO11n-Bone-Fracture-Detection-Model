# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the frontend code
COPY . /app

# Install dependencies
RUN pip install -r requirements_streamlit.txt

# Expose the Streamlit port
EXPOSE 8501

# Command to run Streamlit
ENTRYPOINT ["streamlit", "run"]
CMD ["streamlit_bonefracture.py"]
