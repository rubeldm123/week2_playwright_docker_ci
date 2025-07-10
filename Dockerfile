# Use official Python image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Install system dependencies required by Playwright browsers
RUN apt update && apt install -y wget

# Copy requirements file and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install Playwright browsers with dependencies
RUN python -m playwright install --with-deps

# Copy all project files into container
COPY . .

# Command to run the test
CMD ["pytest", "test_orangehrm_login.py", "-s"]
