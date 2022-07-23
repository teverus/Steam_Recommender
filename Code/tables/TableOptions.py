from pydantic import BaseModel


class TableOptions(BaseModel):
    title: str
    rows: list
    current_position: list = [0, 0]
