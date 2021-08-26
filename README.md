# Containerized-Selenium-FastAPI

Running a Docker Container with Fast API, and requesting data using selenium

The main objective of this repository is to deploy a Docker container with both, FastAPI and Selenium, to check the possibilities when we try to use FastAPI to receive parameters, and run a selenium process in the background to gather and parse data.
This example uses Selenium to make google search and scrap the links

## Build Setup

```
# Clone repo and cd into directory
git clone https://github.com/Prasundas99/mydiary.git
```

```
# Install dependencies locally
pip install pipenv
pip shell
pipenv install

```
```
# Docker build
docker build  Containerized-Selenium-FastAPI
docker run -d  -p 8080:8080  Containerized-Selenium-FastAPI

```



## About

<details>
<summary><strong>Contributing</strong></summary>

Pull requests and stars are always welcome. For bugs and feature requests, [please create an issue](../../issues/new).

</details>

### License
Released under the [MIT License](LICENSE).

***
