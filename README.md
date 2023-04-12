# Scrapy Project: Fragmenty

Fragmenty is a Scrapy project that crawls the Telegram's auction's platform, https://fragment.com/numbers, to extract and persist data about phone numbers that are up for auction. The data includes the phone number itself, the price, the memorability score, and the end of the bid time. The data is then stored in MongoDB.

In addition to the web crawler, the project includes custom middleware for running the project with an HTTP proxy and a custom pipeline for storing data in MongoDB. The project also includes scripts for generating charts based on data stored in MongoDB using Python's Plotly library.

## Tech Stack

- Python 3
- Scrapy
- MongoDB
- Plotly

## Installation and Setup

1. Clone the repository.

```
git clone https://github.com/Maders/fragmenty-spider.git
cd fragmenty-spider
```

2. Create and activate a virtual environment.

- I used poetry, If you are poetry user so you can install with `poetry install` command and skip virualenv creation step.

```
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the required packages.

   `pip install -r requirements.txt`

4. Rename `env.sample` to `.env` and configure the settings.

5. Start the MongoDB database using Docker Compose.

   `docker-compose up -d mongodb`

6. Wait for the database to start up (you can check the logs using docker-compose logs mongodb).

7. Start the web crawler.

   `scrapy crawl fragment-number`

## Docker Compose

This Docker Compose file sets up the MongoDB database that the Fragmenty Scrapy project uses to store data. Before running the Scrapy project, you need to start this Docker Compose setup to create the database.

- You also need to provide your own `MONGO_URI` and `MONGO_DATABASE` values in the `.env` file before running the Scrapy project.

## Usage

1. After starting the web crawler, the data will be stored in MongoDB.

2. To generate charts based on the data, run one of the scripts in `fragmenty-spider/scripts`.

   `python3 fragmenty-spider/scripts/chart.py`

## HTTP Proxy

If you want to use a list of HTTP proxies with the Scrapy project, you can fill the `HTTP_PROXY_LIST` in the `fragmenty/core/settings.py` file. The project includes a custom middleware that randomly selects a proxy from the list for each request. If you don't want to use a proxy, you can leave the `HTTP_PROXY_LIST` empty. The middleware will simply skip the proxy selection step.

## Related Project:

- The [`fragmenty`](https://github.com/Maders/fragmenty) repository contains the infrastructure provisioning code for the Fragmenty project using Amazon Web Services (AWS). The infrastructure is organized into different components.

- The [`fragmenty-api`](https://github.com/Maders/fragmenty-api) repository contains the API server code for the Fragmenty project. The API server provides a RESTful and Websocket interface. The API is built with the Scala programming language and the Play Framework.
