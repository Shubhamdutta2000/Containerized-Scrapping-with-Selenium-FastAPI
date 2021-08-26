from pydantic import BaseModel

# Text model


class Text(BaseModel):
    text: str
