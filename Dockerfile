# Use the official Python 3.10 image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y curl

# Install pyenv to manage Python versions
RUN curl https://pyenv.run | bash

# Add pyenv to PATH
ENV PATH="/root/.pyenv/bin:$PATH"
RUN echo 'if command -v pyenv 1>/dev/null 2>&1; then eval "$(pyenv init -)"; fi' >> ~/.bashrc

# Install Python 3.10 using pyenv
RUN pyenv install 3.10.0
RUN pyenv global 3.10.0

# Install poetry
RUN pip install poetry

# Copy the Pyproject.toml and poetry.lock files to the container
COPY pyproject.toml poetry.lock /app/

# Install project dependencies using Poetry
RUN poetry install

# Copy your application code into the container
COPY . /app/

# Expose the port that your application will listen on
EXPOSE 8000

# Start your application using Uvicorn
CMD ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
