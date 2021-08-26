from fastapi import FastAPI
from typing import Optional
from models.model import Text
from websearch import searchWithSelenium
import uvicorn
import re

app = FastAPI()


@app.get('/')
def hello_world():
    return {"greetings": "Hello from Containerized-Selenium-FastAPI"}


@app.post('/search')
def result(result: Text):
    res = re.sub(r"[^a-zA-Z0-9+[%][]? ]", "", result.text)
    print(res)
    return {"report": searchWithSelenium(str(res)), "submittedText": res}


# Run the API with uvicorn
# Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
