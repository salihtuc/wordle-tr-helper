from pydantic import BaseModel
from typing import Optional, List


class WordRequest(BaseModel):
    word_arr: List[str]
    word_rnd: Optional[List[str]] = None


class Meaning(BaseModel):
    anlam: str


class WordDict(BaseModel):
    madde: str
    anlamlarListe: Optional[List[Meaning]] = None
