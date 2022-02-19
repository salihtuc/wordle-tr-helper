from fastapi import FastAPI, HTTPException
from utils import generate_regex, create_filter
from models import WordRequest, WordDict

from pymongo import MongoClient

app = FastAPI()

# Default connection parameters for MongoDB connection.
dbname = "dictionary"
username = "dbreader"
password = "dSd54KihNqqxacPy"

conn_string = "mongodb+srv://{}:{}@cluster0.tayhq.mongodb.net/{}?retryWrites=true&w=majority".format(username, password,
                                                                                                     dbname)
print(conn_string)

client = MongoClient(conn_string)


db = client[dbname]

col_dict = db["tr-dict"]


@app.post("/tr/words/find")
async def get_filtered_words(word: WordRequest):

    if word is None:
        err_msg = "Cannot get the input Order from the client."
        raise HTTPException(status_code=400, detail={"error": err_msg})

    print("------->")
    print(word)

    word_arr = word.word_arr
    word_rnd = word.word_rnd if word.word_rnd else []

    regex = generate_regex(word_arr, additional=word_rnd)

    results = [WordDict(**x) for x in col_dict.find(filter=create_filter(regex))]

    return results

