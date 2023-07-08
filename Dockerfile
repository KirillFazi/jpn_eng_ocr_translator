# Use an official Python runtime as the base image
FROM python:3.10.11

# Set the working directory in the container
WORKDIR /app

# Install Tesseract and other dependencies
RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip

# Copy the downloaded files to the Tesseract tessdata directory
COPY tessdata/* /usr/share/tesseract-ocr/4.00/tessdata/

# Copy the project files to the container
COPY . /app

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application will run on (if applicable)
EXPOSE 8000

# Define the command to run your application
CMD ["python", "app.py"]
