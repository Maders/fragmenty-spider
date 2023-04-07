# Use an official Python runtime as a parent image
from public.ecr.aws/lambda/python:3.9

# Set the working directory to /app
WORKDIR ${LAMBDA_TASK_ROOT}

# Copy the current directory contents into the container at /app
COPY ./fragmenty/ ${LAMBDA_TASK_ROOT}

# Install any needed packages specified in pyproject.toml and poetry.lock
RUN pip install --upgrade pip && \
    # pip install poetry && \
    # poetry config virtualenvs.create false && \
    pip install pymongo scrapy plotly python-dotenv

# Define environment variable
# ENV NAME World

# WORKDIR /app/fragmenty


# Run app.py when the container launches
# CMD ["scrapy", "crawl", "spider_name"]
CMD [ "lambda.handler" ]

