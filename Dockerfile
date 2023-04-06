# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in pyproject.toml and poetry.lock
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

# Define environment variable
# ENV NAME World

WORKDIR fragmenty

# Run app.py when the container launches
CMD ["scrapy", "crawl", "spider_name"]
