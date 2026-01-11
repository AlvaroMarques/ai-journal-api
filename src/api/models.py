from pydantic import BaseModel
from typing import Optional, List


class Secret:
    def __init__(self, value: str):
        self._value = value

    def get(self):
        return self._value

    def __repr__(self):
        return "<SECRET>"

    def __str__(self):
        return "<SECRET>"


class JournalEntry(BaseModel):
    model_name: str
    journal_entry: str
    links_accessed: Optional[List[str]]
