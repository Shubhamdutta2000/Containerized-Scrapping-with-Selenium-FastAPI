# Containerized-Scrapping-with-Selenium-FastAPI

Building and Running a Docker Container and Scrapping data using Selenium and with Fast API

The main goal of this repository is to deploy a Docker container with both, FastAPI and Selenium, to check the possibilities when we try to use FastAPI to receive parameters, and run a selenium process in the background to gather and parse data.
This example uses Selenium to make google search and scrap the links

## Build Setup

```
# Clone repo and cd into directory
git clone https://github.com/Shubhamdutta2000/Containerized-Scrapping-with-Selenium-FastAPI.git
cd Containerized-Scrapping-with-Selenium-FastAPI
```

```
# Install dependencies locally
pip install pipenv
pipenv shell
pipenv install
```

# How to Start

```
uvicorn main:app --reload
```

```
# Docker build
docker build  Containerized-Scrapping-with-Selenium-FastAPI

# Docker Run
docker run -d  -p 8000:8000  Containerized-Scrapping-with-Selenium-FastAPI

```

## About

<details>
<summary><strong>Contributing</strong></summary>

Pull requests and stars are always welcome. For bugs and feature requests, [please create an issue](../../issues/new).

</details>

### License

Released under the [MIT License](LICENSE).

---
