from pydantic import BaseModel, Field
from typing import Optional, List


class WordRequest(BaseModel):
    word_arr: List[str]
    word_rnd: Optional[List[str]] = None


class Meaning(BaseModel):
    meaning: str = Field(alias='anlam')


class WordDict(BaseModel):
    word: str = Field(alias='madde')
    meanings: Optional[List[Meaning]] = Field(default=None, alias='anlamlarListe')
